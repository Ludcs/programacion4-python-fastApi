from fastapi import APIRouter, HTTPException, status
from models.users import (User, GetUsersResponse, CreateUserResponse, DeleteUserResponse, UpdateUser, UpdateUserResponse)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez", isActive=True),
    User(id=2, name="pepe sanchez", isActive=False),
]

@router.get("/users")
def get_users(is_active: bool | None = None) -> GetUsersResponse:
    if is_active is None:
        return GetUsersResponse(users=usuarios)

    filtrados = [user for user in usuarios if user.isActive == is_active]
    return GetUsersResponse(users=filtrados)

@router.post("/users")
def create_user(user: User) -> CreateUserResponse:
    usuarios.append(user)
    r = CreateUserResponse(message="Usuario creado correctamente", user=user)
    return r

@router.patch("/users/{user_id}")
def update_user(user_id: int, payload: UpdateUser) -> UpdateUserResponse:
    for index, user in enumerate(usuarios):
        if user.id == user_id:
            data = payload.model_dump(exclude_unset=True)
            updated_user = user.model_copy(update=data)
            usuarios[index] = updated_user
            return UpdateUserResponse(message="Usuario actualizado correctamente", user=updated_user)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )

@router.delete("/users/{user_id}")
def delete_user(user_id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == user_id:
            usuarios.remove(user)
            r = DeleteUserResponse(message="Usuario eliminado correctamente", user_id=user_id)
            return r
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

