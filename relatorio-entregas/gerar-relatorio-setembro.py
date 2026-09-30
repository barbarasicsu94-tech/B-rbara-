# -*- coding: utf-8 -*-
"""Relatorio de entregas de conteudo da Honey Films — setembro/2026.

Gera o HTML na identidade Honey (cabecalho e rodape graficos, laranja
#FF7502, roxo #42067E) com indicadores, grafico de status por cliente,
contratado x postado, pendencias com justificativa e o detalhamento de
cada item. O PDF sai do HTML com o Chromium headless.
"""
import html, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from honey_template import HDR, FTR

LARANJA, ROXO = "#FF7502", "#42067E"

# status: (rotulo, cor da marca, cor do texto dentro da barra)
STATUS = {
    "post": (u"Postado", ROXO, "#fff"),
    "pron": (u"Pronto, não postado", "#A77BDB", "#1a1a1a"),
    "edic": (u"Em edição", LARANJA, "#1a1a1a"),
    "capt": (u"Captação agendada", "#B5B5B5", "#1a1a1a"),
}
ORDEM = ["post", "pron", "edic", "capt"]

# item: (nome, status, veio de agosto, quantidade)
def it(nome, st="post", ago=False, qtd=1):
    return (nome, st, ago, qtd)

CLIENTES = [
 (u"BV Locadora", u"04 cards | 04 reels", [
   it(u"Card 01 – Lago do Robertinho"), it(u"Card 02 – Independência"),
   it(u"Card 03 – Mormaço"), it(u"Card 04 – Dia do cliente"),
   it(u"Card 05 – Motion"), it(u"Card 06 – Frota atualizada"),
   it(u"Reels 01 – Feriado"), it(u"Reels 02 – Facilidade"),
   it(u"Reels 03 – 03 motivos")]),
 (u"Visual Tintas", u"02 cards | 05 reels | 10 encartes", [
   it(u"10 encartes de produtos", qtd=10),
   it(u"Card 01 – Carrossel verniz"), it(u"Card 02 – Dia do cliente"),
   it(u"Card 03 – Laranja", ago=True),
   it(u"Reels 01 – Campanha do mês"), it(u"Reels 02 – Faça você mesmo"),
   it(u"Reels 03 – Dicas verão"), it(u"Reels 04 – Todo mundo (…)"),
   it(u"Reels 05 – Balde de água")]),
 (u"Cambará", u"01 VT | 15 cards | 04 reels", [
   it(u"VT – Campanha"),
   it(u"Cards 01 a 08", qtd=8), it(u"Card 09 – Madeira"), it(u"Card 10 – Cimento"),
   it(u"Card 11 – Carrossel Dia C"), it(u"Card 12 – Tráfego"), it(u"Card 13 – Tráfego"),
   it(u"Card 14 – Saldão"), it(u"Card 15 – Template saldão"),
   it(u"Reels – Dia do cliente"), it(u"Reels 01 – Jeitinho"),
   it(u"Reels 02 – Jingle", "edic"),
   it(u"Reels 03 – Depoimento de cliente", "capt"),
   it(u"Reels 04 – Localização", "edic"),
   it(u"Reels 05", ago=True)]),
 (u"Evolution · PWS", u"Grupo Evolution: 10 cards | 10 reels", [
   it(u"Card 01 – Trend"), it(u"Card 02 – Verão mormaço"), it(u"Card 03 – UTV"),
   it(u"Card 04 – Qual a sua vibe"), it(u"Card 05 – Independência"),
   it(u"Card 06 – Dia do cliente"),
   it(u"Reels 01 – Oferta UTV"), it(u"Reels 02 – Oferta moto aquática"),
   it(u"Reels 03 – Aniversário de Roraima", "edic"),
   it(u"Reels 04 – TBT Ana Paula"),
   it(u"Reels 05 – POV: mundo", ago=True), it(u"Reels 06 – Transformes", ago=True)]),
 (u"Evolution · Marina", u"Grupo Evolution: 10 cards | 10 reels", [
   it(u"Card 01 – Verão"), it(u"Card 02 – Final de semana"), it(u"Card 03 – Planos"),
   it(u"Card 04 – Catamarã"), it(u"Card 05 – POV", ago=True), it(u"Card 06 – Pescaria"),
   it(u"Reels 01 – Final de semana", "pron"),
   it(u"Reels 02 – Patrimônio"),
   it(u"Reels 03 – Catamarã", "capt"), it(u"Reels 04 – 03 motivos", "capt"),
   it(u"Reels 05 – Verão", ago=True), it(u"Reels 06 – Churrasco", ago=True),
   it(u"Reels 07 – Sexta-feira", "pron", ago=True)]),
 (u"Campeão Express", u"02 cards | 02 reels", [
   it(u"Card 01 – Mini carrossel"), it(u"Card 02 – Localização"),
   it(u"Reels 01 – a definir", "capt"), it(u"Reels 02 – a definir", "capt")]),
]

