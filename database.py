from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker , declarative_base
load_dotenv()
# DATABASE_URL="mysql+pymysql://root:root@localhost:3306/ecommerce_db"
DATABASE_URL=os.getenv("DATABASE_URL")
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)
Base=declarative_base()
