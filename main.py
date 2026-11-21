from fastapi import FastAPI
from routers.users import router as users_router
from routers.productos import router as productos_router

app = FastAPI()

app.include_router(users_router)
app.include_router(productos_router)

@app.get("/")
def read_root():
    mensaje = "Tp 1 Final Programacion 4 Backend"
    return {"message": mensaje}