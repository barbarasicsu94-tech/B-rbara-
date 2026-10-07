# -*- coding: utf-8 -*-
"""Storyboard na identidade Honey Films.

Mesma pagina A4 e os mesmos graficos de cabecalho e rodape do roteiro.
Os quadros sao 9:16, desenhados em SVG tracado, cinco por linha.
"""
import html, os
from honey_template import HDR, FTR

ROXO, LARANJA, CINZA = "#42067E", "#FF7502", "#A6A6A6"

CSS = """
@page { size: 210mm 297mm; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:"Liberation Sans",Arial,Helvetica,sans-serif; color:#000;
       -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { position:relative; width:595.44pt; height:841.68pt; overflow:hidden; background:#fff; }
.hdr { position:absolute; left:1.10pt; top:0.65pt; width:596.75pt; height:170.85pt; }
.ftr { position:absolute; left:1.33pt; bottom:0.58pt; width:593.22pt; height:143.40pt; }
.body { position:absolute; left:0; top:171pt; width:595.44pt; }
.t1 { text-align:center; font-size:11.04pt; }
.t2 { text-align:center; font-size:12pt; font-weight:bold; color:#FF7502; margin-top:3pt; }
.sub { margin:19pt 0 0 49.92pt; font-size:9.96pt; font-weight:bold; color:#42067E; }
.fmt { margin:3.5pt 0 0 49.92pt; font-size:9.96pt; }
.fmt b { font-weight:bold; }
.tira { margin:18pt 0 0 49.92pt; width:496.56pt; display:flex; gap:8pt; }
.q { width:92.9pt; }
.q svg { display:block; width:92.9pt; height:165pt; border:0.6pt solid #A6A6A6; }
.cn { margin-top:4pt; font-size:8pt; font-weight:bold; color:#FF7502; }
.cd { margin-top:2pt; font-size:6.4pt; line-height:1.28; }
.ct { margin-top:3pt; font-size:6.4pt; line-height:1.28; }
.ct b { color:#FF0000; }
.rod { margin:16pt 0 0 49.92pt; width:496.56pt; font-size:8pt; line-height:1.35; }
.rod b { color:#42067E; }
"""

def quadro(svg, numero, descricao, marcacoes):
    txt = "".join('<div class="ct"><b>%s</b> %s</div>'
                  % (html.escape(t), html.escape(x)) for t, x in marcacoes)
    return ('<div class="q">%s<div class="cn">CENA %s</div>'
            '<div class="cd">%s</div>%s</div>'
            % (svg, numero, html.escape(descricao), txt))

def montar(titulo, formato, cliente, quadros, rodape, saida):
    doc = ("<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'><title>%s</title>"
           "<style>%s</style></head><body><div class='page'>"
           "<img class='hdr' src='data:image/png;base64,%s'>"
           "<img class='ftr' src='data:image/png;base64,%s'>"
           "<div class='body'>"
           "<div class='t1'>STORYBOARD DE</div><div class='t2'>GRAVAÇÃO</div>"
           "<div class='sub'>%s</div>"
           "<div class='fmt'><b>Formato:</b> %s | <b>Cliente:</b> %s</div>"
           "<div class='tira'>%s</div>"
           "<div class='rod'>%s</div>"
           "</div></div></body></html>"
           % (html.escape(titulo), CSS, HDR, FTR, html.escape(titulo),
              html.escape(formato), html.escape(cliente),
              "".join(quadros), rodape))
    with open(saida, "w", encoding="utf-8") as f:
        f.write(doc)
    print("html gerado:", saida, len(doc), "bytes")

# ---------- vocabulario de desenho ----------

def svg(corpo, guias=True):
    g = ('<line x1="46.5" y1="0" x2="46.5" y2="160" stroke="%s" stroke-width="0.3" '
         'stroke-dasharray="2 3" opacity="0.5"/>' % CINZA) if guias else ""
    return ('<svg viewBox="0 0 93 160" xmlns="http://www.w3.org/2000/svg" '
            'fill="none" stroke-linecap="round" stroke-linejoin="round">'
            '<rect x="0" y="0" width="93" height="160" fill="#fff"/>%s%s</svg>' % (g, corpo))

def chao(y=132):
    return '<line x1="0" y1="%s" x2="93" y2="%s" stroke="%s" stroke-width="0.8"/>' % (y, y, CINZA)

