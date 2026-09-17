# -*- coding: utf-8 -*-
import base64, html, os
OUT = "/home/user/B-rbara-/marina-evolution"
def b64(p):
    return base64.b64encode(open(p,'rb').read()).decode()
HDR = b64(OUT+"/assets/honey-header.png")
FTR = b64(OUT+"/assets/honey-footer.png")

# ---- conteudo: (titulo, duracao, [ (n, rotulo, descricao, [(tag,texto),...]) ] )
REELS = [
 ("REELS 01 \u2014 PATRIM\u00d4NIO N\u00c1UTICO PROTEGIDO", "Vertical", "at\u00e9 45s", [
  ("01","ABERTURA",
   "Imagens externas da Marina + jets e embarca\u00e7\u00f5es.",
   [("OFF:","\u201cSeu jet ou sua lancha \u00e9 muito mais do que uma embarca\u00e7\u00e3o. \u00c9 um patrim\u00f4nio.\u201d")]),
  ("02","ESTRUTURA",
   "Mostrar chegada da embarca\u00e7\u00e3o, acesso e estrutura da Marina.",
   [("OFF:","\u201cE para cuidar desse patrim\u00f4nio, voc\u00ea precisa de um lugar preparado para isso.\u201d")]),
  ("03","CUIDADOS E SEGURAN\u00c7A",
   "Mostrar detalhes da estrutura, armazenamento, limpeza, equipe e demais diferenciais dispon\u00edveis.",
   [("OFF:","\u201cNa Marina Evolution, sua embarca\u00e7\u00e3o conta com estrutura, tecnologia e seguran\u00e7a para estar sempre bem cuidada e pronta para o pr\u00f3ximo passeio.\u201d")]),
  ("04","FECHAMENTO",
   "Embarca\u00e7\u00e3o saindo da Marina + imagens da \u00e1gua.",
   [("OFF:","\u201cPorque quando sua embarca\u00e7\u00e3o est\u00e1 em boas m\u00e3os, voc\u00ea s\u00f3 precisa se preocupar com uma coisa: aproveitar a pr\u00f3xima aventura.\u201d"),
    ("TEXTO NA TELA:","MARINA EVOLUTION\nSeu porto seguro. \u2693\U0001F30A")]),
 ]),

 ("MARINA EVOLUTION | Sexta-feira, 17h42", "Horizontal", "at\u00e9 30s", [
  ("01","GANCHO",
   "Abre no p\u00f4r do sol visto da Ponte dos Macuxis, sobre o Rio Branco. Corta para o close em slow-mo do gelo caindo dentro da caixa t\u00e9rmica. Som real amplificado.",
   [("TEXTO:","Sexta-feira, 17h42.")]),
  ("02","A MARINA",
   "Estacionamento da Marina com as lanchas e os jets guardados. Equipe tirando o jet da vaga e descendo pela rampa.",
   [("OFF:","\u201cSem carreta. Sem fila. Sem preocupa\u00e7\u00f5es.\u201d")]),
  ("03","NA \u00c1GUA",
   "Cortes r\u00e1pidos: jet cortando a \u00e1gua, rastro branco no rio, imagem a\u00e9rea do Rio Branco no fim da tarde.",
   [("\u2014","Sem locu\u00e7\u00e3o. Trilha e som real de motor e vento.")]),
  ("04","FECHAMENTO",
   "P\u00f4r do sol. Caixa t\u00e9rmica aberta no deck do Campe\u00e3o Express, embarca\u00e7\u00f5es ancoradas ao fundo.",
   [("OFF:","\u201cSegunda-feira chega igual pra todo mundo. O s\u00e1bado, n\u00e3o.\u201d")]),
 ]),

 ("MARINA EVOLUTION | 3 Motivos para N\u00c3O Vir", "Vertical", "at\u00e9 35s", [
  ("01","GANCHO",
   "Ela andando pela Marina, falando direto na c\u00e2mera. C\u00e2mera acompanhando em movimento, passando pelo deck e pelas embarca\u00e7\u00f5es. Ritmo solto, energia alta.",
   [("ON:","\u201cTr\u00eas motivos pra voc\u00ea N\u00c3O vir pra Marina Evolution neste fim de semana.\u201d")]),
  ("02","MOTIVO 01",
   "Ela chega na beira do deck e aponta pro rio. Corta para o p\u00f4r do sol no Rio Branco.",
   [("ON:","\u201cUm: voc\u00ea vai amar o p\u00f4r do sol de Boa Vista daqui. Depois n\u00e3o vai querer ver de outro lugar nunca mais.\u201d")]),
  ("03","MOTIVO 02",
   "Ela passa pelo estacionamento das embarca\u00e7\u00f5es e encosta a m\u00e3o num jet. Corta para jet acelerando na \u00e1gua.",
   [("ON:","\u201cDois: voc\u00ea vai amar andar de jet. A\u00ed \u00e9 altas aventuras no Rio Branco todo fim de semana.\u201d")]),
  ("04","MOTIVO 03",
   "Ela no deck, com a equipe descendo a embarca\u00e7\u00e3o pela rampa atr\u00e1s dela.",
   [("ON:","\u201cE tr\u00eas: voc\u00ea vai amar chegar e j\u00e1 sair navegando, sem carreta e sem trabalho nenhum. Depois n\u00e3o tem volta.\u201d")]),
  ("05","FECHAMENTO",
   "Ela d\u00e1 de ombros, sorrindo, e senta no deck com o movimento normal da Marina atr\u00e1s.",
   [("ON:","\u201cT\u00e1 avisado. Se mesmo assim voc\u00ea quiser vir, a gente te espera no s\u00e1bado.\u201d"),
    ("TEXTO:","Marca aquele amigo que precisa ler isso")]),
 ]),

 ("MARINA EVOLUTION | O Ver\u00e3o de Roraima", "Vertical", "at\u00e9 30s", [
  ("01","GANCHO",
   "A Ponte dos Macuxis e o sol forte sobre o Rio Branco. O calor da cidade: asfalto quente, sombra curta, sol duro.",
   [("OFF:","\u201cBoa Vista, o calor de sempre.\u201d"),
    ("TEXTO:","38\u00b0")]),
  ("02","O RIO",
   "Jet cortando a \u00e1gua. Imagem a\u00e9rea do Rio Branco, com as praias come\u00e7ando a aparecer.",
   [("OFF:","\u201c\u00c9 o rio baixando, a praia aparecendo, o motor pegando.\u201d")]),
  ("03","AS PESSOAS",
   "Grupo rindo dentro da lancha, crian\u00e7a de colete, brinde no deck do Campe\u00e3o Express.",
   [("OFF:","\u201c\u00c9 todo mundo que voc\u00ea gosta no mesmo barco.\u201d")]),
  ("04","FECHAMENTO",
   "P\u00f4r do sol sobre o Rio Branco, embarca\u00e7\u00f5es ancoradas na Marina Evolution.",
   [("OFF:","\u201cO ver\u00e3o de Roraima \u00e9 aqui.\u201d"),
    ("TEXTO:","Marina Evolution")]),
 ]),
]

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

