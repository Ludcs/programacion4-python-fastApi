from pydantic import BaseModel


class Producto(BaseModel):
    id: int
    nombre: str
    categoria: str
    precio: float
    disponible: bool = True


class UpdateProducto(BaseModel):
    nombre: str | None = None
    categoria: str | None = None
    precio: float | None = None
    disponible: bool | None = None


class GetProductosResponse(BaseModel):
    productos: list[Producto]


class CreateProductoResponse(BaseModel):
    message: str
    producto: Producto


class UpdateProductoResponse(BaseModel):
    message: str
    producto: Producto


class DeleteProductoResponse(BaseModel):
    message: str
    producto_id: int