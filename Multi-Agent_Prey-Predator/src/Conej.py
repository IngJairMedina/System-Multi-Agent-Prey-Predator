# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:47:31 2021

@author: JAIR_PC_JAPA
"""
from Nacer import nacer
from Aparear import aparear
from Cazar import cazar
from Mover import mover
from Pas import pas

ncr=nacer()
apr=aparear()
czr=cazar()
mvr=mover()
pst=pas()

class conej:
    def __init__(self):
        self.ACn={}
        self.nombre='Conejo'
        self.hipo=10
        self.vmax=2880
        self.vmin=1440
        self.vminrep=120
        self.vmaxrep=1440
        self.dias_tick=30
        self.probapar=0
        self.probgest=0
        self.nminnac=3
        self.nmaxnac=12
        self.tiempoNuevaGesta=90
        self.tiempoGesta=30
        self.energiaXtick=10
        self.RA=10
        self.tick_s_comer_max=6
        
    def limpiar(self):
        self.ACn.clear()
    
    def evaluar(self,presa):
        L_A0=ncr.nacimiento(self.ACn, self.nombre, self.nminnac, self.nmaxnac, self.vmin, self.vmax)
        self.ACn=L_A0
        L_A1=apr.apareo(self.ACn, self.nombre,self.dias_tick, self.vminrep, self.vmaxrep, self.RA, self.probapar, self.probgest, self.tiempoGesta, self.tiempoNuevaGesta)
        self.ACn=L_A1
        L_A2,L_AP=czr.caza(self.ACn, presa, self.nombre, pst.nombre, self.RA)
        self.ACn=L_A2
        L_A3=mvr.movimineto(self.ACn, self.nombre, self.hipo, self.dias_tick, self.energiaXtick)
        self.ACn=L_A3
        return self.ACn, L_AP
    
        