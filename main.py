from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def read_root():
    mensaje = "Tp 1 Final Programacion 4 Backend"
    return {"message": mensaje}