# -*- coding: utf-8 -*-
import base64, html, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import HDR, FTR, CSS

RAIZ = os.path.dirname(os.path.abspath(__file__))

def b64(nome):
    with open(os.path.join(RAIZ, "assets", nome), "rb") as f:
        return base64.b64encode(f.read()).decode()

EXTRA = """
.fotos { margin:22pt 0 0 49.92pt; width:496.56pt; display:flex; gap:16pt;
         align-items:flex-start; justify-content:center; }
.foto img { display:block; height:250pt; width:auto; border:0.6pt solid #A6A6A6; }
.foto p { margin-top:5pt; font-size:8.4pt; font-weight:bold; color:#FF7502; text-align:center; }
"""

PAGINA = u"""<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>
<title>Direcionamento de Fotos — Tropical</title><style>%s%s</style></head><body>
<div class="page">
  <img class="hdr" src="data:image/png;base64,%s">
  <img class="ftr" src="data:image/png;base64,%s">
  <div class="body">
    <div class="t1">DIRECIONAMENTO DE</div>
    <div class="t2">FOTOS</div>
    <div class="sub">VENDEDORES E MODELOS | TROPICAL</div>
    <div class="fmt"><b>Formato:</b> Fotos para cards | <b>Cliente:</b> Tropical</div>

    <div class="fotos">
      <div class="foto"><img src="data:image/jpeg;base64,%s"><p>REFERÊNCIA 1</p></div>
      <div class="foto"><img src="data:image/jpeg;base64,%s"><p>REFERÊNCIA 2</p></div>
    </div>

    <div class="btit">OBJETIVO</div>
    <div class="btxt">Pessoa em foco e showroom desfocado atrás, com os carros
    reconhecíveis mas sem competir com o rosto. Olhar sempre na câmera, sorriso leve
    e natural. Luz clara, sem sombra dura no rosto. Enquadramento da cintura para cima,
    sobrando ar acima da cabeça.</div>

    <div class="btit">DUAS POSES POR VENDEDOR</div>
    <div class="btxt">Uma em pé, como a referência 2, e uma sentado à mesa, como a
    referência 1. Assim o card tem opção na hora da arte.</div>
  </div>
</div></body></html>""" % (CSS, EXTRA, HDR, FTR, b64("ref-sentado.jpg"), b64("ref-em-pe.jpg"))

saida = os.path.join(RAIZ, "direcionamento-fotos.html")
with open(saida, "w", encoding="utf-8") as f:
    f.write(PAGINA)
print("html gerado:", saida, len(PAGINA), "bytes")
