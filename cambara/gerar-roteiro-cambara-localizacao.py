# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Cambará Materiais de Construção"
AUD = u"ÁUDIO (WEIZA):"
TELA = u"TEXTO NA TELA:"

PAGINAS = [
 (u"ROTEIRO CAMBARÁ — LOCALIZAÇÃO", u"Vertical | até 50 segundos", CLIENTE, [

  ("01", u"CHEGOU ÁUDIO",
   u"Gravação de tela real do celular. Conversa do WhatsApp aberta, contato “Weiza” "
   u"no topo. O áudio entra no chat, o dedo toca o play e a onda começa a correr. "
   u"Som de notificação real, sem trilha ainda.",
   [(AUD, u"Galera, é o seguinte: eu preciso de um vídeo bem legal pra mostrar a nossa "
          u"localização."),
    (TELA, u"A legenda do áudio acompanha a fala, no estilo da transcrição do "
           u"próprio WhatsApp.")]),

  ("02", u"NADA ROBÓTICO",
   u"A edição obedece ao pé da letra: entram 2 segundos de um institucional "
   u"caricato — imagem parada, fonte serifada, música de elevador, locução "
   u"metálica. Corta na hora com glitch e volta pra tela do WhatsApp.",
   [(AUD, u"Só que, por favor, nada daquela linguagem robótica, sabe? "
          u"“A Cambará está situada à rua tal, número tal…” Nada disso."),
    (TELA, u"não é isso aí")]),

  ("03", u"JEITINHO CAMBAR\u00c1",
   u"Corta pra vida real da loja: cliente sendo atendido no balc\u00e3o, movimento nos "
   u"corredores, algu\u00e9m carregando material. C\u00e2mera na m\u00e3o, luz natural, som "
   u"ambiente. Do nada um vendedor entra no quadro, d\u00e1 de ombros, sorri e abre os "
   u"bra\u00e7os \u2014 o jeitinho Cambar\u00e1 em pessoa. Congela no sorriso dele e entra "
   u"o carimbo na tela.",
   [(AUD, u"Eu quero uma coisa humana, do jeito que a gente fala aqui todo dia. "
          u"Aquele jeitinho Cambar\u00e1, sabe?"),
    (TELA, u"JEITINHO CAMBAR\u00c1 \u2014 carimbo entrando sobre o congelado")]),

  ("04", u"O DRONE",
   u"Drone gira em volta da fachada da Cambará. E gira. E gira de novo — o giro se "
   u"estende de propósito, até passar do ponto. Alguém da equipe entra no quadro "
   u"fazendo sinal de “já deu”.",
   [(AUD, u"Ah, e bota um drone girando, que fica bonito!"),
    (TELA, u"ela pediu")]),

  ("05", u"O ARIST\u00d3TELES",
   u"Corte para a placa da rua: RUA ARIST\u00d3TELIS CARNEIRO. Em seguida, uma est\u00e1tua grega "
   u"de m\u00e1rmore aparece plantada na cal\u00e7ada em frente \u00e0 loja, em inser\u00e7\u00e3o "
   u"de p\u00f3s com entrada c\u00f4mica. Quem passa na rua ignora a est\u00e1tua.",
   [(AUD, u"E j\u00e1 que a rua chama Arist\u00f3telis Carneiro, bota uma est\u00e1tua do "
          u"Arist\u00f3teles ali na frente, pra ningu\u00e9m esquecer. Aquele deus grego, sabe?"),
    (TELA, u"fil\u00f3sofo, Weiza. ele era fil\u00f3sofo.")]),

  ("06", u"A LOCALIZA\u00c7\u00c3O",
   u"A edi\u00e7\u00e3o fica s\u00e9ria por alguns segundos: ponto de refer\u00eancia conhecido "
   u"da cidade, o caminho at\u00e9 a loja, a placa da rua e a fachada da Cambar\u00e1. Setas e "
   u"lettering marcando o trajeto. A est\u00e1tua segue ali, discreta, no canto do quadro.",
   [(AUD, u"Mas n\u00e3o esquece de falar o endere\u00e7o certinho, viu?"),
    (TELA, u"Rua Arist\u00f3telis Carneiro, 147 - Cambar\u00e1")]),

  ("07", u"CAMBAR\u00c1 NO CAMBAR\u00c1",
   u"Split na tela: a placa do bairro de um lado, a fachada da loja do outro, com o lettering "
   u"empilhando CAMBAR\u00c1 sobre CAMBAR\u00c1. Volta pro WhatsApp com o \u201cdigitando\u2026\u201d "
   u"e a resposta da equipe. Fecha na fachada com a assinatura \u2014 e a est\u00e1tua ainda "
   u"parada na cal\u00e7ada, no \u00faltimo quadro.",
   [(AUD, u"Ah, e deixa claro que a Cambar\u00e1 fica no Cambar\u00e1 mesmo, viu? O bairro "
          u"tamb\u00e9m chama Cambar\u00e1. A\u00ed n\u00e3o tem como errar."),
    (AUD, u"Ficou bom assim?"),
    (TELA, u"LOJA: CAMBAR\u00c1 / BAIRRO: CAMBAR\u00c1 / \u00e9 isso mesmo\n"
           u"Resposta no chat: Ficou \u00f3tima, Weiza. J\u00e1 t\u00e1 no ar.\n"
           u"Assinatura: logo da Cambar\u00e1 + Rua Arist\u00f3telis Carneiro, "
           u"147 - Cambar\u00e1")]),
 ], 2),
]

montar(PAGINAS, u"Roteiro de Gravação — Cambará | Localização",
       os.path.join(RAIZ, "roteiro-cambara-localizacao.html"))
