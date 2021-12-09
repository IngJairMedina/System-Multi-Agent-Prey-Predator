# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:33:59 2021

@author: JAIR_PC_JAPA
"""

from Propagar import propagar

prg=propagar()

class pas:
    def __init__(self):
        self.APt={}
        self.nombre='Pasto'
        self.propmax=100
        self.propmin=50
    
    def limpiar(self):
        self.APt.clear()
        
    def evaluar(self):
        L_A=prg.propagacion(self.APt, self.nombre, self.propmax, self.propmin)
        self.APt=L_A
        return self.APt