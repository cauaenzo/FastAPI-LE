# FastAPI-LE

## Conceitos Principais do FastAPI

### FastAPI
FastAPI é um framework moderno, rápido (alta performance) para construir APIs com Python 3.7+ baseado em padrões como OpenAPI e JSON Schema.

### Aplicação (app)
É a instância principal criada a partir da classe `FastAPI()`. Serve para registrar rotas, middlewares e configurações da API.

```python
from fastapi import FastAPI
app = FastAPI()
```
### Endpoint com Rota
```python
@app.get("/items/")
def read_items():
    return {"items": ["item1", "item2"]}
```
### Métodos HTTP
FastAPI suporta os principais métodos HTTP:

- GET: Buscar dados

- POST: Criar dados

- PUT: Atualizar dados

- DELETE: Remover dados

### Pydantic
Biblioteca para validação e parsing de dados. FastAPI usa Pydantic para definir e validar modelos de dados (schemas) usados nas requisições e respostas.

- python
- Copiar
- Editar

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
```

### Tipagem
FastAPI usa tipagem do Python para validação automática e documentação da API.

### Documentação automática
FastAPI gera automaticamente documentação interativa (Swagger UI e ReDoc) acessível via /docs e /redoc.

###  Dependências
FastAPI permite injeção de dependências para organizar código e compartilhar recursos.

### Execução
Para executar a API, utiliza-se servidores ASGI como Uvicorn ou Hypercorn.

Exemplo para rodar com Uvicorn:

```bash
uvicorn main:app --reload
```


