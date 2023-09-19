import numpy as np
import pandas as pd



## juego del BlackJack


valores= ['as',2,3,4,5,6,7,8,9,10,'jota', 'reina', 'rey']
palos= ['pica', 'corazones', 'trebol', 'diamante']
baraja=52
cantidad_barajas=6
apuesta_minima= 500

mano_cartas= 0


class usuario:
    def __init__(self,apuesta):
        cartas= 0
        self.apuesta= 0
        valor_mano= []
        if apuesta > 500:
            return "Debe realizar la apuesta minima de 500 para iniciar"
        else:
            self.apuesta += apuesta
    def mano_inicial(self,cartas,apuesta):
        cartas += 2
        return
    def apostar(self, apuesta):
        self.apuesta += apuesta
    def pedir_carta():
        return
    def plantarse():
        return
# class juego:
#     def __init__(self)

jugador1= usuario(400)
jugador1.apuesta
























