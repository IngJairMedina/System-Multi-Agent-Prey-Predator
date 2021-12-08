// JavaScript Document

function dibujar_circulo(x, y, color) {
  ctx.beginPath();
  ctx.arc(x, y, 4, 0, 2 * Math.PI);
  ctx.fillStyle = color;
  ctx.fill();
}

function dibujar_pasto(x, y, color) {
  ctx.beginPath();
  ctx.fillStyle = color;
  ctx.fillRect(x, y, 8, 8);
  ctx.fill();
}

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

window.onload = function () {
canvas = document.getElementById("cv1");
ctx = canvas.getContext("2d");
cangraf = document.getElementById("cv2");
const ctx1 = cangraf.getContext("2d");
var cb0 = document.getElementById("cbx0");
var cb1 = document.getElementById("cbx1");
var cb2 = document.getElementById("cbx2");
var cb3 = document.getElementById("cbx3");
var cb4 = document.getElementById("cbx4");
var cb5 = document.getElementById("cbx5");
var cb6 = document.getElementById("cbx6");
var nm0 = document.getElementById("nm0");
var nm1 = document.getElementById("nm1");
var nm2 = document.getElementById("nm2");
var nm3 = document.getElementById("nm3");
var nm4 = document.getElementById("nm4");
var nm5 = document.getElementById("nm5");
var nm6 = document.getElementById("nm6");
var nm7 = document.getElementById("nm7");
var nm10 = document.getElementById("nm10");
var nm11 = document.getElementById("nm11");
var nm12 = document.getElementById("nm12");
var nm13 = document.getElementById("nm13");
var nm14 = document.getElementById("nm14");
var nm15 = document.getElementById("nm15");
var nm16 = document.getElementById("nm16");
var nm17 = document.getElementById("nm17");
var nm18 = document.getElementById("nm18");
var conM = document.getElementById("conM");
var conH = document.getElementById("conH");
var lobM = document.getElementById("lobM");
var lobH = document.getElementById("lobH");
var halM = document.getElementById("halM");
var halH = document.getElementById("halH");
var serM = document.getElementById("serM");
var serH = document.getElementById("serH");
var jabM = document.getElementById("jabM");
var jabH = document.getElementById("jabH");
var buhM = document.getElementById("buhM");
var buhH = document.getElementById("buhH");
var zorM = document.getElementById("zorM");
var zorH = document.getElementById("zorH");
var comM = document.getElementById("comM");
var comH = document.getElementById("comH");
tic = document.getElementById("nm8");
nm9 = document.getElementById("nm9");
var T = document.getElementById("rg0");
var VRC = document.getElementById("rg1");
var VRL = document.getElementById("rg2");
var VRH = document.getElementById("rg3");
var VRS = document.getElementById("rg4");
var VRJ = document.getElementById("rg5");
var VRB = document.getElementById("rg6");
var VRZ = document.getElementById("rg7");
var VRCM = document.getElementById("rg8");
cargar = document.getElementById("btn0");
ejecutar = document.getElementById("btn1");
nm1.style.display = 'none';
nm2.style.display = 'none';
nm3.style.display = 'none';
nm4.style.display = 'none';
nm5.style.display = 'none';
nm6.style.display = 'none';
nm7.style.display = 'none';
VRL.style.display = 'none';
VRH.style.display = 'none';
VRS.style.display = 'none';
VRJ.style.display = 'none';
VRB.style.display = 'none';
VRZ.style.display = 'none';
VRCM.style.display = 'none';
lobM.style.display = 'none';
lobH.style.display = 'none';
halM.style.display = 'none';
halH.style.display = 'none';
serM.style.display = 'none';
serH.style.display = 'none';
jabM.style.display = 'none';
jabH.style.display = 'none';
buhM.style.display = 'none';
buhH.style.display = 'none';
zorM.style.display = 'none';
zorH.style.display = 'none';
comM.style.display = 'none';
comH.style.display = 'none';
conM.value = "#F8A6D5";
conH.value = "#94DBBD";
lobM.value = "#BDA5C5";
lobH.value = "#B5C9CB";
halM.value = "#AC788F";
halH.value = "#C38D4E";
serM.value = "#5B414C";
serH.value = "#41545B";
jabM.value = "#546184";
jabH.value = "#788454";
buhM.value = "#7A4257";
buhH.value = "#7A4F42";
zorM.value = "#AD55A8";
zorH.value = "#AD7F55";
comM.value = "#F6C325";
comH.value = "#A025F6";
  chart = grafica();

  function addval(a0, a1, a2, a3, a4, a5, a6, a7, ti, i) {
    chart.data.datasets[i].data.push(a0);
    chart.data.datasets[i + 1].data.push(a1);
    chart.data.datasets[i + 2].data.push(a2);
    chart.data.datasets[i + 3].data.push(a3);
    chart.data.datasets[i + 4].data.push(a4);
    chart.data.datasets[i + 5].data.push(a5);
    chart.data.datasets[i + 6].data.push(a6);
    chart.data.datasets[i + 7].data.push(a7);
    chart.data.labels.push(ti);
    chart.update('none');
  };

  function updateval(dato, i) {
    chart.data.datasets[i].data = [dato];
    chart.update('none');
  };

  function grafica() {
    var chart = new Chart(document.getElementById("cv2"), {
      type: 'line',
      data: {
        labels: [],
        datasets: [{
          label: 'Conejo',
          data: [],
          backgroundColor: 'rgba(176, 45, 40)',
          borderColor: 'rgba(176, 45, 40)',
          borderWidth: 1,
          radius: 2,
        }, {
          label: 'Lobo',
          data: [],
          backgroundColor: 'rgba(157, 176, 40)',
          borderColor: 'rgba(157, 176, 40)',
          borderWidth: 1,
          radius: 2,
        }, {
          label: 'Halcon',
          data: [],
          backgroundColor: 'rgba(67, 176, 40)',
          borderColor: 'rgba(67, 176, 40)',
          borderWidth: 1,
          radius: 2,
        }, {
          label: 'Serpiente',
          data: [],
          backgroundColor: 'rgba(40, 158, 176)',
          borderColor: 'rgba(40, 158, 176)',
          borderWidth: 1,
          radius: 2,
        }, {
          label: 'Jabali',
          data: [],
          backgroundColor: 'rgba(75, 40, 176)',
          borderColor: 'rgba(75, 40, 176)',
          borderWidth: 1,
          radius: 2,
        }, {
          label: 'Buho',
          data: [],
          backgroundColor: 'rgba(133, 40, 176)',
          borderColor: 'rgba(133, 40, 176)',
          borderWidth: 1,
          radius: 2,
        }, {
          label: 'Zorro',
          data: [],
          backgroundColor: 'rgba(176, 40, 151)',
          borderColor: 'rgba(176, 40, 151)',
          borderWidth: 1,
          radius: 2,
        }, {
          label: 'Comadreja',
          data: [],
          backgroundColor: 'rgba(233, 177, 5)',
          borderColor: 'rgba(233, 177, 5)',
          borderWidth: 1,
          radius: 2,
        }]
      },
      options: {
        responsive: false,
        plugins: {
          title: {
            display: true,
            text: 'POBLACIÓN'
          }
        },
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
    return chart
  };


  cb0.addEventListener('click', function () {
    if (cb0.checked) {
      nm1.style.display = 'block';
      lobH.style.display = 'block';
      lobM.style.display = 'block';
      VRL.style.display = 'block';
    } else {
      nm1.style.display = 'none';
      lobH.style.display = 'none';
      lobM.style.display = 'none';
      VRL.style.display = 'none';
    }
  });
  cb1.addEventListener('click', function () {
    if (cb1.checked) {
      nm2.style.display = 'block';
      halM.style.display = 'block';
      halH.style.display = 'block';
      VRH.style.display = 'block';
    } else {
      nm2.style.display = 'none';
      halM.style.display = 'none';
      halH.style.display = 'none';
      VRH.style.display = 'none';
    }
  });
  cb2.addEventListener('click', function () {
    if (cb2.checked) {
      nm3.style.display = 'block';
      serM.style.display = 'block';
      serH.style.display = 'block';
      VRS.style.display = 'block';
    } else {
      nm3.style.display = 'none';
      serM.style.display = 'none';
      serH.style.display = 'none';
      VRS.style.display = 'none';
    }
  });
  cb3.addEventListener('click', function () {
    if (cb3.checked) {
      nm4.style.display = 'block';
      jabM.style.display = 'block';
      jabH.style.display = 'block';
      VRJ.style.display = 'block';
    } else {
      nm4.style.display = 'none';
      jabM.style.display = 'none';
      jabH.style.display = 'none';
      VRJ.style.display = 'none';
    }
  });
  cb4.addEventListener('click', function () {
    if (cb4.checked) {
      nm5.style.display = 'block';
      buhM.style.display = 'block';
      buhH.style.display = 'block';
      VRB.style.display = 'block';
    } else {
      nm5.style.display = 'none';
      buhM.style.display = 'none';
      buhH.style.display = 'none';
      VRB.style.display = 'none';
    }
  });
  cb5.addEventListener('click', function () {
    if (cb5.checked) {
      nm6.style.display = 'block';
      zorM.style.display = 'block';
      zorH.style.display = 'block';
      VRZ.style.display = 'block';
    } else {
      nm6.style.display = 'none';
      zorM.style.display = 'none';
      zorH.style.display = 'none';
      VRZ.style.display = 'none';
    }
  });
  cb6.addEventListener('click', function () {
    if (cb6.checked) {
      nm7.style.display = 'block';
      comM.style.display = 'block';
      comH.style.display = 'block';
      VRCM.style.display = 'block';
    } else {
      nm7.style.display = 'none';
      comM.style.display = 'none';
      comH.style.display = 'none';
      VRCM.style.display = 'none';
    }
  });
	
  cargar.onclick = async function () {
    chart.clear();
    chart.destroy();
    chart = grafica();
    ticks = 200;

    var colorconM = conM.value;
    var colorconH = conH.value;
    var colorlobM = lobM.value;
    var colorlobH = lobH.value;
    var colorhalM = halM.value;
    var colorhalH = halH.value;
    var colorserM = serM.value;
    var colorserH = serH.value;
    var colorjabM = jabM.value;
    var colorjabH = jabH.value;
    var colorbuhM = buhM.value;
    var colorbuhH = buhH.value;
    var colorzorM = zorM.value;
    var colorzorH = zorH.value;
    var colorcomM = comM.value;
    var colorcomH = comH.value;
    var RC = VRC.value;
    var RL = VRL.value;
    var RH = VRH.value;
    var RS = VRS.value;
    var RJ = VRJ.value;
    var RB = VRB.value;
    var RZ = VRZ.value;
    var RCM = VRCM.value;
    
    if (nm0.value == '') {
      window.alert("Introduzca numero de conejos")
      return
    } else {
      var NC = nm0.value;
      NC1 = String(NC);
    };
    if (cb0.checked) {
      if (nm1.value == '') {
        window.alert("Introduzca numero de lobos")
        return
      } else {
        var NL = nm1.value;
      };
      NL1 = String(NL);
    } else {
      var NL = 0
      NL1 = String(NL);
    };
    if (cb1.checked) {
      if (nm2.value == '') {
        window.alert("Introduzca numero de halcones")
        return
      } else {
        var NH = nm2.value;
      };
      NH1 = String(NH);
    } else {
      var NH = 0
      NH1 = String(NH);
    };
    if (cb2.checked) {
      if (nm3.value == '') {
        window.alert("Introduzca numero de serpientes")
        return
      } else {
        var NS = nm3.value;
      };
      NS1 = String(NS);
    } else {
      var NS = 0
      NS1 = String(NS);
    };
    if (cb3.checked) {
      if (nm4.value == '') {
        window.alert("Introduzca numero de jabalis")
        return
      } else {
        var NJ = nm4.value;
      };
      NJ1 = String(NJ);
    } else {
      var NJ = 0
      NJ1 = String(NJ);
    };
    if (cb4.checked) {
      if (nm5.value == '') {
        window.alert("Introduzca numero de buhos")
        return
      } else {
        var NB = nm5.value;
      };
      NB1 = String(NB);
    } else {
      var NB = 0
      NB1 = String(NB);
    };
    if (cb5.checked) {
      if (nm6.value == '') {
        window.alert("Introduzca numero de zorros")
        return
      } else {
        var NZ = nm6.value;
      };
      NZ1 = String(NZ);
    } else {
      var NZ = 0
      NZ1 = String(NZ);
    };
    if (cb6.checked) {
      if (nm7.value == '') {
        window.alert("Introduzca numero de halcones")
        return
      } else {
        var NCo = nm7.value;
      };
      NCo1 = String(NCo);
    } else {
      var NCo = 0
      NCo1 = String(NCo);
    };
    i0 = 0;
    i1 = 0;
    i2 = 0;
    i3 = 0;
    i4 = 0;
    i5 = 0;
    i6 = 0;
    i7 = 0;
    i8 = 0;

    x = 0;
    y = 0;
    s = 0;
    var datos = {
      NC: NC1,
      NL: NL1,
      NH: NH1,
      NS: NS1,
      NJ: NJ1,
      NB: NB1,
      NZ: NZ1,
      NCo: NCo1,
      RC: RC,
      RL: RL,
      RH: RH,
      RS: RS,
      RJ: RJ,
      RB: RB,
      RZ: RZ,
      RCM: RCM,
    };
    var init = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(datos),
    };
    url = "/load";
    let response = await fetch(url, init);
    data = await response.json();

    cn = data.cn;
    pasto = data.pasto;
    lb = data.lb;
    cm = data.cm;
    jb = data.jb;
    sr = data.sr;
    zr = data.zr;
    bh = data.bh;
    hl = data.hl;

    let clc = Object.keys(cn);
    let clp = Object.keys(pasto);
    let cll = Object.keys(lb);
    let clcm = Object.keys(cm);
    let clj = Object.keys(jb);
    let cls = Object.keys(sr);
    let clz = Object.keys(zr);
    let clb = Object.keys(bh);
    let clh = Object.keys(hl);

    let vac = Object.values(cn);
    let vap = Object.values(pasto);
    let val = Object.values(lb);
    let vacm = Object.values(cm);
    let vaj = Object.values(jb);
    let vas = Object.values(sr);
    let vaz = Object.values(zr);
    let vab = Object.values(bh);
    let vah = Object.values(hl);

    vc = clc.length;
    vp = clp.length
    vl = cll.length;
    vcm = clcm.length;
    vj = clj.length;
    vs = cls.length;
    vz = clz.length;
    vb = clb.length;
    vh = clh.length;

    nm9.value = parseInt(vc, 10);
    nm10.value = parseInt(vl, 10);
    nm11.value = parseInt(vh, 10);
    nm12.value = parseInt(vs, 10);
    nm13.value = parseInt(vj, 10);
    nm14.value = parseInt(vb, 10);
    nm15.value = parseInt(vz, 10);
    nm16.value = parseInt(vcm, 10);
    nm17.value = parseInt(vp, 10);

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    while (i0 < clp.length) {
      v = vap[i0];
      x = v[0];
      y = v[1];
      dibujar_pasto(x, y, "#1A6C33");
      i0++;
    };

    while (i1 < clc.length) {
      v = vac[i1];
      x = v[0];
      y = v[1];
      s = v[2];
      if (s == 'H') {
        dibujar_circulo(x, y, colorconH);
      } else {
        dibujar_circulo(x, y, colorconM);
      }
      i1++;
    };

    while (i2 < cll.length) {
      v = val[i2];
      x = v[0];
      y = v[1];
      s = v[2];
      if (s == 'H') {
        dibujar_circulo(x, y, colorlobH);
      } else {
        dibujar_circulo(x, y, colorlobM);
      }
      i2++;
    };

    while (i3 < clh.length) {
      v = vah[i3];
      x = v[0];
      y = v[1];
      s = v[2];
      if (s == 'H') {
        dibujar_circulo(x, y, colorhalH);
      } else {
        dibujar_circulo(x, y, colorhalM);
      }
      i3++;
    };
    while (i4 < cls.length) {
      v = vas[i4];
      x = v[0];
      y = v[1];
      s = v[2];
      if (s == 'H') {
        dibujar_circulo(x, y, colorserH);
      } else {
        dibujar_circulo(x, y, colorserM);
      }
      i4++;
    };
    while (i5 < clj.length) {
      v = vaj[i5];
      x = v[0];
      y = v[1];
      s = v[2];
      if (s == 'H') {
        dibujar_circulo(x, y, colorjabH);
      } else {
        dibujar_circulo(x, y, colorjabM);
      }
      i5++;
    };
    while (i6 < clb.length) {
      v = vab[i6];
      x = v[0];
      y = v[1];
      s = v[2];
      if (s == 'H') {
        dibujar_circulo(x, y, colorbuhH);
      } else {
        dibujar_circulo(x, y, colorbuhM);
      }
      i6++;
    };
    while (i7 < clz.length) {
      v = vaz[i7];
      x = v[0];
      y = v[1];
      s = v[2];
      if (s == 'H') {
        dibujar_circulo(x, y, colorzorH);
      } else {
        dibujar_circulo(x, y, colorzorM);
      }
      i7++;
    };
    while (i8 < clcm.length) {
      v = vacm[i8];
      x = v[0];
      y = v[1];
      s = v[2];
      if (s == 'H') {
        dibujar_circulo(x, y, colorcomH);
      } else {
        dibujar_circulo(x, y, colorcomM);
      }
      i8++;
    };

    updateval(vc, 0);
    updateval(vl, 1);
    updateval(vh, 2);
    updateval(vs, 3);
    updateval(vj, 4);
    updateval(vb, 5);
    updateval(vz, 6);
    updateval(vcm, 7);
  };

  ejecutar.onclick = async function () {
    ticks = 0;
    chart.clear();
    chart.destroy();
    chart = grafica();
    var colorconM = conM.value;
    var colorconH = conH.value;
    var colorlobM = lobM.value;
    var colorlobH = lobH.value;
    var colorhalM = halM.value;
    var colorhalH = halH.value;
    var colorserM = serM.value;
    var colorserH = serH.value;
    var colorjabM = jabM.value;
    var colorjabH = jabH.value;
    var colorbuhM = buhM.value;
    var colorbuhH = buhH.value;
    var colorzorM = zorM.value;
    var colorzorH = zorH.value;
    var colorcomM = comM.value;
    var colorcomH = comH.value;
    if (nm18.value == '') {
      window.alert("Introduzca numero ticks a simular")
      return
    } else {
      var NTS = nm18.value;
    };
    while (ticks < NTS) {
      i0 = 0;
      i1 = 0;
      i2 = 0;
      i3 = 0;
      i4 = 0;
      i5 = 0;
      i6 = 0;
      i7 = 0;
      i8 = 0;

      x = 0;
      y = 0;
      s = 0;

      var init = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      };
      url = "/simular";
      let response = await fetch(url, init);
      data1 = await response.json();

      cn = data1.cn;
      pasto = data1.pasto;
      lb = data1.lb;
      cm = data1.cm;
     jb = data1.jb;
      sr = data1.sr;
      zr = data1.zr;
      bh = data1.bh;
      hl = data1.hl;
		console.log(pasto);

      clc = Object.keys(cn);
      clp = Object.keys(pasto);
      cll = Object.keys(lb);
      clcm = Object.keys(cm);
      clj = Object.keys(jb);
      cls = Object.keys(sr);
      clz = Object.keys(zr);
      clb = Object.keys(bh);
      clh = Object.keys(hl);
		console.log(clc);

      vac = Object.values(cn);
      vap = Object.values(pasto);
      val = Object.values(lb);
      vacm = Object.values(cm);
      vaj = Object.values(jb);
      vas = Object.values(sr);
      vaz = Object.values(zr);
      vab = Object.values(bh);
      vah = Object.values(hl);
		console.log(vac);

      vc = clc.length;
      vp = clp.length
      vl = cll.length;
      vcm = clcm.length;
      vj = clj.length;
      vs = cls.length;
      vz = clz.length;
      vb = clb.length;
      vh = clh.length;
		console.log(vc);


      nm9.value = parseInt(vc, 10);
      nm10.value = parseInt(vl, 10);
      nm11.value = parseInt(vh, 10);
      nm12.value = parseInt(vs, 10);
      nm13.value = parseInt(vj, 10);
      nm14.value = parseInt(vb, 10);
      nm15.value = parseInt(vz, 10);
      nm16.value = parseInt(vcm, 10);
      nm17.value = parseInt(vp, 10);

      tim = T.value;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      while (i0 < clp.length) {
        v = vap[i0];
        x = v[0];
        y = v[1];
        dibujar_pasto(x, y, "#1A6C33");
        i0++;
      };

      while (i1 < clc.length) {
        v = vac[i1];
        x = v[0];
        y = v[1];
        s = v[2];
        if (s == 'H') {
          dibujar_circulo(x, y, colorconH);
        } else {
          dibujar_circulo(x, y, colorconM);
        }
        i1++;
      };

      while (i2 < cll.length) {
        v = val[i2];
        x = v[0];
        y = v[1];
        s = v[2];
        if (s == 'H') {
          dibujar_circulo(x, y, colorlobH);
        } else {
          dibujar_circulo(x, y, colorlobM);
        }
        i2++;
      };

      while (i3 < clh.length) {
        v = vah[i3];
        x = v[0];
        y = v[1];
        s = v[2];
        if (s == 'H') {
          dibujar_circulo(x, y, colorhalH);
        } else {
          dibujar_circulo(x, y, colorhalM);
        }
        i3++;
      };
      while (i4 < cls.length) {
        v = vas[i4];
        x = v[0];
        y = v[1];
        s = v[2];
        if (s == 'H') {
          dibujar_circulo(x, y, colorserH);
        } else {
          dibujar_circulo(x, y, colorserM);
        }
        i4++;
      };
      while (i5 < clj.length) {
        v = vaj[i5];
        x = v[0];
        y = v[1];
        s = v[2];
        if (s == 'H') {
          dibujar_circulo(x, y, colorjabH);
        } else {
          dibujar_circulo(x, y, colorjabM);
        }
        i5++;
      };
      while (i6 < clb.length) {
        v = vab[i6];
        x = v[0];
        y = v[1];
        s = v[2];
        if (s == 'H') {
          dibujar_circulo(x, y, colorbuhH);
        } else {
          dibujar_circulo(x, y, colorbuhM);
        }
        i6++;
      };
      while (i7 < clz.length) {
        v = vaz[i7];
        x = v[0];
        y = v[1];
        s = v[2];
        if (s == 'H') {
          dibujar_circulo(x, y, colorzorH);
        } else {
          dibujar_circulo(x, y, colorzorM);
        }
        i7++;
      };
      while (i8 < clcm.length) {
        v = vacm[i8];
        x = v[0];
        y = v[1];
        s = v[2];
        if (s == 'H') {
          dibujar_circulo(x, y, colorcomH);
        } else {
          dibujar_circulo(x, y, colorcomM);
        }
        i8++;
      };
      addval(vc, vl, vh, vs, vj, vb, vz, vcm, ticks, 0);
      await delay(tim);
      ticks++;
		delete cn;
		delete pasto;
		delete lb;
		delete cm;
		delete jb;
		delete sr;
		delete zr;
		delete bh;
		delete hl;
		clc.splice(0,clc.length);
		clp.splice(0,clp.length);
		cll.splice(0,cll.length);
		clcm.splice(0,clcm.length);
		clj.splice(0,clj.length);
		cls.splice(0,cls.length);
		clz.splice(0,clz.length);
		clb.splice(0,clb.length);
		clh.splice(0,clh.length);
		
		vac.splice(0,vac.length);
		vap.splice(0,vap.length);
		val.splice(0,val.length);
		vacm.splice(0,vacm.length);
		vaj.splice(0,vaj.length);
		vas.splice(0,vas.length);
		vaz.splice(0,vaz.length);
		vab.splice(0,vab.length);
		vah.splice(0,vah.length);
		
		delete vc;
		delete vp;
		delete vl;
		delete vcm;
		delete vj;
		delete vs;
		delete vz;
		delete vb;
		delete vh;
		tic.value = ticks;
		
    }
  };
};