def page(titulo, orient, dur, cenas):
    rows = []
    for n, lbl, desc, falas in cenas:
        fal = "".join(
            '<div class="ln"><span class="tag">%s</span> %s</div>' % (html.escape(t), html.escape(x).replace('\n','<br>'))
            for t, x in falas)
        rows.append(
            '<tr><td class="n">%s</td>'
            '<td><span class="lbl">%s</span>%s</td>'
            '<td>%s</td></tr>' % (n, html.escape(lbl), html.escape(desc), fal))
    return """
<div class="page">
  <img class="hdr" src="data:image/png;base64,%s">
  <img class="ftr" src="data:image/png;base64,%s">
  <div class="body">
    <div class="t1">ROTEIRO DE</div>
    <div class="t2">GRAVAÇÃO</div>
    <div class="sub">%s</div>
    <div class="fmt"><b>Formato:</b> %s | %s | <b>Cliente:</b> Marina Evolution</div>
    <div class="chk">CHECKLIST GRAVAÇÃO</div>
    <div class="chki">Foto Capa | Off | Bastidores</div>
    <table>
      <colgroup><col class="c1"><col class="c2"><col class="c3"></colgroup>
      <tr><th>CENA</th><th>DESCRIÇÃO DA CENA</th><th>TEXTO | ON | OFF</th></tr>
      %s
    </table>
  </div>
</div>""" % (HDR, FTR, html.escape(titulo if titulo.startswith("REELS") else u"REELS \u2014 "+titulo), html.escape(orient), html.escape(dur), "\n      ".join(rows))

doc = "<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>" \
      "<title>Roteiro de Gravação — Marina Evolution</title><style>%s</style></head><body>%s</body></html>" % (
      CSS, "".join(page(*r) for r in REELS))
open(OUT+"/03-roteiros-marina-evolution.html","w",encoding="utf-8").write(doc)
print("html gerado:", len(doc), "bytes")