def pessoa(cx, topo=38, h=1.0, bone=None, virada=0, chao_y=None):
    """Figura de frente. virada: -1 esquerda, 0 centro, 1 direita."""
    r = 9 * h
    cy = topo + r
    dx = virada * 3.0
    p = []
    p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" stroke="%s" stroke-width="1.4"/>'
             % (cx + dx, cy, r, ROXO))
    if bone:
        p.append('<path d="M %.1f %.1f a %.1f %.1f 0 0 1 %.1f 0 z" fill="%s" stroke="%s" '
                 'stroke-width="1"/>' % (cx + dx - r, cy - r * 0.35, r, r * 0.95, 2 * r, bone, bone))
        lado = 1 if virada >= 0 else -1
        p.append('<path d="M %.1f %.1f q %.1f 1.5 %.1f 3.5 l %.1f 0 z" fill="%s" stroke="%s" '
                 'stroke-width="0.8"/>'
                 % (cx + dx + lado * r * 0.9, cy - r * 0.35, lado * 6, lado * 7,
                    -lado * 7, bone, bone))
    y0 = cy + r
    p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4"/>'
             % (cx + dx, y0, cx, y0 + 4 * h, ROXO))
    om = 17 * h
    p.append('<path d="M %.1f %.1f Q %.1f %.1f %.1f %.1f L %.1f %.1f L %.1f %.1f Z" '
             'stroke="%s" stroke-width="1.4"/>'
             % (cx - om, y0 + 11 * h, cx, y0 + 2 * h, cx + om, y0 + 11 * h,
                cx + om * 0.82, y0 + 46 * h, cx - om * 0.82, y0 + 46 * h, ROXO))
    p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4"/>'
             % (cx - om, y0 + 12 * h, cx - om - 3, y0 + 40 * h, ROXO))
    p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4"/>'
             % (cx + om, y0 + 12 * h, cx + om + 3, y0 + 40 * h, ROXO))
    if chao_y:
        base = y0 + 46 * h
        for lado in (-1, 1):
            p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                     'stroke-width="1.4"/>'
                     % (cx + lado * 7 * h, base, cx + lado * 9 * h, chao_y, ROXO))
    return "".join(p)

def quadriciclo(cx, cy, e=1.0, cor=None):
    c = cor or ROXO
    r = 8 * e
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" stroke="%s" stroke-width="1.3"/>'
            '<circle cx="%.1f" cy="%.1f" r="%.1f" stroke="%s" stroke-width="1.3"/>'
            '<path d="M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z" stroke="%s" '
            'stroke-width="1.3"/>'
            '<path d="M %.1f %.1f L %.1f %.1f L %.1f %.1f" stroke="%s" stroke-width="1.3"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.3"/>'
            % (cx - 13 * e, cy, r, c, cx + 13 * e, cy, r, c,
               cx - 17 * e, cy - 7 * e, cx - 9 * e, cy - 15 * e, cx + 9 * e, cy - 15 * e,
               cx + 17 * e, cy - 7 * e, c,
               cx - 9 * e, cy - 15 * e, cx - 7 * e, cy - 24 * e, cx - 6 * e, cy - 25 * e, c,
               cx - 12 * e, cy - 25 * e, cx, cy - 25 * e, c))

def bone_icone(x, y, e=1.0, cor=None):
    c = cor or LARANJA
    return ('<path d="M %.1f %.1f a %.1f %.1f 0 0 1 %.1f 0 z" fill="%s" stroke="%s" '
            'stroke-width="0.8"/>'
            '<path d="M %.1f %.1f q %.1f 1.5 %.1f 3.5 l %.1f 0 z" fill="%s" stroke="%s" '
            'stroke-width="0.8"/>'
            % (x, y, 9 * e, 8 * e, 18 * e, c, c,
               x + 17 * e, y, 6 * e, 7 * e, -7 * e, c, c))

def seta(x1, y1, x2, y2, cor=None):
    c = cor or LARANJA
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2"/>'
            '<path d="M %.1f %.1f l %.1f -2.5 l 0 5 z" fill="%s"/>'
            % (x1, y1, x2, y2, c, x2, y2, -3 if x2 > x1 else 3, c))

def etiqueta(texto, y=12):
    return ('<text x="46.5" y="%s" font-family="Liberation Sans, Arial" font-size="6" '
            'fill="%s" text-anchor="middle" stroke="none">%s</text>'
            % (y, ROXO, html.escape(texto)))
