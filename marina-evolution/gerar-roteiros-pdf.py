# -*- coding: utf-8 -*-
import base64, html, os
OUT = "/home/user/B-rbara-/marina-evolution"
def b64(p):
    return base64.b64encode(open(p,'rb').read()).decode()
HDR = b64(OUT+"/assets/honey-header.png")
FTR = b64(OUT+"/assets/honey-footer.png")

# ---- conteudo: (titulo, duracao, [ (n, rotulo, descricao, [(tag,texto),...]) ] )
REELS = [
 ("MARINA EVOLUTION | A Chave", "até 50s", [
  ("01","GANCHO",
   "Close macro: a chave do jet cai em slow-mo na palma da mão aberta. Sol duro, fundo desfocado com o brilho da água. Som real, sem trilha.",
   [("OFF:","“Essa chave é a parte fácil.”")]),
  ("02","O PROBLEMA",
   "Quintal comum de Boa Vista: carreta parada, lona desbotada com folha seca, pneu murcho, ferrugem no engate. Câmera baixa, sol estourado.",
   [("OFF:","“Difícil é manter o que ela liga valendo o que você pagou. Sol de Boa Vista não perdoa gelcoat. Chuva de maio não pede licença. E carreta parada no quintal enferruja em silêncio.”"),
    ("TEXTO:","8 meses parada.")]),
  ("03","A VIRADA",
   "Travelling entrando na guarda: fileira de jets e lanchas alinhados e cobertos. Drone baixo passando por cima. A trilha abre.",
   [("OFF:","“Aqui ela não dorme no tempo. Dorme coberta, seca, na vaga dela.”"),
    ("TEXTO:","GUARDA COBERTA")]),
  ("04","A PROVA",
   "Oficina em três planos: ferramenta original apertando, tela de diagnóstico, técnico fechando a tampa do motor. Corta para a rampa, jet descendo pela equipe.",
   [("OFF:","“E acorda revisada por quem foi treinado pela fábrica. Concessionária autorizada BRP: Sea-Doo, Can-Am, Focker e Mercury. Peça original, ferramenta original, técnico certificado.”"),
    ("TEXTO:","CONCESSIONÁRIA AUTORIZADA BRP")]),
  ("05","FECHAMENTO",
   "Cliente chega, pega a chave no quadro. Corta: já está no jet, motor ligando. Drone abre revelando o Rio Branco.",
   [("OFF:","“Você chega e sai navegando. O resto é com a gente.”"),
    ("TEXTO:","A temporada abre em outubro. As vagas, não esperam ela abrir.")]),
 ]),

 ("MARINA EVOLUTION | Sexta, 17h42", "até 35s", [
  ("01","GANCHO",
   "Close extremo em slow-mo: gelo caindo dentro da caixa térmica. Gotas, vapor frio, luz lateral de fim de tarde. Som real amplificado, sem trilha.",
   [("TEXTO:","Sexta-feira. 17h42.")]),
  ("02","PREPARAÇÃO",
   "Cortes rápidos no tempo da batida, todos em close: colete saindo do gancho, protetor solar no ombro, óculos escuros descendo, chinelo batendo no chão, a chave girando no dedo.",
   [("—","Sem locução. Trilha e som real de cada corte.")]),
  ("03","CHEGADA",
   "Portão da Marina abrindo. Equipe descendo o jet pela rampa. Aperto de mão. Motor pegando — close na água saindo do escapamento.",
   [("TEXTO:","Sem carreta. Sem fila. Sem lavar depois.")]),
  ("04","ÁGUA",
   "Explosão de movimento: jet acelerando, rastro branco no Rio Branco, drone acompanhando de lado, respingo na lente, grupo passando junto e rindo. Sol baixo e dourado.",
   [("—","Trilha no auge, motor e vento.")]),
  ("05","FECHAMENTO",
   "Pôr do sol. Caixa térmica aberta no deck do Campeão Express, duas latas suando. Ao fundo, desfocadas, as embarcações e as pessoas conversando.",
   [("OFF:","“Segunda-feira chega igual pra todo mundo. O sábado, não.”")]),
 ]),

 ("MARINA EVOLUTION | 3 Motivos para NÃO Vir", "até 35s", [
  ("01","GANCHO",
   "Personagem em pé no deck, de costas para o rio, segurando três cartelas de papel. Câmera na mão, levemente instável — proposital.",
   [("ON:","“Três motivos pra você NÃO vir pra Marina Evolution neste fim de semana.”"),
    ("TEXTO:","3 motivos para NÃO vir")]),
  ("02","MOTIVO 01",
   "Cartela 1 na câmera. Atrás dele, jet passando. Na frase, corta para corredor de shopping / ar-condicionado pingando. Ele joga a cartela fora do quadro e o corte acontece no movimento.",
   [("ON:","“Um: você ama passar o sábado no shopping. No mesmo ar-condicionado de segunda a sexta.”")]),
  ("03","MOTIVO 02",
   "Cartela 2. B-roll sofrido: alguém suando pra engatar carreta, fila de carretas na rampa, mangueira lavando jet no escuro.",
   [("ON:","“Dois: pra você, engatar carreta, pegar fila na rampa e lavar o jet às seis da tarde... é lazer.”")]),
  ("04","MOTIVO 03",
   "Cartela 3. Na metade da frase a câmera gira dele para o pôr do sol no Rio Branco — o plano mais bonito do banco, 2 segundos inteiros sem corte.",
   [("ON:","“E três: você acha que pôr do sol no Rio Branco é exagero da internet.”")]),
  ("05","FECHAMENTO",
   "Ele sem cartela nenhuma, dá de ombros. Atrás, o movimento normal da marina.",
   [("ON:","“Se você não se identificou com nenhum... a gente te espera sábado.”"),
    ("TEXTO:","Marca aquele amigo que precisa ler isso")]),
 ]),

 ("MARINA EVOLUTION | O Verão Aqui é um Lugar", "até 30s", [
  ("01","GANCHO",
   "A cidade em setembro: asfalto tremendo de calor em teleobjetiva, sol duro, ventilador girando, sombra curta. Planos parados e pesados. Alguém mergulha e o respingo toma a tela.",
   [("OFF:","“Tem cidade onde o verão é uma estação.”"),
    ("TEXTO:","Boa Vista, 38°.")]),
  ("02","EXPLOSÃO",
   "Rajada de cortes de meio segundo: motor pegando, pé descalço no deck, corda sendo soltada, rastro branco na água, drone subindo do rio, respingo na lente.",
   [("OFF:","“Aqui, o verão é um lugar.”")]),
  ("03","AS PESSOAS",
   "Bloco humano, mais quente e mais lento: grupo rindo dentro da lancha, criança de colete sendo erguida, brinde no deck do Campeão Express, alguém puxando o outro pra dentro da água.",
   [("OFF:","“É o rio baixando, a praia aparecendo, o motor pegando.”")]),
  ("04","VELOCIDADE",
   "Bloco de adrenalina: jet cortando em curva fechada, lancha de frente abrindo água, drone alto revelando a frota em formação no Rio Branco, sol atravessando o respingo em contraluz.",
   [("OFF:","“E todo mundo que você gosta no mesmo barco.”")]),
  ("05","ASSINATURA",
   "Pôr do sol amplo sobre o Rio Branco, silhuetas das embarcações ancoradas na Marina. Plano fixo, longo, sem corte. Só ambiente.",
   [("OFF:","“Verão em Roraima é na água. E a água começa aqui.”")]),
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

def page(titulo, dur, cenas):
    rows = []
    for n, lbl, desc, falas in cenas:
        fal = "".join(
            '<div class="ln"><span class="tag">%s</span> %s</div>' % (html.escape(t), html.escape(x))
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
    <div class="sub">REELS — %s</div>
    <div class="fmt"><b>Formato:</b> Vertical | %s | <b>Cliente:</b> Marina Evolution</div>
    <div class="chk">CHECKLIST GRAVAÇÃO</div>
    <div class="chki">Foto Capa | Off | Bastidores</div>
    <table>
      <colgroup><col class="c1"><col class="c2"><col class="c3"></colgroup>
      <tr><th>CENA</th><th>DESCRIÇÃO DA CENA</th><th>TEXTO | ON | OFF</th></tr>
      %s
    </table>
  </div>
</div>""" % (HDR, FTR, html.escape(titulo), html.escape(dur), "\n      ".join(rows))

doc = "<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>" \
      "<title>Roteiro de Gravação — Marina Evolution</title><style>%s</style></head><body>%s</body></html>" % (
      CSS, "".join(page(*r) for r in REELS))
open(OUT+"/03-roteiros-marina-evolution.html","w",encoding="utf-8").write(doc)
print("html gerado:", len(doc), "bytes")
