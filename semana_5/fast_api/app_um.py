from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import Role, User


app = FastAPI()

db: List[User] = [
    User(
        id=UUID("e3710fe2-7b11-42c8-98ee-6353a0abbced"), 
        first_name="Rai",
        last_name="Carneiro",
        email="email@email.com",
        role=[Role.role_1]
        ),
        User(
        id=UUID("e88ba775-978c-465a-a690-0ade624d846f"), 
        first_name="Hello",
        last_name="Carneiro",
        email="hello@email.com",
        role=[Role.role_2]
        ),
        User(
        id=UUID("b0d01dac-6b97-4113-82df-945b305a7cb7"), 
        first_name="Hellen",
        last_name="Carneiro",
        email="hellen@email.com",
        role=[Role.role_3]
        )
]

@app.get("/")
async def root():
    return {"message": "Hello, Rai!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id:": user.id}

@app.delete("api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com id {id} não encontrado!"
    )    


    
        
        



    
