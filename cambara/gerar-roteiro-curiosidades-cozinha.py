# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Cambará Materiais de Construção"

PAGINAS = [
 (u"ROTEIRO — JEITINHO CAMBARÁ | 3 CURIOSIDADES SOBRE SUA COZINHA",
  u"Reels vertical | até 40s", CLIENTE, [

  ("01", u"",
   u"Personagem de costas, organizando o armário da cozinha, e guardando ali uma lata de "
   u"tinta no meio dos itens, algo fora de lugar, que prende a atenção. Fecha a "
   u"porta, vira e olha para a câmera para emendar a segunda metade da fala.",
   [(u"OFF:", u"Você usa sua cozinha todos os dias,"),
    (u"ON:", u"mas tem três coisas sobre ela que talvez você nunca tenha imaginado."),
    (u"LETTERING:", u"3 coisas que você talvez não sabia sobre sua cozinha")]),

  ("02", u"",
   u"Personagem em cena, intercalando com imagens de apoio, grafismos e detalhes da cozinha.\n"
   u"Corte rápido entre a primeira e a segunda curiosidade.",
   [(u"ON:", u"A primeira: a cozinha planejada, como a gente conhece hoje, começou a ganhar "
             u"forma em 1926, com a famosa Cozinha de Frankfurt."),
    (u"ON:", u"E a segunda: existe uma técnica chamada triângulo de trabalho. A ideia "
             u"é posicionar geladeira, pia e fogão de um jeito que deixe a rotina na "
             u"cozinha mais prática."),
    (u"LETTERING:", u"1. Cozinha planejada: desde 1926\n"
                    u"2. Triângulo de trabalho = mais praticidade")]),

  ("03", u"",
   u"Aqui acontece a mudança da trilha. A personagem fecha o armário ou faz uma "
   u"transição de movimento e começa a mostrar os modelos disponíveis na "
   u"Cambará.\nCortes rápidos mostrando opções, abrindo portas, gavetas e "
   u"detalhes dos armários.",
   [(u"ON:", u"Agora, a terceira talvez você realmente não soubesse: o seu próximo "
             u"armário pode estar aqui na Cambará!"),
    (u"ON/OFF:", u"O fim do ano já está chegando. Então que tal começar o "
                 u"próximo ano com uma cozinha nova, mais bonita e organizada? Aqui na "
                 u"Cambará tem opções pra você escolher.")]),

  ("04", u"",
   u"Personagem ao lado de um dos armários. Pode fechar uma porta ou gaveta e olhar "
   u"diretamente para a câmera.",
   [(u"ON:", u"Porque renovar a casa também pode começar pela cozinha. E esse é o "
             u"Jeitinho Cambará de começar o ano de casa renovada!"),
    (u"LETTERING FINAL:", u"JEITIN CAMBARÁ")]),
 ], 1),
]

montar(PAGINAS, u"Roteiro de Gravação — Cambará | Curiosidades sobre a Cozinha",
       os.path.join(RAIZ, "roteiro-curiosidades-cozinha.html"))
