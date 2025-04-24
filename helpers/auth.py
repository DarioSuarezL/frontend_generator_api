from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt

from config.jwt import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRES_IN

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)

def generate_access_token(data:dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(hours=JWT_EXPIRES_IN))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, key=JWT_SECRET, algorithm=JWT_ALGORITHM)