# (cliente, item, status, motivo, previsao)
PENDENCIAS = [
 (u"Cambará", u"Reels 02 – Jingle", "edic",
  u"Material captado; em fase de edição.", u"Em edição"),
 (u"Cambará", u"Reels 04 – Localização", "edic",
  u"Material captado; em fase de edição.", u"Em edição"),
 (u"Cambará", u"Reels 03 – Depoimento de cliente", "capt",
  u"Captação remarcada a pedido do cliente, no café.", u"Captação 03/10"),
 (u"Evolution · PWS", u"Reels 03 – Aniversário de Roraima", "edic",
  u"Em finalização na edição.", u"Pronto 01/10"),
 (u"Evolution · Marina", u"Reels 01 – Final de semana", "pron",
  u"Pronto e enviado; aguardando aprovação do cliente.", u"Posta após aprovação"),
 (u"Evolution · Marina", u"Reels 07 – Sexta-feira (agosto)", "pron",
  u"Pronto; um detalhe pendente antes do envio ao cliente.", u"Envio após ajuste"),
 (u"Evolution · Marina", u"Reels 03 – Catamarã", "capt",
  u"Captação agendada.", u"Captação 01/10"),
 (u"Evolution · Marina", u"Reels 04 – 03 motivos", "capt",
  u"Captação agendada.", u"Captação 01/10"),
 (u"Campeão Express", u"Reels 01 e 02", "capt",
  u"Captação agendada na Marina Evolution.", u"Captação 01/10"),
]

# (cliente, formato, contratado, postado set, postado pendencia ago, em andamento)
CONTRATO = [
 (u"BV Locadora", u"Cards", "4", "6", u"—", u"—"),
 (u"", u"Reels", "4", "3", u"—", u"—"),
 (u"Visual Tintas", u"Encartes", "10", "10", u"—", u"—"),
 (u"", u"Cards", "2", "2", "1", u"—"),
 (u"", u"Reels", "5", "5", u"—", u"—"),
 (u"Cambará", u"VT", "1", "1", u"—", u"—"),
 (u"", u"Cards", "15", "15", u"—", u"—"),
 (u"", u"Reels", "4", "2", "1", u"3 (2 em edição, 1 captação 03/10)"),
 (u"Grupo Evolution (PWS + Marina)", u"Cards", "10", "11", "1", u"—"),
 (u"", u"Reels", "10", "4", "4", u"5 (1 em edição, 2 prontos, 2 captação 01/10)"),
 (u"Campeão Express", u"Cards", "2", "2", u"—", u"—"),
 (u"", u"Reels", "2", "0", u"—", u"2 (captação 01/10)"),
]

def e(s):
    return html.escape(s)

def contar(itens):
    c = dict.fromkeys(ORDEM, 0)
    for _, st, _, q in itens:
        c[st] += q
    return c

TOT = dict.fromkeys(ORDEM, 0)
for _, _, itens in CLIENTES:
    for k, v in contar(itens).items():
        TOT[k] += v
TOTAL = sum(TOT.values())
AGOSTO = sum(q for _, _, itens in CLIENTES for _, _, a, q in itens if a)

