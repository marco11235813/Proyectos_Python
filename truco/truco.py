# Juego del Truco 


#Importamos las librerias/modulos que vamos a necesitar
import random


#--------------------------------------------------------------------------
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
    jugador= ['',baraja[0],baraja[2],baraja[4]]
    bot= [baraja[1],baraja[3],baraja[5]]
    
    return jugador, bot
#--------------------------------------------------------------------------
def ronda():

    irse= False
    jugador,bot= repartir()
    etiquetas= ['Primera', 'Segunda', 'Tercera']
    jugar= 'si'
    manos= []

    while irse == False:
        for mano in etiquetas:
            if jugar == 'si':                
                print(f"{mano} mano\n")
                jugador1(jugador)


                if mano == 'Primera':
                    print('\n')
                    e= envido(bot)

                t= input('\n----TRUCO----   -> SI/NO: ').lower()
                carta= input("que carta vas a tirar? ------> ").lower()

                if t == 'si':
                    truco(jugador[int(carta)],bot[0])
                else:
                    pass

                if carta == 'mazo':
                    salir= input('Estas seguro que das la ronda por terminada? SI/NO: ').lower()
                    if salir == 'si':
                        return 
                    else:
                        pass
                else:
                    print(f'\nCarta Jugador: {jugador[int(carta)]}')
                    random.shuffle(bot)
                    print(f'Carta PC: {bot[0]}\n')
                    
                    manos.append((jugador[int(carta)],bot[0]))
                    jugador.pop(int(carta))
                    bot.pop(0)
                    if mano == 'Tercera':
                        irse= True
                        break
                    else:
                        continue
                
            elif jugar == 'no':
                irse = True
                break

    return manos
#--------------------------------------------------------------------------
def jugador1(cartas= None)-> list|str|None:

    for idx, carta in enumerate(cartas):
        if carta == '':
            continue
        else:
            print(idx,' --->',carta,end= '  ')

    return 
#--------------------------------------------------------------------------
def envido(a):
    bot= a
    envido= False
    while envido == False:
        temp= input('quieres cantar envido? SI/NO   ').lower()
        if temp == 'si':
            envido= True
            print('ENVIDO')
            if (bot[0][1]== bot[1][1] or bot[0][1] == bot[2][1] or bot[1][1] == bot[2][1]) and envido == True:
                print('Quiero')
            else:
                print('No quiero') 
        elif temp == 'no':
            break
        else:
            print('Ingreso incorrecto. Debe responder si o no\n')

    return
#--------------------------------------------------------------------------
def truco(jugador:tuple, bot:tuple):

    valores= [(1,'espada'),(1,'basto'),(7,'espada'),(7,'oro'),(3,),(2,),((1,'oro'),(1,'copas')),(12,),(11,),(10,),((7,'basto'),(7,'copas')),(6,),(5,),(4,)]

    for valor in valores:
        if isinstance(valor[0],tuple):
            if jugador in valor:
                carta_jug= valores.index(valor)
            elif bot in valor:
                carta_bot= valores.index(valor)

        else:
            if isinstance(valor[0],int) and len(valor) == 2:
                if jugador == valor:
                    carta_jug= valores.index(valor)
                elif bot == valor:
                    carta_bot= valores.index(valor)
            elif len(valor) == 1:
                if jugador[0] == valor[0]:
                    carta_jug= valores.index(valor)
                elif bot[0] == valor[0]:
                    carta_bot= valores.index(valor)

    return carta_jug,carta_bot
#--------------------------------------------------------------------------
def puntaje(puntos: tuple):
    return
#--------------------------------------------------------------------------
def main():
    
    print(f'\n\nBienvenido al Juego del Truco!\n')
    nombre= input('Ingresa tu nombre: ')
    while True:
        print(f'\nJugador1: {nombre}')
        juego= ronda()
        print('\nFin de la ronda')
        continuar= input('Continuar?? SI/NO ').lower()

        if continuar == 'no':
            break
        else:
            print('-'*80)
            continue


    return
#--------------------------------------------------------------------------
if __name__ == '__main__':
    main()







