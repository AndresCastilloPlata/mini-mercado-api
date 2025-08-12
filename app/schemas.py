from pydantic import BaseModel

# Esquema base con los campos comunes
class ProductBase(BaseModel):
    name: str
    price: float
    stock: int

# Esquema para la creación (no se necesita ID)
class ProductCreate(ProductBase):
    pass

# Esquema para la lectura (incluye el ID)
class Product(ProductBase):
    id: int

    class Config:
        # Permite que Pydantic lea datos desde modelos de SQLAlchemy
        from_attributes = True