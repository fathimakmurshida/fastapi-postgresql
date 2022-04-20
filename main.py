
from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel

from database import SessionLocal
from typing import List
import models

app=FastAPI()

class config:
    orm_mode=True


class User_register(BaseModel): #serializer
    user_id:int
    name:str
    phone:str

db=SessionLocal()
@app.get('/')
def index():
    return{"message":"hello world"}

@app.get('/users')
def get_all_users():
    users=db.query(models.Register).all()
    return users

@app.get('/users/{user_id}')
def get_an_user(user_id:int):
    user=db.query(models.Register).filter(models.Register.id==user_id).first()

    return user

@app.post('/users')
def create_an_user(user:User_register):
    new_user=models.Register(
        name=user.name,
        phone=user.phone

    )

    db_user=db.query(models.Register).filter(user.name==new_user.name).first()
    if db_user is not None:
        raise HTTPException(status_code=400,detail="item already exists")

    db.add(new_user)
    db.commit()
    return new_user


@app.put('/user/{user_id}')
def update_an_user(user_id:int,user:User_register):
    user_to_update=db.query(models.Register).filter(models.Register.id==user_id).first()
    user_to_update.name=user.name
    user_to_update.phone=user.phone

    db.commit()
    return user_to_update

@app.delete('/user/{user_id}')
def delete_an_user(user_id:int):
    item_to_delete=db.query(models.Register).filter(models.Register.id==user_id).first()
    
    if item_to_delete is  None:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="resource not found")

    return item_to_delete