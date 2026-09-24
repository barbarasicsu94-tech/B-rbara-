# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"BV Locadora"

PAGINAS = [
 (u"ROTEIRO | FINAL DE SEMANA", u"até 30 segundos | até 4 cenas", CLIENTE, [
  ("01", u"0s a 7s",
   u"Imagem: Pessoa andando a pé no sol quente, visivelmente cansada e desconfortável. "
   u"Pode usar planos fechados no rosto, passos e sol forte para reforçar a situação.",
   [(u"OFF:", u"Final de semana chegando e você ainda está sem carro?")]),
  ("02", u"7s a 13s",
   u"Imagem: Faz a virada da situação. Corte mais dinâmico entrando na BV Locadora, "
   u"começando pela fachada.",
   [(u"OFF:", u"Calma, ainda dá tempo de resolver isso."),
    (u"LETTERING NA TELA:",
     u"CALMA\n"
     u"entra primeiro, em destaque\n"
     u"depois entra:\n"
     u"AINDA DÁ TEMPO DE RESOLVER ISSO\n"
     u"A ideia é esse texto acompanhar o ritmo da locução, com tipografia grande e movimento.")]),
  ("03", u"13s a 21s",
   u"Imagem: Mostrar os carros disponíveis na BV Locadora. Takes de detalhes, veículos "
   u"alinhados e apresentação rápida da estrutura.",
   [(u"OFF:", u"Na BV Locadora temos carros confortáveis e prontos pra você.")]),
  ("04", u"21s a 30s",
   u"Imagem: Pessoa já com o carro, entrando no veículo ou saindo da locadora. Finaliza com "
   u"take do carro seguindo e entra identidade da BV + WhatsApp.",
   [(u"OFF:", u"Não perca tempo e reserve agora seu carro pelo WhatsApp."),
    (u"LETTERING FINAL:", u"(95)98102-2395")]),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — BV Locadora | Final de Semana",
       os.path.join(RAIZ, "roteiro-final-de-semana.html"))
