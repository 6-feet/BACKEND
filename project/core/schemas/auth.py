from pydantic import BaseModel


class AuthDetails(BaseModel):
    login: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
