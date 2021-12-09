# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:13:39 2021

@author: JAIR_PC_JAPA
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:10:24 2021

@author: JAIR_PC_JAPA
"""
from Crear import crear
from Eliminar_Agente_Muerto import eliminar_agente_muerto
from Eliminar_Agente_Pasto import eliminar_agente_pasto
from Pas import pas
from Conej import conej
from Lob import lob
from Comad import comad
from Jaba import jaba
from Serp import serp
from Zorr import zorr
from Buh import buh
from Halc import halc

cr=crear()
eam=eliminar_agente_muerto()
eap=eliminar_agente_pasto()
pst=pas()
cnj=conej()
lb=lob()
cmd=comad()
ja=jaba()
srp=serp()
zr=zorr()
bh=buh()
hlc=halc()

class prin:
    def __init__(self):
        self.listaconejos={}
        
    def crear_agente(self,NC,NL,NCo,NJ,NS,NZ,NB,NH,RC1,RL1,RH1,RS1,RJ1,RB1,RZ1,RCM1):
        pst.limpiar()
        Agente_pas=cr.cr_Agnts(0, 0, 0,pst.nombre)
        pst.APt=Agente_pas
        cnj.limpiar()
        Agente_con=cr.cr_Agnts(NC, cnj.vmin, cnj.vmax,cnj.nombre)
        cnj.probapar=RC1
        cnj.probgest=RC1
        cnj.ACn=Agente_con
        lb.limpiar()
        Agente_lob=cr.cr_Agnts(NL, lb.vmin, lb.vmax, lb.nombre)
        lb.probapar=RL1
        lb.probgest=RL1
        lb.ALb=Agente_lob
        cmd.limpiar()
        Agente_com=cr.cr_Agnts(NCo, cmd.vmin, cmd.vmax, cmd.nombre)
        cmd.probapar=RCM1
        cmd.probgest=RCM1
        cmd.ACm=Agente_com
        ja.limpiar()
        Agente_jab=cr.cr_Agnts(NJ, ja.vmin, ja.vmax, ja.nombre)
        ja.probapar=RJ1
        ja.probgest=RJ1
        ja.AJb=Agente_jab
        srp.limpiar()
        Agente_serp=cr.cr_Agnts(NS, srp.vmin, srp.vmax,srp.nombre)
        srp.probapar=RS1
        srp.probgest=RS1
        srp.ASr=Agente_serp
        zr.limpiar()
        Agente_zor=cr.cr_Agnts(NZ, zr.vmin, zr.vmax, zr.nombre)
        zr.probapar=RZ1
        zr.probgest=RZ1
        zr.AZo=Agente_zor
        bh.limpiar()
        Agente_buh=cr.cr_Agnts(NB, bh.vmin, bh.vmax, bh.nombre)
        bh.probapar=RB1
        bh.probgest=RB1
        bh.ABu=Agente_buh
        hlc.limpiar()
        Agente_hal=cr.cr_Agnts(NH, hlc.vmin, hlc.vmax, hlc.nombre)
        hlc.probapar=RH1
        hlc.probgest=RH1
        hlc.AHa=Agente_hal
        return cnj.ACn,pst.APt,lb.ALb,cmd.ACm,ja.AJb,srp.ASr,zr.AZo,bh.ABu,hlc.AHa
        
    def evaluar_agente(self,LC,LP,LL,LCm,LJ,LS,LZ,LB,LH):
        cnj.ACn=LC
        pst.APt=LP
        lb.ALb=LL
        cmd.ACm=LCm
        ja.AJb=LJ
        srp.ASr=LS
        zr.AZo=LZ
        bh.ABu=LB
        hlc.AHa=LH
        Agente_pas=eap.eliminar(pst.APt, pst.nombre)
        pst.APt=Agente_pas
        Agente_con=eam.eliminar(cnj.ACn, cnj.nombre,cnj.tick_s_comer_max)
        cnj.ACn=Agente_con
        Agente_lob=eam.eliminar(lb.ALb, lb.nombre,lb.tick_s_comer_max)
        lb.ALb=Agente_lob
        Agente_com=eam.eliminar(cmd.ACm, cmd.nombre,cmd.tick_s_comer_max)
        cmd.ACm=Agente_com
        Agente_jab=eam.eliminar(ja.AJb, ja.nombre,ja.tick_s_comer_max)
        ja.AJb=Agente_jab
        Agente_serp=eam.eliminar(srp.ASr, srp.nombre,srp.tick_s_comer_max)
        srp.ASr=Agente_serp
        Agente_zor=eam.eliminar(zr.AZo, zr.nombre,zr.tick_s_comer_max)
        zr.AZo=Agente_zor
        Agente_buh=eam.eliminar(bh.ABu, bh.nombre,bh.tick_s_comer_max)
        bh.ABu=Agente_buh
        Agente_hal=eam.eliminar(hlc.AHa, hlc.nombre,hlc.tick_s_comer_max)
        hlc.AHa=Agente_hal
        
        Agente_con, AP0=cnj.evaluar(pst.APt)
        cnj.ACn=Agente_con
        pst.APt=AP0
        
        Agente_lob,AP1,AP2=lb.evaluar(cnj.ACn,ja.AJb)
        lb.ALb=Agente_lob
        cnj.ACn=AP1
        ja.AJb=AP2
        
        Agente_com,AP3=cmd.evaluar(cnj.ACn)
        cmd.ACm=Agente_com
        cnj.ACn=AP3
        
        Agente_jab,AP4=ja.evaluar(cnj.ACn)
        ja.AJb=Agente_jab
        cnj.ACn=AP4
        
        Agente_serp,AP5,AP6=srp.evaluar(cnj.ACn,cmd.ACm)
        srp.ASr=Agente_serp
        cnj.ACn=AP5
        cmd.ACm=AP6
        
        Agente_zor,AP7,AP8=zr.evaluar(cnj.ACn,cmd.ACm)
        zr.AZo=Agente_zor
        cnj.ACn=AP7
        cmd.ACm=AP8
        
        Agente_buh,AP9,AP10=bh.evaluar(cnj.ACn,cmd.ACm)
        bh.ABu=Agente_buh
        cnj.ACn=AP9
        cmd.ACm=AP10
        
        Agente_hal,AP11,AP12,AP13=hlc.evaluar(cnj.ACn,cmd.ACm,srp.ASr)
        hlc.AHa=Agente_hal
        cnj.ACn=AP11
        cmd.ACm=AP12
        srp.ASr=AP13
        
        Agente_pas=pst.evaluar()
        pst.APt=Agente_pas
        
        return cnj.ACn,pst.APt,lb.ALb,cmd.ACm,ja.AJb,srp.ASr,zr.AZo,bh.ABu,hlc.AHa
        
        