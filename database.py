from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker

#local database connection

engine=create_engine("postgresql://postgres:postgres@localhost/Arclif",echo=True)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)