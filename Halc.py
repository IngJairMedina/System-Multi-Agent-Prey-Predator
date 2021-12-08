# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:03:56 2021

@author: JAIR_PC_JAPA
"""

from Nacer import nacer
from Aparear import aparear
from Cazar import cazar
from Mover import mover
from Conej import conej
from Comad import comad
from Serp import serp

ncr=nacer()
apr=aparear()
czr=cazar()
mvr=mover()
cnj=conej()
cmd=comad()
srp=serp()

class halc:
    def __init__(self):
        self.AHa={}
        self.nombre='Halcon'
        self.hipo=15
        self.vmax=5400
        self.vmin=3600
        self.vminrep=900
        self.vmaxrep=3600
        self.dias_tick=30
        self.probapar=0.7
        self.probgest=0.7
        self.nminnac=2
        self.nmaxnac=4
        self.tiempoNuevaGesta=360
        self.tiempoGesta=30
        self.energiaXtick=1
        self.RA=15
        self.tick_s_comer_max=12
        
    def limpiar(self):
        self.AHa.clear()
        
    def evaluar(self,presa1,presa2,presa3):
        L_A0=ncr.nacimiento(self.AHa, self.nombre, self.nminnac, self.nmaxnac, self.vmin, self.vmax)
        self.AHa=L_A0
        L_A1=apr.apareo(self.AHa, self.nombre,self.dias_tick, self.vminrep, self.vmaxrep, self.RA-5, self.probapar, self.probgest, self.tiempoGesta, self.tiempoNuevaGesta)
        self.AHa=L_A1
        L_A2,L_AP_0=czr.caza(self.AHa, presa1, self.nombre, cnj.nombre, self.RA)
        self.AHa=L_A2
        L_A2,L_AP_1=czr.caza(self.AHa, presa2, self.nombre, cmd.nombre, self.RA)
        self.AHa=L_A2
        L_A2,L_AP_2=czr.caza(self.AHa, presa3, self.nombre, srp.nombre, self.RA)
        self.AHa=L_A2
        L_A3=mvr.movimineto(self.AHa, self.nombre, self.hipo, self.dias_tick, self.energiaXtick)
        self.AHa=L_A3
        return self.AHa,L_AP_0,L_AP_1,L_AP_2