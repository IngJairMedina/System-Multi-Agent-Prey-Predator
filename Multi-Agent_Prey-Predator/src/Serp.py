# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:03:52 2021

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

class serp:
    def __init__(self):
        self.ASr={}
        self.nombre='Serpiente'
        self.hipo=15
        self.vmax=3600
        self.vmin=2520
        self.vminrep=360
        self.vmaxrep=2520
        self.dias_tick=30
        self.probapar=0.7
        self.probgest=0.7
        self.nminnac=4
        self.nmaxnac=25
        self.tiempoNuevaGesta=360
        self.tiempoGesta=90
        self.energiaXtick=5
        self.RA=20
        self.tick_s_comer_max=12
        
    def limpiar(self):
        self.ASr.clear()
        
    def evaluar(self,presa1,presa2):
        L_A0=ncr.nacimiento(self.ASr, self.nombre, self.nminnac, self.nmaxnac, self.vmin, self.vmax)
        self.ASr=L_A0
        L_A1=apr.apareo(self.ASr, self.nombre,self.dias_tick, self.vminrep, self.vmaxrep, self.RA-10, self.probapar, self.probgest, self.tiempoGesta, self.tiempoNuevaGesta)
        self.ASr=L_A1
        L_A2,L_AP_0=czr.caza(self.ASr, presa1, self.nombre, cnj.nombre, self.RA)
        self.ASr=L_A2
        L_A2,L_AP_1=czr.caza(self.ASr, presa2, self.nombre, cmd.nombre, self.RA)
        self.ASr=L_A2
        L_A3=mvr.movimineto(self.ASr, self.nombre, self.hipo, self.dias_tick, self.energiaXtick)
        self.ASr=L_A3
        return self.ASr,L_AP_0,L_AP_1