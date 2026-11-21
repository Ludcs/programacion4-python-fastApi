from fastapi import APIRouter, HTTPException, status
from models.productos import (
    Producto,
    UpdateProducto,
    GetProductosResponse,
    CreateProductoResponse,
    UpdateProductoResponse,
    DeleteProductoResponse,
)

router = APIRouter()

productos: list[Producto] = [
    Producto(id=1, nombre="Yerba Suave 1kg", categoria="almacen", precio=3500.0, disponible=True),
    Producto(id=2, nombre="Granola con Frutos Secos", categoria="dietetica", precio=4800.0, disponible=False),
]


@router.get("/productos")
def get_productos(categoria: str | None = None, disponible: bool | None = None) -> GetProductosResponse:
    resultado = productos

    if categoria is not None:
        resultado = [p for p in resultado if p.categoria.lower() == categoria.lower()]

    if disponible is not None:
        resultado = [p for p in resultado if p.disponible == disponible]

    return GetProductosResponse(productos=resultado)


@router.get("/productos/{producto_id}")
def get_producto_by_id(producto_id: int) -> Producto:
    for producto in productos:
        if producto.id == producto_id:
            return producto

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado",
    )


@router.post("/productos", status_code=status.HTTP_201_CREATED)
def create_producto(producto: Producto) -> CreateProductoResponse:
    productos.append(producto)
    return CreateProductoResponse(message="Producto creado correctamente", producto=producto)


@router.patch("/productos/{producto_id}")
def update_producto(producto_id: int, payload: UpdateProducto) -> UpdateProductoResponse:
    for index, producto in enumerate(productos):
        if producto.id == producto_id:
            data = payload.model_dump(exclude_unset=True)
            updated = producto.model_copy(update=data)
            productos[index] = updated
            return UpdateProductoResponse(message="Producto actualizado correctamente", producto=updated)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado",
    )


@router.delete("/productos/{producto_id}")
def delete_producto(producto_id: int) -> DeleteProductoResponse:
    for producto in productos:
        if producto.id == producto_id:
            productos.remove(producto)
            return DeleteProductoResponse(message="Producto eliminado correctamente", producto_id=producto_id)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado",
    )