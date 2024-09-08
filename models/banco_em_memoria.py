import uuid
from datetime import datetime

banco = {} 

def nova_noticia( 
    titulo: str,
    conteudo: str,
    publicado: bool,
    autor: str
):
    identificador = uuid.uuid4().int # gera um identificador único
    data_criacao = str(datetime.now()) # pega a data e hora atual e converte para string
    banco[identificador] = {
        'id': identificador,
        'titulo': titulo,
        'conteudo': conteudo,
        'autor': autor,
        'publicado': publicado,
        'data_criacao': data_criacao
    }
    return banco[identificador] 

def listagem():
    return banco

def listagem_por_id(identificador: int):
    return banco[identificador]

def editar_noticia(
    identificador: int,
    titulo: str,
    conteudo: str,
    publicado: bool,
    autor: str
):
    data_criacao = str(datetime.now())
    banco[identificador] = {
        'id': identificador,
        'titulo': titulo,
        'conteudo': conteudo,
        'autor': autor,
        'publicado': publicado,
        'data_criacao': data_criacao
    }
    return banco[identificador]

def remover_noticia(identificador: int):
    del banco[identificador]