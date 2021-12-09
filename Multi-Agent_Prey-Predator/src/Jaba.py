# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:00:47 2021

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

class jaba:
    def __init__(self):
        self.AJb={}
        self.nombre='Jabali'
        self.hipo=15
        self.vmax=5400
        self.vmin=3600
        self.vminrep=360
        self.vmaxrep=2880
        self.dias_tick=30
        self.probapar=0.7
        self.probgest=0.7
        self.nminnac=3
        self.nmaxnac=5
        self.tiempoNuevaGesta=360
        self.tiempoGesta=120
        self.energiaXtick=1
        self.RA=15
        self.tick_s_comer_max=8
        
    def limpiar(self):
        self.AJb.clear()
        
    def evaluar(self,presa):
        L_A0=ncr.nacimiento(self.AJb, self.nombre, self.nminnac, self.nmaxnac, self.vmin, self.vmax)
        self.AJb=L_A0
        L_A1=apr.apareo(self.AJb, self.nombre,self.dias_tick, self.vminrep, self.vmaxrep, self.RA-5, self.probapar, self.probgest, self.tiempoGesta, self.tiempoNuevaGesta)
        self.AJb=L_A1
        L_A2,L_AP=czr.caza(self.AJb, presa, self.nombre, cnj.nombre, self.RA)
        self.AJb=L_A2
        L_A3=mvr.movimineto(self.AJb, self.nombre, self.hipo, self.dias_tick, self.energiaXtick)
        self.AJb=L_A3
        return self.AJb,L_AP