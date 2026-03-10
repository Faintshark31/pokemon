from f_pokemon import centrar, centrar1

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
        print(f'|{centrar(pokemon.tipos[0])}|{centrar(pokemon.tipos[1])}|{centrar(str(int(pokemon.peso)/10)+"KG")}|{centrar(str(int(pokemon.altura)/10)+"M")}|{centrar(pokemon.generation)}|' ) 
        print(f'|{centrar1(tipo1)}|{centrar1(tipo2)}|{centrar1(peso)}|{centrar1(altura)}|{centrar1(generation)}|') 
