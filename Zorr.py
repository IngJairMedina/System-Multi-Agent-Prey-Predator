# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:01:50 2021

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

class zorr:
    def __init__(self):
        self.AZo={}
        self.nombre='Zorro'
        self.hipo=15
        self.vmax=5040
        self.vmin=3600
        self.vminrep=360
        self.vmaxrep=2880
        self.dias_tick=30
        self.probapar=0.7
        self.probgest=0.7
        self.nminnac=3
        self.nmaxnac=8
        self.tiempoNuevaGesta=360
        self.tiempoGesta=90
        self.energiaXtick=1
        self.RA=10
        self.tick_s_comer_max=7
        
    def limpiar(self):
        self.AZo.clear()
        
    def evaluar(self,presa1,presa2):
        L_A0=ncr.nacimiento(self.AZo, self.nombre, self.nminnac, self.nmaxnac, self.vmin, self.vmax)
        self.AZo=L_A0
        L_A1=apr.apareo(self.AZo, self.nombre,self.dias_tick, self.vminrep, self.vmaxrep, self.RA, self.probapar, self.probgest, self.tiempoGesta, self.tiempoNuevaGesta)
        self.AZo=L_A1
        L_A2,L_AP_0=czr.caza(self.AZo, presa1, self.nombre, cnj.nombre, self.RA)
        self.AZo=L_A2
        L_A2,L_AP_1=czr.caza(self.AZo, presa2, self.nombre, cmd.nombre, self.RA)
        self.AZo=L_A2
        L_A3=mvr.movimineto(self.AZo, self.nombre, self.hipo, self.dias_tick, self.energiaXtick)
        self.AZo=L_A3
        return self.AZo,L_AP_0,L_AP_1