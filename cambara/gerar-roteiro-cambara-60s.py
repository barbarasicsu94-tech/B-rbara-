# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Cambará Materiais de Construção"

PAGINAS = [
 (u"ROTEIRO CAMBARÁ", u"Vertical | 60 s", CLIENTE, [
  ("01", u"",
   u"Personagem caminha pela rua com uma lista de obra na mão, olhando em volta como quem "
   u"procura algo. Passa em frente à fachada da Cambará, para, olha a fachada, sorri e "
   u"entra na loja. Jingle começa junto com o primeiro passo.",
   [(u"TEXTO:", u"JINGLE: O que você procura tem na Cambará")]),
  ("02", u"",
   u"Personagem entra e percorre os corredores. Cortes rápidos no ritmo da música: pilhas "
   u"de madeira, cimento, ferragens, tintas, prateleiras cheias.",
   [(u"TEXTO:", u"JINGLE: Material de construção / Tem variedade e solução")]),
  ("03", u"",
   u"Sequência de produtos na ordem de uma obra: madeira e estrutura, material básico e, "
   u"por último, acabamento (pisos, revestimentos, louças). Personagem riscando itens da lista.",
   [(u"TEXTO:", u"JINGLE: Do começo ao fim, até o acabamento / Na Cambará você "
                u"encontra tudo no momento")]),
  ("04", u"",
   u"Vendedor recebe o personagem sorrindo e mostra um produto; aperto de mão. Corte para o "
   u"caixa com compra rápida. Corte para a fachada com carro chegando/estacionando.",
   [(u"TEXTO:", u"JINGLE: Belo atendimento, fácil confiar / É fácil chegar, é "
                u"rápido comprar")]),
  ("05", u"",
   u"Close no personagem com as compras.",
   [(u"TEXTO:", u"JINGLE: Pra sua casa, pra sua empresa, pro seu projeto / Na Cambará você "
                u"encontra o lugar certo")]),
  ("06", u"",
   u"Personagem sai da loja satisfeito, olha para a câmera. Plano aberto da fachada. Texto na "
   u"tela com os 41 anos e logo final da Cambará.",
   [(u"TEXTO:", u"JINGLE: Cambará é na Cambará / O que você procura tem na "
                u"Cambará / São 41 anos fazendo parte da sua obra / Construindo história "
                u"por toda Roraima"),
    (u"TEXTO NA TELA:", u"41 anos construindo história em Roraima")]),
 ], True),
]

montar(PAGINAS, u"Roteiro de Gravação — Cambará 60s",
       os.path.join(RAIZ, "roteiro-cambara-60s.html"))
