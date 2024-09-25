from pydantic import BaseModel, EmailStr
from fastapi.param_functions import Form
from typing import Annotated

class User(BaseModel):
    email: EmailStr
    password: str
    name: str




