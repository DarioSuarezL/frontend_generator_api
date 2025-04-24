from pydantic import BaseModel, field_validator, Field, ValidationInfo, EmailStr
from pydantic_core import PydanticCustomError

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=6)
    repeat_password: str

    @field_validator('repeat_password', mode='after')
    @classmethod
    def check_passwords_match(cls, value: str, info: ValidationInfo) -> str:
        password = info.data.get("password")
        if password and value != password:
            raise PydanticCustomError('value_error', 'Passwords don\'t match')
        return value
    
    @field_validator("name")
    @classmethod
    def validate_name_length(cls, value: str) -> str:
        if len(value) < 3:
            raise PydanticCustomError('value_error', 'Name should have at least 3 characters')
        return value

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"