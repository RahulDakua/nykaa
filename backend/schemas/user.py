from pydantic import BaseModel,Field,EmailStr


class Register(BaseModel):
    name : str
    phone : int
    mail : EmailStr
    password : str=Field(min_length=6)


class Login(BaseModel):
    mail : str
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str
    name : str


class UserStateData(BaseModel):
    cart: list[dict] = Field(default_factory=list)
    wishlist: list[str] = Field(default_factory=list)