def grafico():
    W, LBL, X0, X1 = 495, 104, 104, 392
    ROW, BAR, TOP = 30, 15, 6
    MAX = 22
    esc = (X1 - X0) / float(MAX)
    out = []
    for i, (nome, _, itens) in enumerate(CLIENTES):
        c = contar(itens)
        tot = sum(c.values())
        y = TOP + i * ROW
        out.append('<text x="0" y="%.1f" class="gl">%s</text>' % (y + BAR * 0.72, e(nome)))
        x = X0
        for k in ORDEM:
            n = c[k]
            if not n:
                continue
            w = n * esc
            _, cor, ink = STATUS[k]
            out.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="2" fill="%s"/>'
                       % (x, y, w - 1.5, BAR, cor))
            if w >= 11:
                out.append('<text x="%.1f" y="%.1f" class="gv" fill="%s">%d</text>'
                           % (x + (w - 1.5) / 2, y + BAR * 0.72, ink, n))
            x += w
        pct = 100.0 * c["post"] / tot
        out.append('<text x="%d" y="%.1f" class="gr"><tspan class="gb">%d%%</tspan> '
                   '· %d de %d postados</text>' % (X1 + 8, y + BAR * 0.72, round(pct), c["post"], tot))
    h = TOP + len(CLIENTES) * ROW
    for v in range(0, MAX + 1, 5):
        xv = X0 + v * esc
        out.insert(0, '<line x1="%.1f" x2="%.1f" y1="0" y2="%d" class="gg"/>' % (xv, xv, h - 10))
        out.append('<text x="%.1f" y="%d" class="ga">%d</text>' % (xv, h + 2, v))
    return ('<svg class="graf" viewBox="0 0 %d %d" role="img" aria-label="Status das entregas por cliente">%s</svg>'
            % (W, h + 6, "".join(out)))

def legenda():
    return "".join('<span class="lg"><i style="background:%s"></i>%s</span>'
                   % (STATUS[k][1], e(STATUS[k][0])) for k in ORDEM)

def selo(st):
    rot, cor, ink = STATUS[st]
    return '<span class="selo" style="background:%s;color:%s">%s</span>' % (cor, ink, e(rot))

CSS = """
@page { size: 210mm 297mm; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:"Liberation Sans",Arial,Helvetica,sans-serif; color:#1a1a1a;
       -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { position:relative; width:595.44pt; height:841.68pt; overflow:hidden;
        page-break-after:always; background:#fff; }
.page:last-child { page-break-after:auto; }
.hdr { position:absolute; left:1.10pt; top:0.65pt; width:596.75pt; height:170.85pt; }
.ftr { position:absolute; left:1.33pt; bottom:0.58pt; width:593.22pt; height:143.40pt; }
.cab { position:absolute; left:50pt; top:66pt; width:420pt; }
.t1 { font-size:11pt; letter-spacing:.5pt; }
.t2 { font-size:22pt; font-weight:bold; color:#FF7502; margin-top:2pt; }
.t3 { font-size:9.5pt; color:#42067E; font-weight:bold; margin-top:5pt; }
.corpo { position:absolute; left:50pt; top:172pt; width:495pt; }
.rod { position:absolute; left:50pt; right:50pt; bottom:26pt; font-size:7.5pt; color:#6b6b6b;
       display:flex; justify-content:space-between; }
h2 { font-size:11pt; color:#42067E; margin:0 0 7pt; text-transform:uppercase; letter-spacing:.4pt; }
h2 small { font-size:8pt; color:#6b6b6b; text-transform:none; letter-spacing:0; font-weight:normal; }
.sec { margin-bottom:16pt; }
.kpis { display:flex; gap:8pt; }
.kpi { flex:1; border:0.6pt solid #d9d9d9; border-top:3pt solid #42067E; border-radius:3pt; padding:8pt 9pt 9pt; }
.kpi.l { border-top-color:#FF7502; }
.kpi .n { font-size:24pt; font-weight:bold; color:#1a1a1a; line-height:1; }
.kpi .n small { font-size:11pt; color:#42067E; margin-left:3pt; }
.kpi .r { font-size:8.5pt; font-weight:bold; margin-top:4pt; }
.kpi .d { font-size:7.5pt; color:#6b6b6b; margin-top:2pt; line-height:1.3; }
.lgs { display:flex; gap:14pt; font-size:8pt; margin-bottom:8pt; color:#3a3a3a; }
.lg i { display:inline-block; width:8pt; height:8pt; border-radius:2pt; margin-right:4pt; vertical-align:-1pt; }
.graf { width:495pt; display:block; }
.gl { font-size:9.2px; font-weight:bold; fill:#1a1a1a; }
.gv { font-size:8px; font-weight:bold; text-anchor:middle; }
.gr { font-size:8px; fill:#3a3a3a; }
.gb { font-weight:bold; fill:#1a1a1a; }
.ga { font-size:7px; fill:#8a8a8a; text-anchor:middle; }
.gg { stroke:#ececec; stroke-width:.6; }
.nota { font-size:7.8pt; color:#6b6b6b; margin-top:6pt; line-height:1.4; }
.resumo { font-size:9pt; line-height:1.5; }
.resumo b { color:#42067E; }
table { width:100%; border-collapse:collapse; font-size:7.9pt; }
td.cli[rowspan] { vertical-align:top; padding-top:4pt; width:92pt; }
th { background:#42067E; color:#fff; font-weight:bold; text-align:left; padding:3.5pt 6pt; font-size:7.6pt; }
td { border-bottom:0.5pt solid #dcdcdc; padding:2.6pt 6pt; vertical-align:middle; line-height:1.3; }
td.c, th.c { text-align:center; }
td.cli { font-weight:bold; }
tr.grp td { border-top:0.9pt solid #bdbdbd; }
.extra { color:#FF7502; font-weight:bold; }
.selo { display:inline-block; font-size:7pt; font-weight:bold; padding:1.5pt 5pt; border-radius:6pt; white-space:nowrap; }
.prev { font-weight:bold; color:#42067E; white-space:nowrap; }
.grade { display:grid; grid-template-columns:1fr 1fr; gap:12pt 18pt; }
.bl h3 { font-size:9.5pt; color:#FF7502; border-bottom:0.8pt solid #FF7502; padding-bottom:2pt; margin-bottom:3pt;
         display:flex; justify-content:space-between; align-items:baseline; }
.bl h3 small { font-size:7pt; color:#6b6b6b; font-weight:normal; }
.li { font-size:7.8pt; line-height:1.45; display:flex; align-items:center; }
.li i { width:6.5pt; height:6.5pt; border-radius:50%; margin-right:5pt; flex:none; }
.li em { font-style:normal; color:#8a8a8a; margin-left:4pt; font-size:7pt; }
.li .s { margin-left:auto; font-size:7pt; color:#6b6b6b; padding-left:6pt; }
"""

