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
    texto =str(texto)
    if texto == None:
        texto = "  "
    cantidad = (10 - len(texto))//2
    palabra = " "*cantidad + texto + " "*cantidad
    return palabra

class pokemon:
    def __init__(self,lista):
        self.nombre = lista[0]
        self.peso = lista[1]
        self.altura = lista[2]
        self.tipos = lista[3]
        self.igualdades = False
        self.generation = lista[4]

    def __comparar(self, pokemon, accion):
        if accion == 'peso':
            if pokemon.peso == self.peso:
                return '✅'
            elif pokemon.peso > self.peso:
                return '🔽'
            else:
                return '🔼'
        elif accion == 'altura':
            if pokemon.altura == self.altura:
                return '✅'
            elif pokemon.altura > self.altura:
                return '🔽'
            else:
                return '🔼'
        elif accion == 'gen':
            if pokemon.generation == self.generation:
                return '✅'
            elif pokemon.generation > self.generation:
                return '🔽'
            else:
                return '🔼'  
        else:
            if self.tipos[0] == pokemon.tipos[0]:
                tipo1 = '✅'
            elif self.tipos[1] == pokemon.tipos[0]:
                tipo1 = '🟨'
            else:
                tipo1 = '❌'
            
            if self.tipos[1] == pokemon.tipos[1]:
                tipo2 = '✅'
            elif self.tipos[0] == pokemon.tipos[1]:
                tipo2 = '🟨'
            else:
                tipo2 = '❌'
            
            return (tipo1,tipo2)

    def __str__(self):
        return(f'soy el pokemon: {self.nombre}')

    def igualdad(self,pokemon):
        tipo1, tipo2 = self.__comparar(pokemon,'tipo')
        altura = self.__comparar(pokemon,'altura')
        peso = self.__comparar(pokemon,'peso')
        generation = self.__comparar(pokemon,'gen')

        if tipo1 == '✅' and tipo2 == '✅' and altura == '✅' and peso == '✅' and generation == '✅':
            self.igualdades = True
    
        print(f'{centrar(pokemon.tipos[0])} {centrar(pokemon.tipos[1])} {centrar(str(int(pokemon.peso)/10)+"KG")} {centrar(str(int(pokemon.altura)/10)+"M")} {centrar(pokemon.generation)}' ) 
        print(f'{centrar(tipo1)}{centrar(tipo2)}{centrar(peso)}  {centrar(altura)}{centrar(generation)}' ) 


pokemon_misterioso = pokemon(pokemon_(''))
pokemon_mio = pokemon(pokemon_(input('ingrese el nombre de un pokemon: ')))
contador = 0
print(centrar("tipo1")+centrar("   tipo2") +centrar("    peso")+ centrar("     Altura")+centrar("   generación") ) 

while pokemon_misterioso.igualdades != True:
    contador +=1
    pokemon_misterioso.igualdad(pokemon_mio)
    if pokemon_misterioso.igualdades != True:
        pokemon_mio = pokemon(pokemon_(input()))
        if contador == 11 and pokemon_misterioso.igualdades != True:
            print(pokemon_misterioso)
            print('Perdiste😢😢')
            break
    else:
        print('Ganaste🎉🎉🎉')





