# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:00:21 2021

@author: JAIR_PC_JAPA
"""
import numpy as np

class cazar:
    def __init__(self):
        self.Agentei={}
        self.Agentej={}
        
    def caza(self,Adep,Apres,NAD,NAP,RadAcc):
        agentes1=0
        agentes2=0
        self.Agentei.clear()
        self.Agentej.clear()
        self.Agentei=Adep
        self.Agentej=Apres
        keysC=self.Agentei.keys()
        j1=0
        i=0
        
        while i < (len(keysC)):
            #  X,Y,S,V,G,TNG
            v=[0,0,' ',0,0,0,0,0,False,False,0]
            nombrec= NAD+str(i)
            cxc=self.Agentei[nombrec][0]
            cyc=self.Agentei[nombrec][1]
            sc=self.Agentei[nombrec][2]
            vc=self.Agentei[nombrec][3]
            gc=self.Agentei[nombrec][4]
            tngc=self.Agentei[nombrec][5]
            vmc=self.Agentei[nombrec][6]
            ec=self.Agentei[nombrec][7]
            eac=self.Agentei[nombrec][8]
            evc=self.Agentei[nombrec][9]
            dsc=self.Agentei[nombrec][10]
            keysP=self.Agentej.keys()
            j=0
            if NAP=='Pasto':
                while j < (len(keysP)):
                    v1=[0,0,False]
                    nombrep=NAP+str(j)
                    xa1=self.Agentej[nombrep][0]
                    ya1=self.Agentej[nombrep][1]
                    evp=self.Agentej[nombrep][2]
                    cercania=np.sqrt((xa1-cxc)**2+(ya1-cyc)**2)
                    if cercania<=RadAcc+80:
                        ec=ec+5
                        evp=False
                        v1[0]=xa1
                        v1[1]=ya1
                        v1[2]=evp
                        self.Agentej[nombrep]=v1
                        j=len(keysP)
                        j1=1
                    else:
                        vc=vc
                        v1[0]=xa1
                        v1[1]=ya1
                        v1[2]=evp
                        self.Agentej[nombrep]=v1
                        j1=0
                    j=j+1
            else:
                while j < (len(keysP)):
                    v1=[0,0,' ',0,0,0,0,0,False,False,0]
                    nombrep=NAP+str(j)
                    xa1=self.Agentej[nombrep][0]
                    ya1=self.Agentej[nombrep][1]
                    sa1=self.Agentej[nombrep][2]
                    va1=self.Agentej[nombrep][3]
                    ga1=self.Agentej[nombrep][4]
                    tnga1=self.Agentej[nombrep][5]
                    vma1=self.Agentej[nombrep][6]
                    ea1=self.Agentej[nombrep][7]
                    eac1=self.Agentej[nombrep][8]
                    evc1=self.Agentej[nombrep][9]
                    dsc1=self.Agentej[nombrep][10]
                    cercania=np.sqrt((xa1-cxc)**2+(ya1-cyc)**2)
                    if cercania<=RadAcc:
                        ec=ec+5
                        evc1=False
                        v1[0]=xa1
                        v1[1]=ya1
                        v1[2]=sa1
                        v1[3]=va1
                        v1[4]=ga1
                        v1[5]=tnga1
                        v1[6]=vma1
                        v1[7]=ea1
                        v1[8]=eac1
                        v1[9]=evc1
                        v1[10]=dsc1
                        self.Agentej[nombrep]=v1
                        j=len(keysP)
                        j1=1
                    else:
                        vc=vc
                        v1[0]=xa1
                        v1[1]=ya1
                        v1[2]=sa1
                        v1[3]=va1
                        v1[4]=ga1
                        v1[5]=tnga1
                        v1[6]=vma1
                        v1[7]=ea1
                        v1[8]=eac1
                        v1[9]=evc1
                        v1[10]=dsc1
                        self.Agentej[nombrep]=v1
                        j1=0
                    j=j+1
            
            if j1==0:
                dsc=dsc+1
                j1=0
            else:
                dsc=0
                j1=0
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
            self.Agentei[nombrec]=v
            i+=1
        agentes1=self.Agentei.copy()
        agentes2=self.Agentej.copy()
        return agentes1,agentes2