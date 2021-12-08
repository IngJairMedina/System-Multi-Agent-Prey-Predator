# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:55:48 2021

@author: JAIR_PC_JAPA
"""

from Nacer import nacer
from Aparear import aparear
from Cazar import cazar
from Mover import mover
from Conej import conej

ncr=nacer()
apr=aparear()
czr=cazar()
mvr=mover()
cnj=conej()

class comad:
    def __init__(self):
        self.ACm={}
        self.nombre='Comadreja'
        self.hipo=10
        self.vmax=720
        self.vmin=360
        self.vminrep=90
        self.vmaxrep=360
        self.dias_tick=30
        self.probapar=0.7
        self.probgest=0.7
        self.nminnac=4
        self.nmaxnac=8
        self.tiempoNuevaGesta=120
        self.tiempoGesta=30
        self.energiaXtick=1
        self.RA=10
        self.tick_s_comer_max=4
        
    def limpiar(self):
        self.ACm.clear()
        
    def evaluar(self,presa):
        L_A0=ncr.nacimiento(self.ACm, self.nombre, self.nminnac, self.nmaxnac, self.vmin, self.vmax)
        self.ACm=L_A0
        L_A1=apr.apareo(self.ACm, self.nombre,self.dias_tick, self.vminrep, self.vmaxrep, self.RA, self.probapar, self.probgest, self.tiempoGesta, self.tiempoNuevaGesta)
        self.ACm=L_A1
        L_A2,L_AP=czr.caza(self.ACm, presa, self.nombre, cnj.nombre, self.RA)
        self.ACm=L_A2
        L_A3=mvr.movimineto(self.ACm, self.nombre, self.hipo, self.dias_tick, self.energiaXtick)
        self.ACm=L_A3
        return self.ACm,L_AP