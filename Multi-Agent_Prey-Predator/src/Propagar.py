# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:18:58 2021

@author: JAIR_PC_JAPA
"""
from numpy.random import default_rng
import random

rng = default_rng()

class propagar:
    def __init__(self):
        self.Agente={}
    def propagacion(self,LA,NA,propmax,propmin):
        agentes=0
        self.Agente.clear()
        self.Agente=LA
        p=rng.integers(propmin, propmax).item()
        kyp=self.Agente.keys()
        lkp=len(kyp)
        i=0
        while i < p:
            kp=self.Agente.keys()
            v=[0,0,False]
            x=random.randrange(6, 710,8)
            y=random.randrange(6, 470,8)
            if len(kp)>0:
                j=0
                while j < len(kp):
                    nomp=NA+str(j)
                    x1=self.Agente[nomp][0]
                    y1=self.Agente[nomp][1]
                    evp=self.Agente[nomp][2]
                    j+=1
                    if x==x1 and y==y1:
                        i-=1
                        p=p-1
                        v[0]=x1
                        v[1]=y1
                        v[2]=evp
                        self.Agente[nomp]=v
                        z=0
                        j=len(kp)+1
                    else:
                        z=1
                        
                if z>0:
                    v[0]=x
                    v[1]=y
                    v[2]=True
                    nombrep=NA+str(lkp+i)
                    self.Agente[nombrep]=v
            else:
                v[0]=x
                v[1]=y
                v[2]=True
                nombrep=NA+str(lkp+i)
                self.Agente[nombrep]=v
            i+=1
        agentes=self.Agente.copy()
        return agentes