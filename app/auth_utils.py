import os
from datetime import datetime, timedelta, timezone
 
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
 
from app.database import get_db
from app.models import User

load_dotenv()

# Password Hashing
bcrypt_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    return bcrypt_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return bcrypt_context.verify(
        plain_password,
        hashed_password
    )
    
# JWT Configuration

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
 
# Create JWT

def create_access_token(
    username: str,
    user_id: int
):
    encode = {
        "sub": username,
        "id": user_id
    }
    expires = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    encode.update({
        "exp": expires
    })
    return jwt.encode(
        encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

# Get current logged-in user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
 
 
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
 
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
 
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
 
    return user