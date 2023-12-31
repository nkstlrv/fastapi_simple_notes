from pydantic import BaseModel, Field


class Note(BaseModel):
    title: str
    body: str
    # user_id: int


class NoteList(BaseModel):
    title: str
    body: str
    user_id: int
    created_at: str
    edited_at: str

    # class Config:
    #     orm_mode = True


class User(BaseModel):
    username: str = Field(strip_whitespace=True)
    email: str = Field(strip_whitespace=True)
    password: str


class UserUpdateEmail(BaseModel):
    email: str = Field(strip_whitespace=True)


class UserUpdateUsername(BaseModel):
    username: str = Field(strip_whitespace=True)


class UserUpdatePassword(BaseModel):
    # old_password: str
    password1: str
    password2: str


class LoginSchema(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
