from urllib import request
from fastapi import FastAPI
from pydantic import BaseModel #librería para manejo de datos
from typing import Text # importar el tipo de dato Text de pydantic
from datetime import datetime # importar el tipo de dato Datetime de pydantic
import requests  #Importamos la librería requests


app =  FastAPI()

notasEsutidante = []

# Modelo de datos
class objEstudiante(BaseModel):
    id: str
    codEstudiante: str
    nomEstudiante: Text
    asignatura: str
    programaAcademico: str
    nota: str
    fechaCreacion: datetime = datetime.now()
    usuario: str


@app.get('/')
def read_root():
    return{"Bienvenido": "Iniciaste mi servicio apiFastApi"}

@app.post('/insertar')
async def guardar_notaEstu(objEst: objEstudiante):
    notasEsutidante.append(objEst.dict())
    return "Registro guardado"

@app.get('/consultar')
def consultar_notasEst():
    return(notasEsutidante)

@app.get('/consultaBonus')
def consultarAPI():
    result = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    return(result.json())