def cabecalho(sub):
    return ('<img class="hdr" src="data:image/png;base64,%s"><img class="ftr" src="data:image/png;base64,%s">'
            '<div class="cab"><div class="t1">RELATÓRIO DE ENTREGAS DE CONTEÚDO</div>'
            '<div class="t2">SETEMBRO 2026</div><div class="t3">%s</div></div>' % (HDR, FTR, e(sub)))

def rodape(n):
    return ('<div class="rod"><span>Honey Films Produtora · Relatório de entregas · Setembro 2026</span>'
            '<span>Atualizado em 30/09/2026 · %d/3</span></div>' % n)

def pagina1():
    p = TOT["post"]
    and_ = TOT["pron"] + TOT["edic"]
    kpis = (
      '<div class="kpi"><div class="n">%d</div><div class="r">itens na demanda</div>'
      '<div class="d">cards, reels, VT e encartes de 6 clientes, incluindo %d itens de agosto</div></div>'
      '<div class="kpi"><div class="n">%d<small>%d%%</small></div><div class="r">postados</div>'
      '<div class="d">entregues e publicados até 30/09</div></div>'
      '<div class="kpi l"><div class="n">%d</div><div class="r">em andamento</div>'
      '<div class="d">%d em edição e %d prontos aguardando aprovação ou ajuste</div></div>'
      '<div class="kpi l"><div class="n">%d</div><div class="r">captações agendadas</div>'
      '<div class="d">4 em 01/10 (Marina Evolution e Campeão) e 1 em 03/10 (Cambará)</div></div>'
      % (TOTAL, AGOSTO, p, round(100.0 * p / TOTAL), and_, TOT["edic"], TOT["pron"], TOT["capt"]))
    return ('<div class="page">%s<div class="corpo">'
      '<div class="sec"><h2>Visão geral</h2><div class="kpis">%s</div></div>'
      '<div class="sec"><h2>Status das entregas por cliente <small>· quantidade de itens</small></h2>'
      '<div class="lgs">%s</div>%s'
      '<div class="nota">Visual Tintas inclui 10 encartes de produto; Cambará inclui 8 cards entregues em lote (01 a 08). '
      'Itens de agosto finalizados ou pendentes em setembro entram na conta de cada cliente.</div></div>'
      '<div class="sec"><h2>Resumo</h2><div class="resumo">'
      '<b>BV Locadora</b>, <b>Visual Tintas</b> e <b>Campeão Express (cards)</b> estão com tudo o que foi produzido já postado; '
      'a BV Locadora recebeu 2 cards além do pacote. '
      'As pendências estão concentradas em <b>reels</b> e todas têm motivo e data: '
      '3 em edição, 2 prontos aguardando aprovação ou ajuste e 5 captações agendadas para 01/10 e 03/10. '
      'O detalhamento está nas páginas seguintes.</div></div>'
      '</div>%s</div>' % (cabecalho(u"Análise de postagens por cliente"), kpis, legenda(), grafico(), rodape(1)))

