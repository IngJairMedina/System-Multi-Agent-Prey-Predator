# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:06:13 2021

@author: JAIR_PC_JAPA
"""
from numpy.random import default_rng
import random

rng = default_rng()

class crear:
    def __init__(self):
        self.Agente={}
    def cr_Agnts(self,NA,vmin,vmax,tA):
        agentes=0
        self.Agente.clear()
        if tA=='Pasto':
            p=rng.integers(100, 300).item()
            i=0
            while i < p:
                kp=self.Agente.keys()
                v=[0,0,False]
                x=random.randrange(6, 710,8)
                y=random.randrange(6, 470,8)
                if len(kp)>0:
                    j=0
                    while j < len(kp):
                        nomp=tA+str(j)
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
                        nombrep=tA+str(i)
                        self.Agente[nombrep]=v
                        
                else:
                    v[0]=x
                    v[1]=y
                    v[2]=True
                    nombrep=tA+str(i)
                    self.Agente[nombrep]=v
                    
                i+=1
            agentes=self.Agente.copy()
        else:
            for i in range(NA):
                #  X,Y,S,V,G,TNG,vmax
                v=[0,0,' ',0,0,0,0,0,False,False,0]
                px=rng.integers(10, 710).item()
                py=rng.integers(10, 470).item()
                v[0]=px
                v[1]=py
                if rng.random()>.5:
                    v[2]='M'
                else:
                    v[2]='H'
                v[3]=60
                v[4]=0
                v[5]=0
                v[6]=rng.integers(vmin, vmax).item()
                v[7]=100
                v[8]=False
                v[9]=True
                v[10]=0
                nombrec=tA+str(i)
                self.Agente[nombrec]=v
            agentes=self.Agente.copy()
        return agentes