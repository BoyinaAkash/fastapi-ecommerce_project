from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import crud , schemas
from database import Base,engine,SessionLocal
Base.metadata.create_all(bind=engine)
app=FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def welcome():
    return {"message": "welcome to the ecommerce product" }
@app.post("/products",response_model=schemas.ProductResponse)
def create(product:schemas.ProductCreate,db:Session=Depends(get_db)):
    return crud.create_product(db,product)
@app.get("/products",response_model=list[schemas.ProductResponse])
def read_all(db:Session=Depends(get_db)):
    return crud.get_products(db)
@app.get("/products/{product_id}",response_model=schemas.ProductResponse)
def read_one(product_id:int,db:Session=Depends(get_db)):
    product=crud.get_product(db,product_id)
    if not product:
        raise HTTPException(status_code=404,detail="product not found")
    return product
@app.delete("/products/{product_id}")
def delete(product_id:int,db:Session=Depends(get_db)):
    deleted=crud.delete_product(db,product_id)
    if not deleted:
        raise HTTPException(status_code=404,detail="product not found")
    return {"message":"product deleted successfully"}
@app.get("/category/{category_name}",response_model=list[schemas.ProductResponse])
def category_products(db:Session=Depends(get_db),category_name=None):
    product_list=crud.get_by_category(db,category_name)
    if not product_list:
        raise HTTPException(status_code=404,detail="no products")
    return product_list

