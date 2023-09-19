# Juego del Truco 

import random

nombre= input('Ingresa tu nombre ').lower()

print(f'\n\nBienvenido {nombre.capitalize()} al Juego del Truco!')

# iniciar= input("Queres jugar? SI/NO ").lower()
# if iniciar == 'no':
#     print("Juguemos la proxima!")


# matriz de valores
## creamos el mazo de cartas con el que vamos a jugar
palos= ['espada', 'basto', 'oro', 'copas']
numeros= [1,2,3,4,5,6,7,10,11,12]

baraja= []

for palo in palos:
    for num in numeros:
        valor= num,palo
        baraja.append(valor)

#mezclamos
random.shuffle(baraja)
random.shuffle(baraja)
random.shuffle(baraja)

# repartimos
jugador= baraja[0:3]
bot= baraja[4:7]


##funcionalidad de la ronda/mano
print(f'\n{jugador}')

envido= False
while envido == False:
    temp= input('quieres cantar envido? SI/NO   ').lower()
    if temp == 'si':
        envido= True
        print('ENVIDO')
    elif temp == 'no':
        break
    else:
        print('Ingreso incorrecto. Debe responder si o no\n')

if (bot[0][1]== bot[1][1] or bot[0][1] == bot[2][1] or bot[1][1] == bot[2][1]) and envido == True:
    print('QUIERO')
    # sum([])

   
irse= False

while irse == False:
    print("Primera mano\n")
    jugar= input('jugas? SI/NO ').lower()
    
    if jugar == 'si':
        primera= int(input("que carta vas a tirar? 1/2/3 ------> "))
        print(f'\nCarta Jugador: {jugador[primera - 1]}')
        random.shuffle(bot)
        print(f'Carta PC: {bot[0]}\n')
        break
    elif jugar == 'no':
        irse = True

print('Fin de la ronda')
input('Continuar?? SI/NO ').lower()











