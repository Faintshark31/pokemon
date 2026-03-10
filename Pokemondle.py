from f_pokemon import centrar, pokemon_
from c_pokemon import pokemon


pokemon_misterioso = pokemon(pokemon_(''))
pokemon_mio = pokemon(pokemon_(input('ingrese el nombre de un pokemon: ')))
contador = 0
print(f"|{centrar("tipo1")}|{centrar("tipo2")}|{centrar("peso")}|{centrar("Altura")}|{centrar("generación")}|") 
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



