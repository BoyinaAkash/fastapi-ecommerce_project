from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
# DATABASE_URL="mysql+pymysql://root:root@localhost:3306/ecommerce_db"
DATABASE_URL="mysql+pymsql://avnadmin:AVNS_xObL3o43wV0W1AXDUms@akash12ma-akashboyina-2925.a.aivencloud.com:17823/defaultdb
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)
Base=declarative_base()
