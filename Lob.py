# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:54:19 2021

@author: JAIR_PC_JAPA
"""
from Nacer import nacer
from Aparear import aparear
from Cazar import cazar
from Mover import mover
from Conej import conej
from Jaba import jaba

ncr=nacer()
apr=aparear()
czr=cazar()
mvr=mover()
cnj=conej()
jbl=jaba()

class lob:
    def __init__(self):
        self.ALb={}
        self.nombre='Lobo'
        self.hipo=15
        self.vmax=5400
        self.vmin=3960
        self.vminrep=720
        self.vmaxrep=4380
        self.dias_tick=30
        self.probapar=0.7
        self.probgest=0.7
        self.nminnac=4
        self.nmaxnac=7
        self.tiempoNuevaGesta=360
        self.tiempoGesta=90
        self.energiaXtick=1
        self.RA=25
        self.tick_s_comer_max=15
        
    def limpiar(self):
        self.ALb.clear()
        
    def evaluar(self,presa1,presa2):
        L_A0=ncr.nacimiento(self.ALb, self.nombre, self.nminnac, self.nmaxnac, self.vmin, self.vmax)
        self.ALb=L_A0
        L_A1=apr.apareo(self.ALb, self.nombre,self.dias_tick, self.vminrep, self.vmaxrep, self.RA-15, self.probapar, self.probgest, self.tiempoGesta, self.tiempoNuevaGesta)
        self.ALb=L_A1
        L_A2,L_AP_0=czr.caza(self.ALb, presa1, self.nombre, cnj.nombre, self.RA)
        self.ALb=L_A2
        L_A2,L_AP_1=czr.caza(self.ALb, presa2, self.nombre, jbl.nombre, self.RA)
        self.ALb=L_A2
        L_A3=mvr.movimineto(self.ALb, self.nombre, self.hipo, self.dias_tick, self.energiaXtick)
        self.ALb=L_A3
        return self.ALb,L_AP_0,L_AP_1