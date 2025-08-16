from pydantic import BaseModel, ConfigDict

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

    model_config = ConfigDict(from_attributes=True)
        

# --- Esquemas para Usuarios ---
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)