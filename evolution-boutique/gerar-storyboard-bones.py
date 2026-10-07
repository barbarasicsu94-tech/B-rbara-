# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_storyboard import (montar, quadro, svg, chao, pessoa, bone_icone,
                              seta, etiqueta, ROXO, LARANJA, CINZA)

RAIZ = os.path.dirname(os.path.abspath(__file__))

def prateleira(y, itens, cor=CINZA):
    s = '<line x1="8" y1="%s" x2="85" y2="%s" stroke="%s" stroke-width="1"/>' % (y, y, CINZA)
    for i, c in enumerate(itens):
        s += bone_icone(12 + i * 25, y - 1, 0.55, c)
    return s

MARCA = ('<path d="M 38 150 l 8 6 l 8 -6" stroke="%s" stroke-width="1.2"/>'
         '<line x1="46" y1="143" x2="46" y2="156" stroke="%s" stroke-width="1.2"/>' % (LARANJA, LARANJA))

Q1 = svg(etiqueta("PLANO BASE") + prateleira(34, [CINZA, CINZA, CINZA]) + chao(140)
         + pessoa(46, topo=48, h=0.95, bone=ROXO, chao_y=140) + MARCA)
Q2 = svg(etiqueta("VIRADA DE CABEÇA") + chao(140)
         + pessoa(46, topo=48, h=0.95, bone=ROXO, virada=-1, chao_y=140)
         + seta(30, 54, 16, 54) + seta(62, 54, 76, 54))
Q3 = svg(etiqueta("UMA COR POR TAKE") + chao(140)
         + pessoa(46, topo=52, h=0.9, bone=LARANJA, chao_y=140)
         + bone_icone(10, 20, 0.6, ROXO) + bone_icone(38, 20, 0.6, LARANJA)
         + bone_icone(66, 20, 0.6, CINZA))
Q4 = svg(etiqueta("A BOUTIQUE")
         + prateleira(48, [ROXO, LARANJA, CINZA])
         + prateleira(84, [LARANJA, CINZA, ROXO])
         + prateleira(120, [CINZA, ROXO, LARANJA])
         + '<rect x="4" y="24" width="85" height="124" stroke="%s" stroke-width="0.8"/>' % CINZA)
Q5 = svg(etiqueta("FECHAMENTO + LOGO") + chao(140)
         + pessoa(46, topo=44, h=1.0, bone=ROXO, chao_y=140)
         + '<rect x="26" y="146" width="41" height="11" rx="2" fill="%s" stroke="none"/>' % ROXO
         + '<rect x="26" y="146" width="8" height="11" fill="%s" stroke="none"/>' % LARANJA)

QUADROS = [
 quadro(Q1, "01", "Enquadramento base. Pessoa de frente, centralizada, com a boutique ao fundo. "
                  "Tripé travado e marcação de fita no chão.",
        [("NOTA:", "Câmera, luz e posição não mudam entre um boné e "
                   "outro.")]),
 quadro(Q2, "02", "Movimento base. A cabeça vira para um lado e volta ao centro; depois "
                  "para o outro lado e volta.",
        [("NOTA:", "O corte acontece no meio da virada, quando o rosto sai de quadro. É ali "
                   "que o boné troca.")]),
 quadro(Q3, "03", "Repetição com cada boné. Mesmo enquadramento e mesma "
                  "posição; só muda a cor e o modelo.",
        [("NOTA:", "Ao menos 3 takes por boné. Quanto mais modelos, mais forte o stop "
                   "motion.")]),
 quadro(Q4, "04", "A boutique. Araras e prateleiras, bonés expostos lado a lado, "
                  "óculos, luvas e acessórios. Closes de aba, logo e costura.",
        [("NOTA:", "É o que mostra que a Evolution também é lifestyle, não "
                   "só veículos.")]),
 quadro(Q5, "05", "Fechamento. Último boné, a pessoa pára de frente, olha para a "
                  "câmera e sorri. Entrada da logo.",
        [("NOTA:", "Deixar o último plano respirar 2 segundos para a assinatura.")]),
]

RODAPE = (u"<b>Continuidade:</b> tripé travado, fita no chão, mesma roupa e mesma luz "
          u"em todos os takes — é o que faz a troca parecer mágica. "
          u"<b>Montagem:</b> alternar as trocas com os planos da boutique para segurar o ritmo. "
          u"<b>Áudio:</b> sem locução, só trilha marcando o corte.")

montar(u"DIRECIONAMENTO | BONÉS EVOLUTION BOUTIQUE",
       u"Vertical (9:16) | sem locução", u"Evolution Boutique",
       QUADROS, RODAPE, os.path.join(RAIZ, "storyboard-bones.html"))
