import os
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv

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

    