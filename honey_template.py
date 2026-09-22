# -*- coding: utf-8 -*-
"""Template Honey Films de roteiro de gravacao.

Reproduz o layout do PDF de referencia: pagina A4 (595,44 x 841,68 pt),
cabecalho e rodape graficos da Honey Films, titulo em duas linhas e
grade de tres colunas (CENA | DESCRICAO DA CENA | TEXTO | ON | OFF) com
bordas de 0,48pt em #A6A6A6.

Uma cena e uma tupla (numero, rotulo, descricao, [(marcacao, texto), ...]).
Rotulo vazio some; '\\n' vira quebra de linha na descricao e nos textos.
"""
import base64, html, os

RAIZ = os.path.dirname(os.path.abspath(__file__))

def _b64(nome):
    with open(os.path.join(RAIZ, "assets", nome), "rb") as f:
        return base64.b64encode(f.read()).decode()

HDR = _b64("honey-header.png")
FTR = _b64("honey-footer.png")

CSS = """
@page { size: 210mm 297mm; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:"Liberation Sans",Arial,Helvetica,sans-serif; color:#000;
       -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { position:relative; width:595.44pt; height:841.68pt; overflow:hidden;
        page-break-after:always; background:#fff; }
.page:last-child { page-break-after:auto; }
.hdr { position:absolute; left:1.10pt; top:0.65pt; width:596.75pt; height:170.85pt; }
.ftr { position:absolute; left:1.33pt; bottom:0.58pt; width:593.22pt; height:143.40pt; }
.body { position:absolute; left:0; top:171pt; width:595.44pt; }
.t1 { text-align:center; font-size:11.04pt; color:#000; }
.t2 { text-align:center; font-size:12pt; font-weight:bold; color:#FF7502; margin-top:3pt; }
.sub { margin:19pt 0 0 72.02pt; font-size:9.96pt; font-weight:bold; color:#42067E; }
.fmt { margin:3.5pt 0 0 72.02pt; font-size:9.96pt; color:#000; }
.fmt b { font-weight:bold; }
.chk { margin:16pt 0 0 72.02pt; font-size:9.96pt; font-weight:bold; color:#42067E; }
.chki{ margin:3.5pt 0 0 108pt; font-size:9.96pt; color:#42067E; }
table { margin:16pt 0 0 49.92pt; width:496.56pt; border-collapse:collapse; table-layout:fixed; }
col.c1 { width:49.46pt; } col.c2 { width:177.39pt; } col.c3 { width:269.71pt; }
th,td { border:0.48pt solid #A6A6A6; vertical-align:middle; padding:4pt 5.1pt; }
th { font-size:11.04pt; font-weight:bold; text-align:center; height:23.2pt; padding:2pt 5.1pt; }
td { font-size:9.2pt; line-height:1.30; }
td.n { text-align:center; font-size:11.04pt; }
.lbl { font-weight:bold; color:#FF7502; font-size:10.2pt; display:block; margin-bottom:2.5pt; }
.tag { font-weight:bold; color:#FF0000; }
.ln  { margin-bottom:3pt; }
.ln:last-child { margin-bottom:0; }
"""

def _txt(s):
    return html.escape(s).replace("\n", "<br>")

def pagina(titulo, formato, cliente, cenas):
    linhas = []
    for n, lbl, desc, falas in cenas:
        fal = "".join('<div class="ln"><span class="tag">%s</span> %s</div>'
                      % (_txt(t), _txt(x)) for t, x in falas)
        rot = '<span class="lbl">%s</span>' % _txt(lbl) if lbl else ""
        linhas.append('<tr><td class="n">%s</td><td>%s%s</td><td>%s</td></tr>'
                      % (n, rot, _txt(desc), fal))
    return """
<div class="page">
  <img class="hdr" src="data:image/png;base64,%s">
  <img class="ftr" src="data:image/png;base64,%s">
  <div class="body">
    <div class="t1">ROTEIRO DE</div>
    <div class="t2">GRAVAÇÃO</div>
    <div class="sub">%s</div>
    <div class="fmt"><b>Formato:</b> %s | <b>Cliente:</b> %s</div>
    <div class="chk">CHECKLIST GRAVAÇÃO</div>
    <div class="chki">Foto Capa | Off | Bastidores</div>
    <table>
      <colgroup><col class="c1"><col class="c2"><col class="c3"></colgroup>
      <tr><th>CENA</th><th>DESCRIÇÃO DA CENA</th><th>TEXTO | ON | OFF</th></tr>
      %s
    </table>
  </div>
</div>""" % (HDR, FTR, _txt(titulo), _txt(formato), _txt(cliente),
             "\n      ".join(linhas))

def montar(paginas, titulo_doc, saida):
    doc = ("<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>"
           "<title>%s</title><style>%s</style></head><body>%s</body></html>"
           % (html.escape(titulo_doc), CSS, "".join(pagina(*p) for p in paginas)))
    with open(saida, "w", encoding="utf-8") as f:
        f.write(doc)
    print("html gerado:", saida, len(doc), "bytes")
