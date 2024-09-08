from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date
import models.banco_em_memoria as banco

app = FastAPI()

class Noticia(BaseModel): # definição da estrutura e validação dos dados
    titulo: str
    conteudo: str
    autor: str
    publicado: bool
    data_criacao: Optional[date] = None # campo opcional

@app.post("/cadastrar/")
def cadastrar_noticia(noticia: Noticia): # cadastra uma nova notícia no banco de dados
    try: 
        banco.nova_noticia(
            noticia.titulo,
            noticia.conteudo,
            noticia.publicado,
            noticia.autor
        )
        return {"mensagem": "Notícia cadastrada com sucesso!"} # 
    except:
        return {"mensagem": "Erro ao cadastrar notícia."}

@app.get("/listar/")
def listar_noticias(): 
    try:
        return banco.listagem()
    except:
        return {"mensagem": "Erro ao listar notícias."}

@app.get("/listar/{id}")
def listar_noticia(id: int): 
    try:
        return banco.listagem_por_id(id)
    except:
        return {"mensagem": "Notícia não encontrada."}
    
@app.put("/editar/{id}")
def editar_noticia(id: int, noticia: Noticia):
    try:
        banco.editar_noticia(
            id,
            noticia.titulo,
            noticia.conteudo,
            noticia.publicado,
            noticia.autor
        )
        return {"mensagem": "Notícia editada com sucesso!"}
    except:
        return {"mensagem": "Erro ao editar notícia."}
    
@app.delete("/deletar/{id}")
def deletar_noticia(id: int):
    try:
        banco.remover_noticia(id)
        return {"mensagem": "Notícia deletada com sucesso!"}
    except:
        return {"mensagem": "Erro ao deletar notícia."}