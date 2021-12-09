# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:17:10 2021

@author: JAIR_PC_JAPA
"""
from numpy.random import default_rng
import math

rng = default_rng()

class mover:
    def __init__(self):
        self.Agente={}
    def movimineto(self,LA,NA,Paso,D_tick,En_tick):
        agentes=0
        self.Agente.clear()
        self.Agente=LA
        keysC=self.Agente.keys()
        for i in range(len(keysC)):
            #  X,Y,S,V,G,TNG
            v=[0,0,' ',0,0,0,0,0,False,False,0]
            nombrec=NA+str(i)
            xC=self.Agente[nombrec][0]
            yC=self.Agente[nombrec][1]
            sc=self.Agente[nombrec][2]
            vc=self.Agente[nombrec][3]
            gc=self.Agente[nombrec][4]
            tngc=self.Agente[nombrec][5]
            vmc=self.Agente[nombrec][6]
            ec=self.Agente[nombrec][7]
            eac=self.Agente[nombrec][8]
            evc=self.Agente[nombrec][9]
            dsc=self.Agente[nombrec][10]
            ang_der=rng.integers(0, 50).item()
            ang_izq=rng.integers(0, 50).item()
            teta=ang_der-ang_izq
            xC1=xC+(Paso*math.cos(teta))
            yC1=yC+(Paso*math.sin(teta))
            if xC1 > 710:
                xC1=710
            if xC1 < 10:
                xC1=10
            if yC1 > 470:
                yC1=470
            if yC1 < 10:
                yC1=10
            vc1=vc+D_tick
            ec=ec-En_tick
            v[0]=xC1
            v[1]=yC1
            v[2]=sc
            v[3]=vc1
            v[4]=gc
            v[5]=tngc
            v[6]=vmc
            v[7]=ec
            v[8]=eac
            v[9]=evc
            v[10]=dsc
            self.Agente[nombrec]=v
        agentes=self.Agente.copy()
        return agentes