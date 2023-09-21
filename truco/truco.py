# Juego del Truco 

import random



def repartir()-> tuple:

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
    jugador= baraja[[0,2,4]]
    bot= baraja[[1,3,5]]
    
    return jugador, bot

def mano(jugador,bot):

    irse= False
    jugador,bot= repartir()
    manos= ['Primera', 'Segunda', 'Tercera']

    while irse == False:
        for mano in manos:
            print(f"{manos} mano\n")
            jugar= input('jugas? SI/NO ').lower()
            
            if jugar == 'si':

                carta= int(input("que carta vas a tirar? 1/2/3 ------> "))
                print(f'\nCarta Jugador: {jugador[carta - 1]}')

                random.shuffle(bot)
                print(f'Carta PC: {bot[0]}\n')
                break
            elif jugar == 'no':
                irse = True
                break
            else:
                print('Elige una opcion')
                continue

    return

def jugador(promp= 'Ingresa tu nombre: '):
    nombre= input(promp)
    return nombre

def envido():

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

    return

def truco():
    return


def ronda():
    return

def puntaje():
    return

def main():
    print(f'\n\nBienvenido al Juego del Truco!')

    print('Fin de la ronda')
    input('Continuar?? SI/NO ').lower()

    return

if __name__ == '__main__':
    main()







