from pydantic import BaseModel
from typing import List, Union

class ValidationErrorDetail(BaseModel):
    loc: List[Union[str, int]]
    msg: str
    type: str

class ValidationErrorResponse(BaseModel):
    detail: List[ValidationErrorDetail]