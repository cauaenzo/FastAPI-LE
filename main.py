from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_dog():
    dog = {
        "name": "Rex",
        "breed": "Labrador Retriever",
        "age": 5,
        "color": "Amarelo",
        "friendly": True
    }
    return dog
