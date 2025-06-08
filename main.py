from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo Pydantic que define a estrutura dos dados do cachorro
class Dog(BaseModel):
    name: str
    breed: str
    age: int
    friendly: bool

# Endpoint para criar um cachorro recebendo dados via POST
@app.post("/dogs/")
def create_dog(dog: Dog):
    return {
        "message": "Cachorro criado com sucesso!",
        "dog": dog
    }
