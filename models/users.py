from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    isActive: bool = True

class UpdateUser(BaseModel):
    name: str | None = None
    isActive: bool | None = None

class UpdateUserResponse(BaseModel):
    message: str
    user: User

class GetUsersResponse(BaseModel):
    users: List[User]

class CreateUserResponse(BaseModel):
    message: str
    user: User

class DeleteUserResponse(BaseModel):
    message: str
    user_id: int