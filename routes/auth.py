from fastapi import APIRouter, HTTPException, Depends

from helpers.auth import (
    hash_password,
    generate_access_token,
    verify_password,
    get_current_user,
)
from schemas.user import UserCreate, Token, UserLogin, UserResponse
from schemas.error import ValidationErrorResponse
from models.user import User

router = APIRouter()


@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    existing = await User.get_or_none(email=user.email)
    if existing:
        raise HTTPException(
            status_code=422,
            detail=[
                {
                    "loc": ["body", "email"],
                    "msg": "The mail is already in use",
                    "type": "value_error",
                }
            ],
        )
    hashed_password = hash_password(user.password)
    new_user = await User.create(
        name=user.name, email=user.email.lower().strip(), password=hashed_password
    )
    token = generate_access_token({"email": new_user.email, "sub": str(new_user.id)})
    return {"access_token": token}


@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    existing = await User.get_or_none(email=user.email)
    if not existing:
        raise HTTPException(
            status_code=422,
            detail=[
                {
                    "loc": ["body", "email"],
                    "msg": "The email is not associated with us",
                    "type": "value_error",
                }
            ],
        )
    if not verify_password(user.password, existing.password):
        raise HTTPException(
            status_code=422,
            detail=[
                {
                    "loc": ["body", "password"],
                    "msg": "Wrong password",
                    "type": "value_error",
                }
            ],
        )
    token = generate_access_token({"email": existing.email, "sub": str(existing.id)})
    return {"access_token": token}


@router.get("/me", response_model=UserResponse)
async def me(user: User = Depends(get_current_user)):
    return user
