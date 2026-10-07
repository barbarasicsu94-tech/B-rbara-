# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_storyboard import (montar, quadro, svg, chao, pessoa, quadriciclo,
                              seta, etiqueta, ROXO, LARANJA, CINZA)

RAIZ = os.path.dirname(os.path.abspath(__file__))

Q1 = svg(etiqueta("PLANO MÉDIO") + chao(128)
         + pessoa(32, topo=36, h=0.92, chao_y=128)
         + quadriciclo(68, 120, 0.72))
Q2 = svg(etiqueta("TAKES DOS MODELOS") + chao(128)
         + quadriciclo(24, 70, 0.6, CINZA)
         + quadriciclo(66, 95, 0.75)
         + quadriciclo(34, 120, 0.9, LARANJA)
         + seta(12, 140, 80, 140))
Q3 = svg(etiqueta("CLOSE / DETALHE")
         + '<circle cx="34" cy="92" r="26" stroke="%s" stroke-width="1.6"/>' % ROXO
         + '<circle cx="34" cy="92" r="11" stroke="%s" stroke-width="1.2"/>' % ROXO
         + '<circle cx="34" cy="92" r="3" fill="%s" stroke="none"/>' % LARANJA
         + '<path d="M 62 56 L 64 76 L 60 80" stroke="%s" stroke-width="1.6"/>' % ROXO
         + '<line x1="54" y1="56" x2="76" y2="56" stroke="%s" stroke-width="1.6"/>' % ROXO
         + '<path d="M 56 104 L 82 104 L 78 114 L 56 114 Z" stroke="%s" stroke-width="1.3"/>' % ROXO)
Q4 = svg(etiqueta("APRESENTADOR + ATV") + chao(128)
         + quadriciclo(22, 112, 0.6, CINZA)
         + quadriciclo(72, 116, 0.65, CINZA)
         + pessoa(47, topo=40, h=0.95, chao_y=128))
Q5 = svg(etiqueta("FECHAMENTO + LOGO") + chao(128)
         + pessoa(46, topo=34, h=1.0, chao_y=128)
         + '<rect x="26" y="136" width="41" height="13" rx="2" fill="%s" stroke="none"/>' % ROXO
         + '<rect x="26" y="136" width="8" height="13" fill="%s" stroke="none"/>' % LARANJA)

QUADROS = [
 quadro(Q1, "01", "Apresentador(a) ao lado de um dos quadriciclos infantis, olhando "
                  "diretamente para a câmera.",
        [("ON:", "A Semana das Crianças chegou! E que tal transformar essa data em uma "
                 "aventura inesquecível?")]),
 quadro(Q2, "02", "Takes dos quadriciclos seminovos disponíveis, mostrando diferentes "
                  "ângulos e modelos.",
        [("OFF:", "Aqui na Evolution Power Sports você encontra quadriciclos infantis "
                  "seminovos, perfeitos para quem quer começar a viver novas aventuras!")]),
 quadro(Q3, "03", "Close nos pneus, guidão, banco e acabamento dos quadriciclos, "
                  "valorizando os detalhes.",
        [("OFF:", "São opções para quem busca diversão e momentos especiais "
                  "sobre quatro rodas!")]),
 quadro(Q4, "04", "Apresentador(a) retorna em cena, próximo aos quadriciclos.",
        [("ON:", "E o melhor: eles estão disponíveis aqui na loja, esperando por "
                 "você!")]),
 quadro(Q5, "05", "Apresentador(a) olhando diretamente para a câmera. No encerramento, "
                  "cortes rápidos dos quadriciclos e entrada da logo.",
        [("ON:", "Aqui na Evolution Power Sports, a aventura não tem idade! Chame um dos "
                 "nossos vendedores no direct e garanta já o seu quadriciclo!")]),
]

RODAPE = (u"<b>Enquadramento:</b> vertical 9:16, apresentador(a) sempre no terço central. "
          u"<b>Luz:</b> natural, loja aberta. <b>Ritmo:</b> cenas 02 e 03 em cortes curtos, "
          u"cenas 01, 04 e 05 com o plano respirando para a fala. "
          u"<b>Duração alvo:</b> até 40 segundos.")

montar(u"ROTEIRO REELS | EVOLUTION POWER SPORTS — SEMANA DAS CRIANÇAS",
       u"Vertical (9:16) | Até 40 segundos", u"Evolution Power Sports",
       QUADROS, RODAPE, os.path.join(RAIZ, "storyboard-quadriciclos.html"))
