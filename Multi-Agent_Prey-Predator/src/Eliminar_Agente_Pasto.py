# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:14:06 2021

@author: JAIR_PC_JAPA
"""

class eliminar_agente_pasto:
    def __init__(self):
        self.Agente={}
    def eliminar(self,LA,NA):
        agentes=0
        self.Agente.clear()
        self.Agente=LA
        kyp=self.Agente.keys()
        i=0
        j=0
        while i < (len(kyp)):
            j=i
            v=[0,0,False]
            nomp=NA+str(i)
            x=self.Agente[nomp][0]
            y=self.Agente[nomp][1]
            evp=self.Agente[nomp][2]
            if evp==False:
                while i<(len(kyp)):
                    nomp=NA+str(i)
                    nomp1=NA+str(i+1)
                    self.Agente[nomp]=self.Agente.get(nomp1)
                    i+=1
                    if i >(len(kyp)-1):
                        nomp1=NA+str(len(kyp)-1)
                        del self.Agente[nomp1]
                        kyp=self.Agente.keys()
            else:
                v[0]=x
                v[1]=y
                v[2]=evp
                self.Agente[nomp]=v
            i=j+1
        agentes=self.Agente.copy()
        return agentes