import random

## juego del ahorcado


##preparamos e inicializamos algunas variables basicas
palabra= []                                                 #-----------------> esta variable nos sirve para proyectar la cantidad de espacios a completar que va a tener la palabra
palabras_random= ['camisa', 'pelota', 'celular', 'lampara'] #------------> este es nuestra base de valores de donde se va a obtener la palabra a completar
random.shuffle(palabras_random)                             # ------------> mezclamos los valores dentro de la lista de palabras, para que se elija una palabra al azar en cada intento
intentos= 3                                                 #------------>  variable que utilizamos condicion para terminar el juego
valores_probados= []                                        # ------------> valores/letras que ya se utilizaron o ingresaron en el input
repeticiones= 0                                             #------------>  variable que utilizamos para terminar el juego
rondas= [x for x in range(1, len(palabras_random)+1)]       # -----------> list comprehension, basicamente creamos una nueva lista con la iteracion del rango




lista= ["a",'b','c','d','e','f'                             # ------------> matriz/lista de valores utilizada como comparacion para validar los caracteres ingresados como input
        ,'g','h','i','j','k','l',            
        'm','n','ñ','o','p','q','r'
        ,'s','t','u','v','w','x','y','z']


# funcionamiento del juego
for ronda in rondas:

    #construimos la presentacion/interfaze
    print(f'\n\nRONDA {ronda}')
    palabra= ['_']*len(palabras_random[0])                      # -------------> construimos la 'capsula' donde ingresaran los valores correctos para armar la palabra
    print(f"{','.join(palabra)}\n\n")                           # --------------> a fines visuales y practicos, unimos las 'celdas' de la capsula para darle salida como un solo string
    print(palabras_random[0])                                   


    while intentos != 0 and repeticiones != 3 and '_' in palabra: ## condiciones 
        letra= input('elije una letra: ').lower()

        #evaluaciones del valor ingresado como input
        if len(letra) == 0 or len(letra) > 1: 
            print('\nPuedes ingresar de a una letra!!\n')
            continue
        else:

            if letra not in lista:
                print("\ncaracter incorrecto\n")
                continue
            elif letra in valores_probados:
                repeticiones +=1
                if repeticiones == 3:
                    break
                print('\nYa utilizaste esta letra!\n')
                continue
            elif letra not in list(palabras_random[0]):
                intentos -=1
                if intentos == 0:
                    break
                print('\nFallaste! intentalo nuevamente\n')
                # print(f'"Te quedan {intentos} intentos"')
                continue
            else:
                valores_probados.append(letra)                 ## agregamos a una lista, el valor ingresado como input, para comparar con futuros inputs y evitar su repeticion
                for idx, x in enumerate(palabras_random[0]):   
                    if x== letra:
                        palabra[idx] = letra
                print(f"{''.join(palabra)}\n\n")


    if repeticiones == 3 or intentos == 0: ## resultados
        print('\nFin del juego')
        break
    else:
        if len(palabras_random) == 1:
            print('Pasaste el juego!!\n Eres el campeon!\nGracias por jugar al Juego del ahorcado :)')
            break
        else:
            print('GANASTE!!!')
            print('Quieres continuar??')
    respuesta= input('SI / NO ----->  ').lower()

    if respuesta == 'si':
        palabra= []                                                 
        palabras_random.remove(palabras_random[0])
        random.shuffle(palabras_random)                             
        intentos= 3                                                 
        valores_probados= []                                        
        repeticiones= 0 
        continue
    if respuesta == 'no':
        print('Gracias por jugar!!')
        break