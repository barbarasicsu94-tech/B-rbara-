# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Cambará Materiais de Construção"
AUD = u"ÁUDIO (WEIZA):"
TELA = u"TEXTO NA TELA:"

PAGINAS = [
 (u"ROTEIRO CAMBARÁ — LOCALIZAÇÃO", u"Vertical | até 45 segundos", CLIENTE, [

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

  ("03", u"LINGUAGEM HUMANA",
   u"Corta pra vida real da loja: vendedor rindo, cliente sendo atendido no balcão, "
   u"alguém carregando material, movimento nos corredores. Câmera na mão, "
   u"luz natural, som ambiente real.",
   [(AUD, u"Eu quero uma coisa humana, do jeito que a gente fala aqui todo dia.")]),

  ("04", u"O DRONE",
   u"Drone gira em volta da fachada da Cambará. E gira. E gira de novo — o giro se "
   u"estende de propósito, até passar do ponto. Alguém da equipe entra no quadro "
   u"fazendo sinal de “já deu”.",
   [(AUD, u"Ah, e bota um drone girando, que fica bonito!"),
    (TELA, u"ela pediu")]),

  ("05", u"A LOCALIZAÇÃO",
   u"A edição fica séria por alguns segundos: ponto de referência conhecido da "
   u"cidade, o caminho até a loja, placa da rua e a fachada da Cambará. Setas e "
   u"lettering marcando o trajeto.",
   [(AUD, u"Mas não esquece de falar onde a gente fica, viu?"),
    (TELA, u"[ENDEREÇO DA CAMBARÁ — rua, número e bairro a confirmar]")]),

  ("06", u"FECHAMENTO",
   u"Volta pra tela do WhatsApp. Aparece “digitando…” e entra a resposta da equipe. "
   u"Corta para plano aberto da fachada e assinatura da Cambará com o endereço.",
   [(AUD, u"Ficou bom assim?"),
    (TELA, u"Resposta no chat: Ficou ótima, Weiza. Já tá no ar.\n"
           u"Assinatura: logo da Cambará + endereço")]),
 ], True),
]

montar(PAGINAS, u"Roteiro de Gravação — Cambará | Localização",
       os.path.join(RAIZ, "roteiro-cambara-localizacao.html"))
