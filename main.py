from fastapi import FastAPI

app = FastAPI()

@app.get("/dog")
def get_dog():
    dog = {
        "name": "Rex",
        "breed": "Labrador Retriever",
        "age": 5,
        "color": "Amarelo",
        "friendly": True
    }
    return dog
