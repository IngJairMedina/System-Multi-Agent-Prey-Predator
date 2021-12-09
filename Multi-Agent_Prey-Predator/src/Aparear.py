# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:46:17 2021

@author: JAIR_PC_JAPA
"""

from numpy.random import default_rng
import numpy as np
rng = default_rng()

class aparear:
    def __init__(self):
        self.Agente={}
    
    def apareo(self,LA,NA,Dtick,VMiRep,VMaRep,RadAcc,ProbApar,probGest,TGesta,TnuGest):
        agentes=0
        self.Agente.clear()
        self.Agente=LA
        keysC=self.Agente.keys()
        for i in range(len(keysC)): #conejo n
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
            tngc=tngc-Dtick
            if tngc<0:
                tngc=0
            if eac==False and tngc==0 and VMiRep<vc<VMaRep:
                while i < (len(keysC)-1):#verificar cercania conejo n con todos
                    #  X,Y,S,V,G,TNG
                    v1=[0,0,' ',0,0,0,0,0,False,False,0]
                    """atributos de conejo n+1"""
                    nombrec1=NA+str(i+1)
                    cxc1=self.Agente[nombrec1][0]
                    cyc1=self.Agente[nombrec1][1]
                    sc1=self.Agente[nombrec1][2]
                    vc1=self.Agente[nombrec1][3]
                    gc1=self.Agente[nombrec1][4]
                    tngc1=self.Agente[nombrec1][5]
                    vmc1=self.Agente[nombrec1][6]
                    ec1=self.Agente[nombrec1][7]
                    eac1=self.Agente[nombrec1][8]
                    evc1=self.Agente[nombrec1][9]
                    dsc1=self.Agente[nombrec1][10]
                    cercania=np.sqrt((cxc1-cxc)**2+(cyc1-cyc)**2)
                    i+=1
                    tngc1=tngc1-Dtick
                    if tngc1<0:
                        tngc1=0
                    if eac1==False and tngc1==0 and VMiRep<vc1<VMaRep and cercania<=(RadAcc-5) and sc!=sc1 and rng.random()<ProbApar and rng.random()<probGest:#cercania en x
                            if sc=='H':
                                gc=TGesta
                                tngc=TnuGest
                                eac=True
                            else:
                                eac1=True
                    """"Guardar nuevos atributos a conejos comparados"""""
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
                    v1[0]=cxc1
                    v1[1]=cyc1
                    v1[2]=sc1
                    v1[3]=vc1
                    v1[4]=gc1
                    v1[5]=tngc1
                    v1[6]=vmc1
                    v1[7]=ec1
                    v1[8]=eac1
                    v1[9]=evc1
                    v1[10]=dsc1
                    self.Agente[nombrec1]=v1
            else:
                if eac==True and gc==0 and tngc==0:
                    gc=TGesta
                    tngc=TnuGest
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
        agentes=self.Agente.copy()
        return agentes