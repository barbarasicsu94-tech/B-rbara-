# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Marina Evolution"

PAGINAS = [
 (u"ROTEIRO | CATAMARÃ", u"Vertical | 30–40s | 4 cenas", CLIENTE, [

  ("01", u"",
   u"Pessoa dentro ou próxima ao catamarã. Começa falando diretamente para a "
   u"câmera.\nEntram cortes do Rio Branco e do catamarã.",
   [(u"ON:", u"Sabe quando você percebe que a semana virou só trabalho, casa e trabalho "
             u"de novo? Às vezes, tudo que falta é fazer um programa diferente."),
    (u"LETTERING:", u"Que tal sair da rotina?")]),

  ("02", u"",
   u"Pessoa entrando no catamarã ou apresentando a embarcação. Mostrar detalhes "
   u"dos bancos, espaço e estrutura.",
   [(u"ON:", u"E uma opção que tá aqui, pertinho da gente, é aproveitar o Rio "
             u"Branco de catamarã."),
    (u"ON:", u"Ele está disponível aqui na Marina Evolution para você reunir sua "
             u"turma e curtir um passeio pelo rio.")]),

  ("03", u"",
   u"Personagem dentro do catamarã, em um enquadramento mais descontraído. Enquanto "
   u"fala, pode caminhar pelo espaço, sentar ou mostrar alguns detalhes da "
   u"embarcação.",
   [(u"ON:", u"Pode ser pra mudar o clima no meio da semana, comemorar alguma coisa ou "
             u"simplesmente aproveitar o final de semana de um jeito diferente."),
    (u"LETTERING:", u"Durante a semana ou no final de semana")]),

  ("04", u"",
   u"Pessoa novamente no catamarã. Finalizar com plano aberto da embarcação e do "
   u"Rio Branco.",
   [(u"ON:", u"Então já chama quem você levaria nesse passeio e vem falar com a "
             u"gente. O catamarã está te esperando aqui na Marina Evolution."),
    (u"LETTERING FINAL:", u"Disponível na Marina Evolution\n"
                          u"Consulte horários e disponibilidade")]),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — Marina Evolution | Catamarã",
       os.path.join(RAIZ, "roteiro-catamara.html"))
