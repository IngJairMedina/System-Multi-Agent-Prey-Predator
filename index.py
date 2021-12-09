# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:11:28 2021

@author: JAIR_PC_JAPA
"""

from flask import Flask,render_template, request
from flask.json import jsonify
from Prin import prin

app= Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
pr=prin()

@app.route('/', methods=['POST','GET'])
def home():
    return render_template("main.html")

@app.route('/load', methods=['POST','GET'])
def cargar():
    if request.method=='POST':
        request_data = request.get_json()
        NC=request_data.get('NC')
        NL=request_data.get('NL')
        NCo=request_data.get('NCo')
        NJ=request_data.get('NJ')
        NS=request_data.get('NS')
        NZ=request_data.get('NZ')
        NB=request_data.get('NB')
        NH=request_data.get('NH')
        RC=request_data.get('RC')
        RL=request_data.get('RL')
        RH=request_data.get('RH')
        RS=request_data.get('RS')
        RJ=request_data.get('RJ')
        RB=request_data.get('RB')
        RZ=request_data.get('RZ')
        RCM=request_data.get('RCM')
        NC1=int(NC)
        NL1=int(NL)
        NCo1=int(NCo)
        NJ1=int(NJ)
        NS1=int(NS)
        NZ1=int(NZ)
        NB1=int(NB)
        NH1=int(NH)
        RC1=float(RC)
        RL1=float(RL)
        RH1=float(RH)
        RS1=float(RS)
        RJ1=float(RJ)
        RB1=float(RB)
        RZ1=float(RZ)
        RCM1=float(RCM)
        cn,pasto,lb,cm,jb,sr,zr,bh,hl=pr.crear_agente(NC1,NL1,NCo1,NJ1,NS1,NZ1,NB1,NH1,RC1,RL1,RH1,RS1,RJ1,RB1,RZ1,RCM1)
    return jsonify({"cn":cn,"pasto":pasto,"lb":lb,"cm":cm,"jb":jb,"sr":sr,"zr":zr,"bh":bh,"hl":hl})

@app.route('/simular', methods=['POST','GET'])
def movi():
    if request.method=='POST':
        request_data = request.get_json()
        LC=request_data.get('cn')
        LP=request_data.get('pasto')
        LL=request_data.get('lb')
        LCm=request_data.get('cm')
        LJ=request_data.get('jb')
        LS=request_data.get('sr')
        LZ=request_data.get('zr')
        LB=request_data.get('bh')
        LH=request_data.get('hl')
        ticks=request_data.get('ticks')
        NTS=request_data.get('NTS')
        cn,pasto,lb,cm,jb,sr,zr,bh,hl=pr.evaluar_agente(LC,LP,LL,LCm,LJ,LS,LZ,LB,LH)
    return jsonify({"cn":cn,"pasto":pasto,"lb":lb,"cm":cm,"jb":jb,"sr":sr,"zr":zr,"bh":bh,"hl":hl,"ticks":ticks,"NTS":NTS})

if __name__ == "__main__":
    app.run(debug=True)