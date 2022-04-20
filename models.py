from enum import unique
from database import Base

from sqlalchemy import String,Boolean,Integer,Column

class Register(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    phone=Column(String(255),nullable=False,unique=True)
 
    #def __repr__(self):
        #return f"<user_register name={self.name} phone={self.phone}>"              
