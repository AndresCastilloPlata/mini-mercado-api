# Archivo: app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importamos desde nuestros nuevos módulos
from . import models, schemas
from .database import SessionLocal, engine

# Crea las tablas en la base de datos (solo si no existen)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini-Mercado API")

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINT PARA PRODUCTOS ---
@app.get("/products", response_model=List[schemas.Product])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene una lista de productos desde la base de datos."""
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

# --- ENDPOINT PARA UN PRODUCTO ---
@app.get("/products/{product_id}", response_model=schemas.Product, status_code=200)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Si el producto existe, lo retornamos
    return product

# --- ENDPOINT PARA CREAR UN PRODUCTO ---
@app.post("/products", response_model=schemas.Product, status_code=201)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Crea un nuevo producto en la base de datos."""
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# --- ENDPOINT PARA ACTUALIZAR UN PRODUCTO ---
@app.put("/products/{product_id}", response_model=schemas.Product, status_code=200)
def update_product(product_id: int, product_update: schemas.ProductCreate, db: Session = Depends(get_db)):
    # PASO 1: Buscar el producto existente.
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    
    # Si no existe, lanzamos un error 404.
    if db_product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # PASO 2: Actualizar los campos del objeto que encontramos con los datos nuevos.
    # Usamos los datos de 'product_update' que vienen en la petición.
    db_product.name = product_update.name
    db_product.price = product_update.price
    db_product.stock = product_update.stock
    
     # PASO 3: Guardar los cambios en la base de datos.
    db.commit()
    db.refresh(db_product) # Refrescar para obtener el objeto actualizado desde la BD.
    
    return db_product

# --- ENDPOINT PARA ELIMINAR UN PRODUCTO ---
@app.delete("/products/{product_id}", status_code=200)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    
    # Lógica de búsqueda.
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    
    if db_product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # 2. Le decimos a SQLAlchemy que borre el objeto encontrado.
    db.delete(db_product)
    
    # 3. Guardamos los cambios en la base de datos para que la eliminación sea permanente.
    db.commit()
    
    # 4. Devolvemos un mensaje de éxito.
    return {"mensaje": "Producto eliminado con éxito"}