def pagina2():
    lin = []
    for i, (cli, fmt, ctr, pst, ago, anda) in enumerate(CONTRATO):
        extra = ' <span class="extra">+%d</span>' % (int(pst) - int(ctr)) if int(pst) > int(ctr) else ""
        cel = ""
        if cli:
            span = 1
            while i + span < len(CONTRATO) and not CONTRATO[i + span][0]:
                span += 1
            cel = '<td class="cli" rowspan="%d">%s</td>' % (span, e(cli))
        lin.append('<tr%s>%s<td>%s</td><td class="c">%s</td><td class="c">%s%s</td>'
                   '<td class="c">%s</td><td>%s</td></tr>'
                   % (' class="grp"' if cli else "", cel, e(fmt), ctr, pst, extra, ago, e(anda)))
    pend = "".join('<tr><td class="cli">%s</td><td>%s</td><td>%s</td><td>%s</td><td class="prev">%s</td></tr>'
                   % (e(c), e(i), selo(s), e(m), e(p)) for c, i, s, m, p in PENDENCIAS)
    return ('<div class="page">%s<div class="corpo">'
      '<div class="sec"><h2>Contratado x postado</h2><table>'
      '<tr><th>Cliente</th><th>Formato</th><th class="c">Contratado</th><th class="c">Postado em setembro</th>'
      '<th class="c">Pendência de agosto postada</th><th>Em andamento</th></tr>%s</table>'
      '<div class="nota">Em laranja, entregas além do pacote contratado. O pacote do Grupo Evolution é compartilhado entre PWS e Marina. '
      'O pacote da Campeão Express considera a demanda do mês.</div></div>'
      '<div class="sec"><h2>Pendências e justificativas</h2><table>'
      '<tr><th>Cliente</th><th>Item</th><th>Status</th><th>Motivo</th><th>Previsão</th></tr>%s</table></div>'
      '</div>%s</div>' % (cabecalho(u"Contratado x postado e pendências"), "".join(lin), pend, rodape(2)))

def pagina3():
    blocos = []
    for nome, pacote, itens in CLIENTES:
        c = contar(itens)
        li = "".join('<div class="li"><i style="background:%s"></i>%s%s<span class="s">%s</span></div>'
                     % (STATUS[st][1], e(n), '<em>(agosto)</em>' if a else "", e(STATUS[st][0]))
                     for n, st, a, q in itens)
        blocos.append('<div class="bl"><h3>%s<small>%s</small></h3>%s</div>' % (e(nome), e(pacote), li))
    return ('<div class="page">%s<div class="corpo">'
      '<div class="sec"><h2>Detalhamento por cliente</h2><div class="lgs">%s</div><div class="grade">%s</div></div>'
      '</div>%s</div>' % (cabecalho(u"Lista de postagens de setembro"), legenda(), "".join(blocos), rodape(3)))

saida = os.path.join(AQUI, "relatorio-entregas-setembro.html")
doc = (u"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>"
       u"<title>Relatório de Entregas — Setembro 2026</title><style>%s</style></head><body>%s%s%s</body></html>"
       % (CSS, pagina1(), pagina2(), pagina3()))
with open(saida, "w", encoding="utf-8") as f:
    f.write(doc)
print("html gerado:", saida, "| total", TOTAL, TOT, "| agosto", AGOSTO)
