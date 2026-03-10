import requests
import random

def pokemon_(nombre):
    if nombre == '':
        nombre = random.randint(1,1025)
    while True:
        url = f'https://pokeapi.co/api/v2/pokemon/{nombre}'

        respuesta = requests.get(url)
        if respuesta.status_code != 200:
            nombre = input('El nombre ingresado no existe: ')
        else:
            break
    archivo = respuesta.json()
    return ((name(archivo),weight(archivo),height(archivo),tipe(archivo),gen(archivo))) #nombre, peso, altura, tipo

def gen(archivo):
    if archivo['id'] <= 151:
        return 1
    elif archivo['id'] <= 251:
        return 2
    elif archivo['id'] <= 386:
        return 3
    elif archivo['id'] <= 493:
        return 4
    elif archivo['id'] <= 649:
        return 5
    elif archivo['id'] <= 721:
        return 6
    elif archivo['id'] <= 809:
        return 7
    elif archivo['id'] <= 905:
        return 8
    elif archivo['id'] <= 1025:
        return 9
    else: 
        return 10

def name(archivo):
    names = archivo['name']
    return names

def weight(archivo):
    return int(archivo['weight'])

def height(archivo):
    return int(archivo['height'])

def tipe(archivo):
    lista = []
    for i in archivo['types']:
        lista.append(i['type']['name'])
    if len(lista) == 1:
        lista.append(None)
    return lista

def centrar(texto):
    texto = str(texto)
    palabra = texto.center(13)
    return palabra

def centrar1(texto):
    texto = str(texto)
    palabra = texto.center(12)
    return palabra


