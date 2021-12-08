# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:02:49 2021

@author: JAIR_PC_JAPA
"""

from Nacer import nacer
from Aparear import aparear
from Cazar import cazar
from Mover import mover
from Conej import conej
from Comad import comad

ncr=nacer()
apr=aparear()
czr=cazar()
mvr=mover()
cnj=conej()
cmd=comad()

class buh:
    def __init__(self):
        self.ABu={}
        self.nombre='Buho'
        self.hipo=15
        self.vmax=5400
        self.vmin=3600
        self.vminrep=720
        self.vmaxrep=2520
        self.dias_tick=30
        self.probapar=0.7
        self.probgest=0.7
        self.nminnac=1
        self.nmaxnac=6
        self.tiempoNuevaGesta=360
        self.tiempoGesta=30
        self.energiaXtick=1
        self.RA=15
        self.tick_s_comer_max=15
        
    def limpiar(self):
        self.ABu.clear()
        
    def evaluar(self,presa1,presa2):
        L_A0=ncr.nacimiento(self.ABu, self.nombre, self.nminnac, self.nmaxnac, self.vmin, self.vmax)
        self.ABu=L_A0
        L_A1=apr.apareo(self.ABu, self.nombre,self.dias_tick, self.vminrep, self.vmaxrep, self.RA-5, self.probapar, self.probgest, self.tiempoGesta, self.tiempoNuevaGesta)
        self.ABu=L_A1
        L_A2,L_AP_0=czr.caza(self.ABu, presa1, self.nombre, cnj.nombre, self.RA)
        self.ABu=L_A2
        L_A2,L_AP_1=czr.caza(self.ABu, presa2, self.nombre, cmd.nombre, self.RA)
        self.ABu=L_A2
        L_A3=mvr.movimineto(self.ABu, self.nombre, self.hipo, self.dias_tick, self.energiaXtick)
        self.ABu=L_A3
        return self.ABu,L_AP_0,L_AP_1