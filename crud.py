from sqlalchemy.orm import session
import bcrypt
import models
import schemas

#create product
def create_product(db:session,product:schemas.ProductCreate):
    db_product=models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
#get all products
def get_products(db:session):
    return db.query(models.Product).all()

#get product by id
def get_product(db:session,product_id:int):
    return db.query(models.Product).filter(
        models.Product.id == product_id
        ).first()
# get product by category
def get_by_category(db:session,category_name:str):
    return db.query(models.Product).filter(
        models.Product.category == category_name
    ).all()

# update the products
def update_product(db:session,product_id :int,product:schemas.ProductCreate):
    db_product = get_product(db,product_id)
    if not db_product:
        return None
    db_product.category=product.category
    db_product.product_name=product.product_name
    db_product.price=product.price
    db_product.stock=product.stock
    db.commit()
    db.refresh(db_product)
    return db_product

#delete the products
def delete_product(db:session,product_id:int):
    db_product=get_product(db,product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product


