from datetime import datetime
import email
from typing import Optional
from winreg import ConnectRegistry
from pydantic import BaseModel,EmailStr
from pydantic.types import conint

class UserCreate(BaseModel):
    email: EmailStr
    password:str
class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email: EmailStr
    password:str

class PostBase(BaseModel):
    #defining what goes in the body.
    title:str
    content:str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut

    class Config:
        orm_mode=True

class PostOut(BaseModel):
    Post:Post
    votes:int
    class Config:
        orm_mode=True


class Token(BaseModel):
    access_token: str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]=None

class Vote(BaseModel):
    post_id:int
    dir:conint(ge=0,le=1)


