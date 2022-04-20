from database import Base,engine
from models import user_register

print("creating database...")

Base.metadata.create_all(engine)