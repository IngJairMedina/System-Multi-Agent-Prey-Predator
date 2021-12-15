# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:27:02 2021

@author: JAIR_PC_JAPA
"""
from numpy.random import default_rng
rng = default_rng()

class nacer:
    def __init__(self):
        self.Agente={}
        
    def nacimiento(self,LA,NA,MiN,MaN,Vmin,Vmax):
        agentes=0
        self.Agente.clear()
        self.Agente=LA
        keysC=self.Agente.keys()
        kc=len(keysC)
        for i in range(len(keysC)): #conejo n
            kyC=self.Agente.keys()
            kc=len(kyC)
            #  X,Y,S,V,G,TNG
            v1=[0,0,' ',0,0,0,0,0,False,False,0]
            """atributos de agente i"""
            nombrec=NA+str(i) 
            cxc=self.Agente[nombrec][0]
            cyc=self.Agente[nombrec][1]
            sc=self.Agente[nombrec][2]
            vc=self.Agente[nombrec][3]
            gc=self.Agente[nombrec][4]
            tngc=self.Agente[nombrec][5]
            vmc=self.Agente[nombrec][6]
            ec=self.Agente[nombrec][7]
            eac=self.Agente[nombrec][8]
            evc=self.Agente[nombrec][9]
            dsc=self.Agente[nombrec][10]
            if gc>0:
                gc=gc-30
                if gc<0:
                    gc==0
                if gc==0:
                    eac=False
                    nacC=rng.integers(MiN, MaN).item()
                    for j in range(nacC):
                        #   X,Y,'S',V,G,TNG
                        v=[0,0,' ',0,0,0,0,0,False,False,0]
                        """atributos de nuevo agente"""
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
                        v[6]=rng.integers(Vmin, Vmax).item()
                        v[7]=ec
                        v[8]=False
                        v[9]=True
                        v[10]=0
                        nombrec1=NA+str(kc+j)
                        self.Agente[nombrec1]=v
                v1[0]=cxc
                v1[1]=cyc
                v1[2]=sc
                v1[3]=vc
                v1[4]=gc
                v1[5]=tngc
                v1[6]=vmc
                v1[7]=ec
                v1[8]=eac
                v1[9]=evc
                v1[10]=dsc
                self.Agente[nombrec]=v1
        agentes=self.Agente.copy()
        return agentes