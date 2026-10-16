# -*- coding: utf-8 -*-
import base64, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Tropical"
TIT = (u"DIRECIONAMENTO DE", u"FOTOS")
CAB = (u"BLOCO", u"COMO FAZER", u"ATENÇÃO")
A = u"ATENÇÃO:"

def b64(nome):
    with open(os.path.join(RAIZ, "assets", nome), "rb") as f:
        return base64.b64encode(f.read()).decode()

TOPO = (u'''
    <div class="refs">
      <div class="ref"><img src="data:image/jpeg;base64,%s">
        <p><b>REFERÊNCIA 1</b><br>Sentado à mesa, notebook, showroom desfocado ao fundo.</p></div>
      <div class="ref"><img src="data:image/jpeg;base64,%s">
        <p><b>REFERÊNCIA 2</b><br>Em pé, braços cruzados, carros desfocados ao fundo.</p></div>
      <div class="refn">
        <b>O que repetir das referências</b><br>
        Pessoa em foco e showroom desfocado atrás, com os carros reconhecíveis mas sem
        competir com o rosto. Olhar sempre na câmera, sorriso leve e natural.
        Luz clara, sem sombra dura no rosto. Enquadramento da cintura para cima,
        sobrando ar acima da cabeça.<br><br>
        <b>Duas poses por vendedor</b><br>
        Uma em pé, como a referência 2, e uma sentado à mesa, como a 1.
        Assim o card tem opção na hora da arte.
      </div>
    </div>''') % (b64("ref-sentado.jpg"), b64("ref-em-pe.jpg"))

VENDEDORES = [
 ("01", u"ENQUADRAMENTO",
  u"Fotografar na vertical, pensando no card. Plano médio, da cintura para cima, com "
  u"folga acima da cabeça para a arte respirar. Fazer também um plano mais fechado, "
  u"do peito para cima.",
  [(A, u"Câmera na altura dos olhos. Acima afina, abaixo engorda.")]),

 ("02", u"POSE EM PÉ",
  u"Braços cruzados ou mãos soltas ao lado do corpo. Ombros levemente na diagonal, "
  u"peso em uma perna só, rosto virado para a câmera. Sorriso leve.",
  [(A, u"Ombro de frente achata. Girar um pouco o corpo e manter o rosto na lente.")]),

 ("03", u"POSE SENTADO",
  u"À mesa, com o notebook aberto, uma mão no teclado, corpo levemente virado para a "
  u"câmera. Pode ter papel e caneta na mesa, como na referência.",
  [(A, u"Mesa limpa. Tirar copo, celular, papel solto e cabo à mostra.")]),

 ("04", u"FUNDO",
  u"Showroom com os carros atrás, sempre desfocado. Abertura aberta para separar a pessoa "
  u"do fundo. Escolher um ponto da loja e repetir para todos.",
  [(A, u"Nada de placa de preço, caixa ou bagunça no quadro. Conferir o que nasce "
       u"atrás da cabeça.")]),

 ("05", u"LUZ",
  u"Luz da vitrine entrando de lado como principal. Posicionar a pessoa a 45 graus da janela, "
  u"nunca de costas para ela.",
  [(A, u"Fugir da luz direta do teto: ela cria sombra funda no olho e no queixo.")]),

 ("06", u"ROUPA E APARÊNCIA",
  u"Padronizar entre todos: camisa social ou uniforme da Tropical. Evitar estampa, listra fina "
  u"e logo de outra marca. Crachá alinhado e reto.",
  [(A, u"Antes de cada clique: gola, cabelo e ombro. Dois minutos aqui poupam retoque depois.")]),

 ("07", u"CONSISTÊNCIA",
  u"Mesma distância, mesma altura de câmera, mesma luz e mesmo fundo para todos os "
  u"vendedores. Marcar o chão com fita.",
  [(A, u"Os cards vão aparecer lado a lado no feed. Qualquer variação fica "
       u"óbvia na grade.")]),
]

CARROS = [
 ("01", u"ÂNGULOS OBRIGATÓRIOS",
  u"Por modelo: 3/4 dianteira, lateral exata, 3/4 traseira e frente. Sempre na altura do farol, "
  u"não da sua cabeça.",
  [(A, u"Rodas alinhadas e viradas para o mesmo lado em todos os carros.")]),

 ("02", u"DETALHES",
  u"Roda, faróis, logo, maçaneta e acabamento. São os planos que dão textura "
  u"ao card e ao carrossel.",
  [(A, u"Carro limpo e seco. Marca de dedo e poeira aparecem muito no close.")]),

 ("03", u"INTERIOR",
  u"Painel, volante, bancos dianteiros e traseiros, central multimídia e porta-malas aberto.",
  [(A, u"Porta aberta deixa entrar luz. Conferir reflexo do fotógrafo no vidro e no painel.")]),

 ("04", u"FUNDO E POSIÇÃO",
  u"Afastar o carro da parede e de outros veículos sempre que der. Fundo limpo valoriza a "
  u"silhueta.",
  [(A, u"Reflexo é o maior inimigo: observar o que a lataria está espelhando antes "
       u"de clicar.")]),

 ("05", u"PADRÃO ENTRE MODELOS",
  u"Repetir o mesmo ângulo e a mesma distância em todos os modelos, para a grade "
  u"ficar uniforme.",
  [(A, u"Fotografar na vertical também, além do horizontal, pensando no story.")]),
]

PAGINAS = [
 (u"VENDEDORES | TROPICAL", u"Fotos para cards | Vertical", CLIENTE, VENDEDORES,
  2, None, None, CAB, TOPO, TIT, False),
 (u"MODELOS DE CARROS | TROPICAL", u"Fotos para cards e carrosséis", CLIENTE, CARROS,
  1, None, None, CAB, None, TIT, False),
]

montar(PAGINAS, u"Direcionamento de Fotos — Tropical",
       os.path.join(RAIZ, "direcionamento-fotos.html"))
