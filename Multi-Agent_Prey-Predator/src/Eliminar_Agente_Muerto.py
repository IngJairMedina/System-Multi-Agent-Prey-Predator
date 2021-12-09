# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:30:04 2021

@author: JAIR_PC_JAPA
"""

class eliminar_agente_muerto:
    def __init__(self):
        self.Agente={}
    def eliminar(self,LA,NA,dscmax):
        agentes=0
        self.Agente.clear()
        self.Agente=LA
        keysC=self.Agente.keys()
        i=0
        j=0
        while i < (len(keysC)):
            j=i
            #  X,Y,S,V,G,TNG
            v=[0,0,' ',0,0,0,0,0,False,False,0]
            """atributos de conejo n"""
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
            if vc>=vmc or ec<=0 or evc==False or dsc==dscmax:
                while i < (len(keysC)):#Recorrer nombres
                    nombrec=NA+str(i) 
                    nombrec1=NA+str(i+1)
                    self.Agente[nombrec]=self.Agente.get(nombrec1)
                    i+=1
                    if i>(len(keysC)-1):
                        nombrec1=NA+str(len(keysC)-1)
                        del self.Agente[nombrec1]
                        keysC=self.Agente.keys()
            else:
                v[0]=cxc
                v[1]=cyc
                v[2]=sc
                v[3]=vc
                v[4]=gc
                v[5]=tngc
                v[6]=vmc
                v[7]=ec
                v[8]=eac
                v[9]=evc
                v[10]=dsc
                self.Agente[nombrec]=v
            i=j+1
        agentes=self.Agente.copy()
        
        return agentes