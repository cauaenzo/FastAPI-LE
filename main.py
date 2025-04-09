from fastapi import FastAPI, HTTPException
from typing import List
from models import Usuario  # Importa o modelo Pydantic

app = FastAPI()

# Simulando um banco de dados na memória
usuarios_db: List[Usuario] = []

# --- ROTA EXTRA: GATINHO 🐱 ---
@app.get("/gatinho")
def mostrar_gatinho():
    return {
        "mensagem": "Aqui está um gatinho fofo para você!",
        "emoji": "🐱",
        "imagem": "https://placekitten.com/300/300"
    }

# --- CREATE ---
@app.post("/usuarios/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    usuarios_db.append(usuario)
    return usuario

# --- READ ALL ---
@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios_db

# --- READ ONE ---
@app.get("/usuarios/{usuario_id}", response_model=Usuario)
def obter_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# --- UPDATE ---
@app.put("/usuarios/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, novo_usuario: Usuario):
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            usuarios_db[index] = novo_usuario
            return novo_usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# --- DELETE ---
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            del usuarios_db[index]
            return {"mensagem": "Usuário deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
