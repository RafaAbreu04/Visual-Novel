# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sabrina Linklaster", color="#d61c0b")
define n = Character("[nome_robo]", color="#020e9c")
define sw = Character("Sarah Winter", color="#9604ba")
define p = Character("Penny Campbell", color="#08ba02")
define nar = Character("", color="#000000")
define c = Character("Cientista Samuel", color="#ffffff")
define cientistas = Character("Cientistas", color="#ffffff")
define jornal = Character("Jornal da Terra", color="#ffffff")
define m = Character("Mediador", color="#ffffff")
define l7 = Character("Líder do Setor 7", color="#ffffff")
define l11 = Character("Líder do Setor 11", color="#ffffff")
define militar = Character("Militar", color="#ffffff")
define d = Character("Desconhecida??", color="d61c0b")

#sprites

image penny_direita = "penny_direita.png"
image penny_esquerda = "penny_esquerda.png"

image robo_direita = "robo_direita.png"
image robo_esquerda = "robo_esquerda.png"

image sabrina_direita = "sabrina_direita.png"
image sabrina_esquerda = "sabrina_esquerda.png"

image sarah_direita = "sarah_direita.png"
image sarah_esquerda = "sarah_esquerda.png"

image samuel_direita = "samuel_direita.png"
image samuel_esquerda = "samuel_esquerda.png"

# Declare background
image deserto = "cenario_deserto.jpg"
image quarto = "Quarto.jpg"
image escritorio = "Escritório.jpg"
image lab = "Lab01.jpg"
image base = "BaseMilitar.jpg"
image tunel = "TúnelGrandeTrem.jpg"
image grandetrem = "GrandeTrem.jpg"
image cupula = "CúpulaDaTerra.jpg"
image sala = "sala_de_estar.jpg"
image cozinha = "cozinha.jpg"
image prisao = "Prisão.jpg"
image loja = "Loja.jpg"
image torres = "Torres-Brancas.jpg"
image tela_final = "tela_final.jpg"

init -1 python:
    import math
# The game starts here.

#ARCO DO TREINAMENTO E COMEÇO
################################################
label start:
    play music "audio/story time.ogg"
    pause(0.5)
    scene lab with fade
    nar"Laboratórios Linklaster - 7/10/2691."
    play sound "audio/heartbeat.mp3"
    #show samuel_esquerda
    #show samuel_esquerda at left with move
    
    #show penny
    #show penny at left with move
    nar"Uma nova robô está sendo criada, a mais poderosa já feita."
    nar"Seu objetivo é coordenar grandes tropas e inteligência artificial suficiente para ser a primeira de sua raça a ter um pensamento racional e e que reproduza emoções humanas."
    nar" Ela será essencial para enfrentar hordas de imundos."
    nar"Após dez dias de seu primeiro suspiro de vida, durante seu treinamento de parkour, realizou de forma voluntária um ataque a quatro cientistas, sendo assim, suas primeiras vítimas."
    nar"(Flashback)"
    #hide penny with moveoutleft

    show samuel_esquerda
    show samuel_esquerda at left with move
    c"- Verificando os últimos ajustes da robô HRF - 492. Componentes devidamente posicionados, software atualizado e atividade normal."
    c"- Por último, vamos ver se os movimentos estão corretos e se ela segue os comandos pedidos."

    pause(1.0)

    nar"O robô é solto da cabine e sua consciência e movimentação são liberadas. Em seguida, a robô recém-criada se levanta e se apresenta."
    show robo_direita
    show robo_direita at right with move
    nar"- Olá, sou a androide HRF-492, fui criada para servir as suas instruções. Qual será meu nome?"

    $ nome_robo = renpy.input("Seu nome será:", default = "Júlia")
    $ nome_robo = nome_robo.strip()

    if nome_robo == "":
        $ nome_robo = "Júlia"

    show samuel_esquerda
    show samuel_esquerda at left with move
    c"- Seu nome será [nome_robo]."
    show robo_direita
    show robo_direita at right with move

    n"- Meu nome foi definido como [nome_robo] no sistema."
    n"Hoje é dia 3 de junho de 2691, a temperatura mínima é de 13 graus e a máxima de 25, o céu está parcialmente nublado."
    c"- Iremos começar seu treinamento hoje mesmo, você será treinada para ser uma arma militar capaz de superar a habilidade de diversos soldados humanos."
    c" Por favor, me siga até a área de treinamento."
    n"- Entendido, irei segui-lo até o local."
    hide samuel_esquerda with moveoutleft
    hide robo_direita with moveoutright
    stop sound
    pause(0.5)
    scene base with fade
    nar"Base militar - Andar de testes -  17/11/2691"

    show samuel_esquerda
    show samuel_esquerda at left with move
    c"- Hoje o treino será de tiro. Diferente dos soldados comuns, você receberá um treinamento especial para auxiliar sua mira em situações importantes."
    c"- Vamos começar, o percurso possui inimigos móveis e obstáculos de diversos tipos espalhados com a neblina no modo de visão."
    hide samuel_esquerda with moveoutleft

    nar"[nome_robo] começa a treinar a sua mira ao alvo, carregamento e seu equilíbrio por seguidas horas."
    nar"Enquanto estava realizando o serviço, a robô estava em modo de batalha, essa função foi adicionada para priorizar a atenção dela e aumentar sua agressividade."

    cientistas"- Chegou a hora de iniciar o treinamento de elite!"
    cientistas"- Vamos colocar objetos em ambiente monitorado e deixaremos com que você tome a melhor decisão, assim avaliaremos seu raciocínio pessoal."
    cientistas"Qual arma você gostaria de usar?"
    show robo_esquerda
    show robo_esquerda at left with move

menu arma_treino:
    "Usar a metralhadora":
        $ arma = "metralhadora"
        n "Eu quero a metralhadora."
        jump a_metralhadora
    "Usar a arma laser":
        $ arma = "laser."
        n "Eu quero a arma laser."
        jump a_laser

label a_metralhadora:
    stop music
    #show robo_normal
    #show robo_normal at left with move
    n"Escuto passos vindo pelo corredor e lentamente meus sistemas ficam incontroláveis, a vontade de continuar atirando é incrível e não consigo mais parar."
    play music "audio/tiros.mp3"
    n"Quando percebo, minha mira vai em direção a alguns cientistas que ali passavam e sem a menor chance de se proteger metralho todos eles em poucos segundos."
    hide robo_esquerda with moveoutleft
    stop music
    jump noticia_jornal

label a_laser:
    play music "audio/laser.mp3"
    n"Meus sensores rapidamente me alertam sobre todas as pessoas presentes no prédio."
    n"Percebo a presença de 3 cientistas entrando para a sala de treinamento, a sensação de atirar me faz tão bem..."
    n"Não consigo mais me controlar. Aponto meus braços mecânicos para os cientistas e sem tempo de reação os carbonizo em poucos segundos com o laser."
    stop music
    hide robo_esquerda with moveoutleft
#label treinamento:
    #if arma == "metralhadora":
        #screen NOME:
    #imagemap:
        #ground "IMAGEM"
        #hover "IMAGEM"

        #hotspot (#, #, #, #) action Return("LUGAR")
        #hotspot (#, #, #, #) action Return("LUGAR2")
        #hotspot (#, #, #, #) action Return("LUGAR3")

    #if arma == "laser":
        #screen NOME:
    #imagemap:
        #ground "IMAGEM"
        #hover "IMAGEM"

        #hotspot (#, #, #, #) action Return("LUGAR")
        #hotspot (#, #, #, #) action Return("LUGAR2")
        #hotspot (#, #, #, #) action Return("LUGAR3")
    jump noticia_jornal

label noticia_jornal:
    play music "audio/story time.ogg"
    pause(0.5)
    scene lab with fade
    jornal"Houve um ataque em uma das bases militares, uma robô do exército atirou em pessoas que trabalhavam no local."
    jornal"Ela fez 4 vítimas, mas apenas 2 viveram."
    jornal"O caso está sendo investigado e a robô já foi contida, logo serão procurados possíveis erros de programação no sistema."

    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"- Precisamos fazer alguma coisa, equipe. \nUm acidente ocorreu e toda a pressão está sobre nós."
    s" Vamos reinicializar [nome_robo], tirando todas suas memórias atuais e ajustando o modo de combate."
    hide sabrina_esquerda with moveoutleft

    pause(0.5)
    nar"Laboratórios Linklaster - Andar 78 - 19/01/2699"
    show sabrina_esquerda
    show sabrina_esquerda at left with move

    s"Sinto falta da minha antiga amada, meu intuito desde o inicio foi conseguir trazê-la de volta à vida com a aparência que sempre mais gostei."
    s"Infelizmente, com a morte de minha esposa na grande onda que devastou o setor 17 no ano de 2688, me sinto muito sozinha."
    s"Além de me fazer companhia, [nome_robo] tem como objetivo trazer a segurança e a paz aos setores que nos restam, foi uma forma de ressignificar sua morte."
    s"Em meio aos corredores brancos e gelados, trago uma maleta prateada comigo."
    s"- A humanoide já está pronta para a análise final?"
    cientistas"- Sim, senhora! já tem uma equipe a trazendo para o laboratório"
    s"Em poucos minutos, o robô com a feição de minha amada entrará por essa porta…"
    s"Uma caixa enorme de metal levada por três grandes homens entra pelas grandes portas douradas da sala."
    s" Ao inserir minha chave de acesso e a leitura da minha íris, um gás branco sai pelas aberturas revelando minha amada aos poucos."
    s"Aos poucos, sua pele ganha cor e seus grandes olhos roxos se abrem. Nunca me senti assim antes, é uma sensação estranha ver sua respiração profunda novamente."
    s"Entrego minha mão para logar como primeira usuária e sinto sua pele macia como antes e a vontade de chorar é eminente."
    s"-Saiam da sala agora! Deixem ela aqui."
    s"Os entregadores envergonhados saem da sala rapidamente."
    s"Permaneço em uma realidade controversa por um tempo e aos poucos levo meu corpo ao dela e envolta em seu calor ardente, caio em lágrimas brilhantes."

    show robo_direita
    show robo_direita at right with move
    n"- Olá Dra. Sabrina obrigada por logar como primeira usuária, espero te fazer muito feliz!"
    s"-Você nem sabe como já me fez."
    s"Nós duas permanecemos ali por um momento interminável, nos abraçamos e assim nos conectamos como nunca antes."
    s"Colocando minha mão dentre seu cabelo, consigo sentir a vibração de seu sistema multifacetado."
    s"- Vamos, vamos para casa…"
    n"-Claro querida!"
    hide robo_direita with moveoutright
    hide sabrina_esquerda with moveoutleft

    pause(0.5)
    scene sala with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Ao chegarmos nas Altas Torres Brancas, mostro rapidamente toda a casa para ela e nos sentamos na sala de estar."
    s"Me deito como nunca antes no colo de [nome_robo] e ficamos assim por um bom tempo..."
    s"Alguns meses se passam…"
    hide sabrina_esquerda with moveoutleft

    pause(0.5)
    scene cozinha with fade
    nar"Torres Brancas Andar 83 - 16/06/2699"
    show robo_esquerda
    show robo_esquerda at left with move
    n"Faz alguns meses que fui nomeada como [nome_robo] e comecei a viver com Sabrina."
    n"Ando preocupada com ela, sempre trabalha demais e deixa de cuidar de si mesma."
    n"Às vezes, seu rosto ganha uma coloração pálida e ela se queixa de dores e fraqueza."
    n"Por isso, sempre procuro fazer as refeições e obrigá-la a comer e ir dormir cedo."
    n"Estou em nossa casa agora preparando a janta, daqui há pouco, Sabrina vai chegar em casa e estarei a esperando para comermos."
    pause(0.5)
    n"Se passa meia hora e Sabrina entra pela porta com uma feição cansada e esgotada."

    n"- Boa noite, querida. Como você está?"
    show sabrina_direita
    show sabrina_direita at right with move
    s"-Boa noite, estou atolada de trabalho, irei direto para o escritório."
    hide sabrina_direita with moveoutright

    n"Sabrina corta o assunto no meio e me deixa sozinha na cozinha. Me preocupo e fico irritada, estou fazendo de tudo para mantê-la bem."

    menu briga:
        "Confrontar Sabrina":
            jump confronto
        "Deixar para lá":
            jump ignorar

label confronto:
    show robo_esquerda
    show robo_esquerda at left with move
    n"Saio da cozinha furiosa e a sigo até a sala."
    pause(0.5)
    scene sala with fade
    show robo_esquerda
    show robo_esquerda at left with move
    n"- Sabrina, você já comeu algo por agora?"
    show sabrina_direita
    show sabrina_direita at right with move
    s"-Não, tenho um relatório muito importante sobre o projeto dos novos robôs."
    n"- Você precisa dar um tempo disso, venha comer, eu estou quase acabando a janta."
    s"- Juro que faço isso depois."
    n"- Porra! Você não tem tempo para nada, não se importa consigo, nem ao menos está me encarando enquanto conversamos, poderia fazer o mínimo de questão?"
    s"- ME DEIXA! Eu já disse que estou ocupada, não tenho tempo para ficar brigando com você agora, existem prioridades."
    n"-Tudo bem, você quem sabe o que é prioridade, não é?"
    n"Nem me dou o trabalho de continuar a briga e saio rápido de lá."
    hide sabrina_direita with moveoutright
    hide robo_esquerda with moveoutleft
    pause(0.5)
    scene cozinha with fade
    n"Estou furiosa, termino a janta e deixo um prato coberto para caso ela sinta fome e vá comer."
    hide robo_esquerda with moveoutleft
    jump continuacao_1

label ignorar:
    n"Acho que não posso fazer nada, Sabrina é teimosa e não vai me escutar, vou apenas terminar o jantar e fazer outra coisa."
    hide robo_esquerda with moveoutleft
    jump continuacao_1

label continuacao_1:
    pause(0.5)
    scene lab with fade
    nar"Altas Torres Brancas - Laboratórios Linklaster - Andar 78 - 16/06/2699"
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Sigo realizando testes em busca de uma futura cura… cura, como se isso fosse realmente uma solução para esse mundo…"
    s"Arrh, que náusea péssima… vou retirar amostras do meu próprio sangue para verificar que merda está acontecendo."
    s"Para isso, preciso procurar o kit de retirada de sangue pelo laboratório! Para onde eu deveria ir agora?"

    menu retirar_sangue:
        "Área de análises clínicas":
            jump lab_analises
        "Área de amostras":
            jump area_amostras

label area_amostras:
    s"-Aqui só tem os sangues que estão sendo examinados pela minha equipe."

    menu ir_lab_analise:
        "Área de análises clínicas":
            jump lab_analises

label lab_analises:
    s"- Aqui temos muitas centrífugas e tubos, era o que eu precisava!"
    s"Após separar todos os itens, pego o oclusor de punção juntamente com a seringa e sinto uma leve ardência."
    s"Enquanto encho todos os tubos necessários para o exame, olho para espesso líquido vermelho com repulsa."
    s"Aos poucos, carrego todos para a centrífuga mais próxima."
    s"Ao pressionar o botão para iniciar, deixo levar consigo o peso de minhas costas, me sinto mais leve."
    hide sabrina_esquerda with moveoutleft
    jump cupula_da_terra
    stop music

label cupula_da_terra:
    pause(0.5)
    scene cupula with fade
    nar"Cúpula da Terra - Setor Neutro - 24/06/2699"
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Alguns dias depois, ainda estou no aguardo dos resultados dos exames, estou em uma conferência no setor Neutro."
    s"A Cúpula da Terra é uma conferência que reúne líderes de diversos lugares, sendo arbitrada por mediadores."
    s"Uma vez ao ano ela é convocada, desta vez por causa de uma tempestade de areia que pode afetar todos os setores."
    s"A reunião começou agora..."
    stop music
    play sound "audio/interior.mp3"
    m"- Sejam bem-vindos à mais uma edição da Cúpula da Terra, como de costume, hoje iremos discutir assuntos urgentes sobre nosso planeta."
    s"A discussão se iniciou rapidamente com os governadores dos setores desérticos nervosos com a falta de preparo para lidar com a tempestade."
    l7"- Algo precisa ser feito, os cidadãos estão protegendo suas casas com os recursos básicos que temos, ainda existem os imundos para lidar."
    l7"- É verdade, já vocês possuem suas casas submersas dotadas de tecnologia que protegem seus rabos imundos."
    militar"- Olhe como fala, filho da puta!"
    s"- Mantenham a calma ou não conseguirão os recursos que vieram buscar!"
    stop sound
    play music "audio/story time.ogg"
    s"A partir daí, o caos se instaura, os mediadores tentaram parar com o conflito, mas não tiveram sucesso."
    s"No fim, nada foi resolvido, nem ao menos irão gerar alertas para a população antecipadamente."
    hide sabrina_esquerda with moveoutleft
    jump procurar_robo

label procurar_robo:
    pause(0.5)
    scene sala with fade
    nar"Torres Brancas Andar 83 - 02/07/2699"
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Entro em casa e o silêncio paira no ambiente. Fecho a porta atrás de mim e procuro [nome_robo] para entregar sua missão mensal."
    s"Onde eu deveria procurar primeiro?"
#escolha dos comodos

    menu procura:
        "Cozinha":
            jump cozinha

        "Quarto":
            jump quarto

        "Escritório":
            jump missao

label quarto:
    pause(0.5)
    scene quarto with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s" O quarto está vazio e até um pouco empoeirado, um feixe de luz entra pelas janelas e consigo aparecem as partículas de poeira no ar."
    s" Preciso enviar um comunicado à equipe de troca de filtro."

    menu quarto_cozinha_escritorio:
        "Cozinha":
            jump cozinha_escritorio

        "Escritório":
            jump missao

label cozinha_escritorio:
    pause(0.5)
    scene cozinha with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s" A cozinha está vazia com tons gelados, o oceano reflete na cama vazia e volto para o corredor."

    menu apenas_escritorio:
        "Escritório":
            jump missao

label cozinha:
    pause(0.5)
    scene cozinha with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s" A cozinha está vazia com tons gelados, o oceano reflete na cama vazia e volto para o corredor."

    menu cozinha_quarto_escritorio:
        "Quarto":
            jump quarto_escritorio

        "Escritório":
            jump missao

label quarto_escritorio:
    pause(0.5)
    scene quarto with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s" O quarto está vazio e até um pouco empoeirado, um feixe de luz entra pelas janelas e consigo aparecem as partículas de poeira no ar."
    s" Preciso enviar um comunicado à equipe de troca de filtro."

    menu so_escritorio:
        "Escritório":
            jump missao


# ARCO DA TEMPESTADE
#################################################
label missao:
    pause(0.5)
    scene escritorio with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"- Ei, tenho uma missão para você!"
    s"A entrego um envelope em vermelho carmim com textura de veludo que contém um chip com todas as informações para a continuação do bem estar nos setores."
    show robo_direita
    show robo_direita at right with move
    n"- Tudo bem, fecha a porta quando sair!"
    s"Em seguida bato a porta para irritá-la, não irei pedir desculpas por nada..."
    stop music

    pause(0.5)
    scene deserto with fade
    #alterar um pouco do deserto
    nar"Deserto - Dunas - Proximidades do Setor 6 - 16/07/2699"
    show robo_esquerda
    show robo_esquerda at left with move

    n"Dados da missão: Uma grande horda de imundos vem das grandes dunas vermelhas a caminho do setor 6 que sofre com as grandes crises hídricas."
    n"O ataque seria iminente e milhares acabariam infectados. Estamos a caminho da localização principal."
    n"- As ordens são claras, humanoides K-980, liquidar todos os imundos em um raio de 50 quilômetros do setor 6, teremos pouco menos de 24 horas para finalizar a missão."
    n"- Câmbio… aterrissando em 3, 2, 1!"
    n"Levo comigo 300 humanoides, todos aterrissaram e envio o sinal de preparação e impacto iminente no inimigo em 2 quilômetros."
    play sound "audio/tiros.mp3"
    n"Foram contabilizados mais de doze mil imundos na horda. Utilizamos metade de um cartucho supersônico para surpreendê-los."
    n"Que arma usar na batalha?"

    menu arma_deserto:
        "Metralhadora":
            jump metralhadora_deserto
        "Laser Atômico ":
            jump laser_deserto

label metralhadora_deserto:
    n"Meu braço se divide e transforma-se em uma metralhadora."
    n"Um som ensurdecedor se inicia e os flashes de luz das balas iluminam o campo de guerra, montantes de imundos que ali me rodeiam ficam vulneráveis, me dando espaço."
    n"Os imundos entram em desespero para saciar sua fome."
    stop music
    play music "audio/alarm rythm sinus.mp3"
    n" De repente, as sirenes do setor 6 soam a iminente chegada de uma tempestade de areia, ao horizonte é possível ver ela chegando e levando consigo todo deserto."
    n"Preciso agir!"
    jump pre_tempestade

label laser_deserto:
    n"Meu braço se desdobra e transforma-se em uma barra de aço capaz de gerar grandes ondas de energia."
    n"Grandes massas de imundos são devorados pelas enormes luzes do canhão atômico e permanecem em chamas até se tornarem pó."
    n"DROGA, usei muita energia nesse ataque. Alertas sobre o desligamento iminente aparecem em minha visão!"
    n"Não posso parar agora! Desligo rapidamente minha arma e poupo energia."
    stop music
    play music "audio/alarm rythm sinus.mp3"
    n"Noto uma grande nuvem a caminho em meio ao meu devaneio momentâneo e um dos imundos alcança minha perna e rasga meus sistemas de proteção corporais."
    n"Tenho que fazer algo!"
    jump pre_tempestade

label pre_tempestade:
    menu fugir_ou_projeto:
        #aqui a Sarah está com a Penny
        "Deixar o posto e fugir para o túnel do Grande Trem mais próximo":
            $ decisao = "fugir_sw&p"
            jump deixar_posto
            #aqui a Sarah está sozinha
        "Iniciar o projeto de proteção do setor contra a tempestade de areia":
            $ decisao = "iniciar_sw&n"
            jump iniciar_projeto


label deixar_posto:
    n"A chegada da onda de areia é eminente e lanço para o alto um sinalizador para todos baterem em retirada."
    n"Coloco em meu rastreador a localização do túnel do Grande Trem mais próximo e envio um sinal para todos robôs, continuo seguindo para lá."
    stop music
    n"Adentramos o Grande Túnel em um número razoável e busco uma zona de carregamento nos corredores frios da estação mais próxima para recuperarmos nossas forças."
    n"Coloco meus pés nos moldes de carregamento magnético e permaneço em descanso durante o passar da tempestade."
    hide robo_esquerda with moveoutleft
    jump garotas

label iniciar_projeto:
    n"Envio para todos presentes na tropa um aviso de impacto eminente da tempestade, vamos para a barreira e iniciamos o protocolo de fechada dos portões principais de forma precipitada."
    n"Os fortes ventos ja passam por mim, sou engulida pela areia, me sinto presa como nunca antes..."
    n" Minha bateria está no vermelho não sei se vou aguentar, decido iniciar o protocolo de desligamento e aguardar a tempestade melhorar enquanto sinto a areia cobrindo meu corpo aos poucos."
    hide robo_esquerda with moveoutleft
    jump garotas

label garotas:
    play music "audio/story time.ogg"
    pause(0.5)
    scene loja with fade
    nar"3 dias antes..."
    nar"Deserto - Dunas do Norte - Setor 9  - 13/07/2699"
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"O alarme da caixa registradora vai soar em dois minutos, minha melhor amiga está no fundo do mercado apontando o revólver 38 meio danificado que achamos numa pilhagem."
    sw" Os maricas estão tremendo de medo, mas é a lei da vida, estamos apenas fazendo o que precisamos para viver."
    sw"Preciso pensar em alguma forma de arrombar esse caixa, eu deveria tentar:"

    menu caixa:
        "Soco":
            sw" Não funciona e fico com a minha mão dolorida!"
            jump tentativa_2
        "Chave de fenda":
            sw"A fechadura se parte em duas!"
            jump fuga_garotas
        "Gazua":
            sw"A fechadura é aberta após algumas tentativas de realizar a volta completa."
            jump fuga_garotas

label tentativa_2:
    menu tentativa_caixa:
        "Chave de fenda":
            sw"A fechadura se parte em duas!"
            jump fuga_garotas
        "Gazua":
            sw"A fechadura é aberta após algumas tentativas de realizar a volta completa."
            jump fuga_garotas

label fuga_garotas:
    show penny_direita
    show penny_direita at right with move
    p"- Boaa! Agora pega toda essa merda e vamos antes que alguém apareça!"
    sw"Começo a guardar todas as moedas de cobre e escuto a chegada de uns malditos mercenários em alguns veículos."
    sw"- Bora, eles estão chegando, já terminei por aqui!"
    sw"Os vultos se aproximam do outro lado do quarteirão, por trás de uma grande fila de carros."
    p"-Que merda! O que vamo fazer?"
    sw"Entramos por um pequeno beco sujo e úmido sem saída e escalamos uma grade de metal."
    sw"Chegamos em uma rua escura e quando menos esperamos ao virar da rua, três grandes cachorros raivosos com a boca molhada nos perseguem."
    sw"- Vamo pegar um carro, entra rápido!"
    p"-Merda! Merda!"
    sw"Penny faz uma ligação direta e dispara com o carro. Entramos na avenida mais próxima e largamos o carro no acostamento mais próximo."
    sw"Continuamos andando em busca de algum abrigo seguro e olho o mapa que tenho na bolsa e vejo que estamos próximas do setor 8 onde conheço um abrigo até a poeira baixar, vamos passar a noite lá."
    hide sarah_esquerda with moveoutleft
    hide penny_direita with moveoutright

    pause(0.5)
    stop music
    scene deserto
    nar"Deserto - Dunas - Setor 8 - 16/08/2699"
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Hoje o dia amanheceu com o cheiro frio e pútrido do mofo dos abrigos do setor. Nossa fuga dura 3 dias..."
    sw"Vou à janela e escuto uma longa e alta sirene ecoando. O número de toques dela avisa que uma tempestade de areia está próxima..."
    sw"- Eii eii, Penny? Penny! Tá acordada?"
    show penny_direita
    show penny_direita at right with move
    p"- Ahn? Que, que foi agora??"
    sw"-Vai, levanta logo… tamo com um problema!"
    p"-Que porra ta acontecendo?"
    play music "audio/alarm rythm sinus.mp3"
    sw"-É uma tempestade de areia, deve ta por por aqui em pouco tempo!!!"
    p"- Que merda, que merda, QUE MERDA!"
    p"Tamo ferradaa Sarah, esse lugar não vai aguentar."
    sw"Saímos correndo enquanto a nuvem de areia se aproxima de forma apressada, levantando tudo que encontra pela frente."
    sw"- Vamos, tamo quase lá!"
    sw"Estamos em uma área de caça árdua, a possibilidade de encontrar armadilhas é enorme!"
    sw"Em meio a busca por forças contra o vento que nos puxa, Penny prende sua perna em uma armadilha e urra de dor."
    p"-AAAARGH! ME AJUDA!"

# se a pessoa escolher fugir com a robo, a decisao dela precisa ser salvar a penny, pq ai as duas encontram a robo lá depois

if decisao == "fugir_sw&p":
    jump salvar_penny_obrigatoriamente

if decisao == "iniciar_sw&n":
    jump abandonar_penny_obrigatoriamente
#-------------------------------------------------
label salvar_penny_obrigatoriamente:
    menu salve_penny:
        "Salvar Penny":
            jump com_penny
        "Abandonar Penny":
            jump penny_salva_de_qualquer_jeito

label penny_salva_de_qualquer_jeito:
    sw"O medo me consome e penso em não salvá-la. Quando vou voltar a correr sinto as mãos de Penny no meu tornozelo."
    p"Por favor! Me ajuda, Sarah."
    p"Eu não quero morrer agora!"
    sw"Eu não posso deixá-la aqui, como cogitei em abandoná-la no momento em que ela mais precisa de mim?"
    sw"- Me desculpa! Eu sou um monstro, eu não vou te deixar aqui."
    p"Você tá com medo, Sarah, eu te entendo!"
    jump com_penny
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#HISTORIA COM A PENNY
label com_penny:
    sw"O sentimento de urgência é colocado a posto e precisamos de abrigo."
    sw"- Deveríamos buscar a saída do grande trem e nos abrigar por lá até a tempestade passar!"
    p"-Vamos logo! Aargh!"
    hide sarah_esquerda with moveoutleft
    hide penny_direita with moveoutright
    pause(0.5)
    scene tunel with fade
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Com Penny apoiada em meu ombro direito, conseguimos adentrar ao grande túnel. A vontade de sobreviver nos levou rapidamente até aqui."
    sw"Deito Penny praticamente desmaiada em um banco e faço um torniquete em sua perna com pedaços de roupa."
    sw"Logo em seguida, depois de tudo que passamos, sinto minha visão escurecer..."
    stop music
    hide sarah_esquerda with moveoutleft

    pause(1.0)
    show sarah_esquerda
    show sarah_esquerda at left with move
    play music "audio/story time.ogg"
    sw"Sou acordada com leves toques por uma moça bem vestida, nunca a vi pelas nossas bandas."
    sw"Ela se apresenta como [nome_robo] e dizemos nossos nomes também."
    show robo_direita
    show robo_direita at right with move
    n"Venham comigo, não posso deixá-las aqui nessas condições."
    hide sarah_esquerda with moveoutleft
    hide robo_direita with moveoutright

    pause(0.5)
    play sound "audio/trem.mp3"
    scene grandetrem with fade
    nar"Grande Trem - A Caminho das Torres Brancas - 18/08/2699"
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Estamos no grande trem que leva até as Torres Brancas, eles não economizaram em suas instalações e projetos."

    pause(0.5)
    scene torres with fade
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Saindo do trem, a mulher que nos guiava teclou o número 83 no elevador, o prédio era debaixo d'água."
    sw"[nome_robo] nos dirgiu para um apartamento e nos abriu passagem."

    pause(0.5)
    scene sala with fade
    show robo_direita
    show robo_direita at right with move
    n"- Sintam-se à vontade, podem se acomodar temporariamente no sofá, irei cuidar de Penny."
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"[nome_robo] voltou com um kit de primeiros socorros em mãos."
    n"- Tudo bem, vamos ver como a ferida está."
    n"- Acredito que não tenha sido uma ferida tão profunda ao ponto de ter entrado algo, mas prefiro que seja averiguado."
    show penny_direita
    p"- Não temos condições pra ter acesso a esse tipo de coisa..."
    n"- Fiquem tranquilas, irei pedir para cuidarem de você, estão sob minha responsabilidade no momento."
    sw"- Valeu mesmo por tudo que está fazendo."
    sw"Nunca na vida algo assim ocorreu, parece um momento de sorte."
    n"- Peço que descansem no quarto de hóspedes, conversamos mais tarde."
    hide sarah_esquerda with moveoutleft
    hide penny_direita with moveoutright
    hide robo_direita with moveoutright

    pause(0.5)
    nar"Mais tarde, no mesmo dia..."
    show robo_esquerda
    show robo_esquerda at left with move
    n"Pouco tempo depois, enquanto estou arrumando a sala, Sabrina chega."
    n"- Já está em casa, que milagre."
    show sabrina_direita
    show sabrina_direita at right with move
    s"- Estou me sentindo cansada."
    n"- Está bem?"
    s"- Sim, estou bem, como vão as coisas?"
    n"Estão caóticas, uma tempestade surgiu do nada e devastou o que tinha pela frente. A batalha contra a horda foi difícil e saí danificada."
    s"- Não acredito, é sério? Devia ter me avisado, eu teria vindo logo e levado você."

    menu discussao:
        "Ocupada":
            jump ocupada
        "Não precisava":
            jump não_precisava

label ocupada:
    n"- Você anda muito ocupada, não queria te incomodar com coisas idiotas e estive ocupada de tarde."
    n"- Preciso te contar uma coisa, trouxe duas garotas para cá, elas estão no quarto de hóspedes."
    s"- Me contar? Por qual motivo alguém estaria aqui?"
    n"- Depois da tempestade, fui para o trem e lá encontrei duas garotas, elas precisavam de ajuda e não podia deixá-las."
    s"- Devia ter me avisado, não acha? Eu moro aqui, é a minha casa!"
    n"- Eu estou fazendo isso agora, eu não ia deixar as garotas sem um lugar para ficar."
    jump convencer_sabrina

label não_precisava:
    n"- Não precisa, eu posso ir sozinha amanhã!"
    s"- Não precisava falar assim, só queria ajudar..."
    n"Antes que Sabrina terminasse, escuto um barulho no quarto de hóspedes."
    n"Penny sai do quarto rapidamente para ver o que está acontecendo e Sabrina acaba vendo ela."
    s"- Quem é essa??? Você anda trazendo gente sem minha permissão para minha casa?"
    n"- Eu ia contar agora mesmo, as encontrei na estação de trem em péssima situação."
    s"- Que ideia brilhante! Achou duas mendigas e deicidiu trazer para cá."
    n"Elas estavam precisando de ajuda, droga!"
    jump convencer_sabrina

label convencer_sabrina:
    n"- Por favor, as deixe ficar, estou supervisionando as duas sempre, não confia em mim?"
    s"- Em você eu confio, mas trazer estranhas para casa não é algo normal!"
    n"- Pode não ser, mas quero fazer algo por elas. Passei o dia todo naquele deserto horrível e quem esperava uma tempestade daquela magnitude?"
    s"- Pensei que você daria conta."
    n"- Dar conta?? Então você sabia, por que não me avisou?"
    s"- Não me lembrei, eu juro. A reunião que participei na Cúpula não levou a nada e eu estava tão ocupada que me esqueci."

    menu enfrentar_sabrina:
        "Questionar":
            jump questionar
        "Se acalmar":
            jump acalmar

label questionar:
    n"- Se esqueceu mesmo? Não se esquece uma merda dessas, porra!"
    s"- Eu realmente esqueci, me desculpa!"
    n"- Milhares de pessoas podem estar mortas ou desaparecidas, até desabrigadas. O que me diz?"
    s"- Nada foi feito, não podia dar a notícia para a mídia. Para você eu podia, mesmo que não tenha feito isso..."
    n"- Você podia ter feito o certo, mas agora não adianta mais."
    s"-Eu sei. Sobre as garotas, as deixe ficar, estou fazendo isso por você!"
    hide robo_esquerda with moveoutleft
    hide sabrina_direita with moveoutright
    jump laboratorio_com_garotas

label acalmar:
    n"- Tudo bem....  Mas não dá para esquecer algo assim, você tem noção de como estava lá fora?"
    n"- Parecia o fim do mundo, se eu fosse humana estaria morta."
    s"-Eu devia ter avisado, me desculpe. Eu confio em você e por isso elas podem ficar aqui.."
    hide sabrina_direita with moveoutright
    pause(0.5)
    n"Depois de toda a conversa, Sabrina foi para o quarto e me deixou na sala."
    pause(0.5)
    scene cozinha with fade
    show robo_esquerda
    show robo_esquerda at left with move
    n"Decidi fazer o jantar para as garotas, imagino que estão com fome. Qual prato preparo?"

    menu janta:
        "Boeuf Bourguignon":
            jump bourguignon
        "Fettuccine à carbonara":
            jump fettucine

label bourguignon:
    n"Vou preparar um Bourguignon, uma carne guisada vai cair bem hoje. A Sabrina reagiu bem melhor do que eu esperava."
    n"Enquanto preparava a comida, acabo deixando uma gota de ensopado cair na minha calça e a mancho com gordura."
    n"Termino o cozimento e faço a mesa para chamar as meninas."
    n"- GAROTAS, o jantar está pronto, podem vir aqui na mesa por gentileza?"

    show sarah_direita
    show sarah_direita at right with move
    sw"- Tá bom, já vamos!"
    n"Algum tempo se passa e elas se sentam na mesa."
    n"- Pensei em algo caseiro para não estranharem muito."
    n"Sarah e Penny começam a comer rapidamente, acho que fazia algum tempo em que não comiam."
    show penny_direita
    p"- Nossa isso aqui... ta bom pra caramba!"
    sw"- Uau, tá mesmo uma delícia!"
    n"- Podem comer o quanto quiserem, fiz bastante e não precisam se preocupar comigo... Fico feliz que gostaram."
    n" Passamos horas sobre a mesa enquanto ambas se deliciavam sobre muitas bacias de ensopado com vinho."
    n"Foi um momento muito bom, acho que fazia um bom tempo que não me sentia assim... em um momento familiar."
    jump laboratorio_com_garotas

label fettucine:
    n"Irei fazer Fettucine à carbonara. Não é muito trabalhoso e é uma boa receita, aposto que vão gostar."
    n"Acho que Sabrina reagiu melhor que o esperado, achei que ela não iria me escutar, porém estava mais flexível."
    n"Em menos de uma hora a comida estava pronta e a mesa estava posta, chamo as duas com um grito."
    n"- Garotas, querem comer?"
    show penny_direita
    p"- Sim!"
    n"- Não fiz nada muito elaborado, vamos lá para a mesa."
    n"Sarah e Penny começam a comer rapidamente."
    show sarah_direita
    show sarah_direita at right with move
    sw"- A comida está muito boa, acho que nunca comi algo tão bom na vida."
    p"- Tá uma delicia, vou até repetir!"
    n"Penny se distrai com as panelas e falo com Sarah."
    n"- Vocês não costumam se alimentar sempre?"
    sw"- Não, viver no deserto é não saber o dia de amanhã, comemos quando temos dinheiro ou com sorte nos dão algo. Não vou mentir, sempre roubamos para sobreviver."
    n"-A situação é bem difícil..."
    sw"- Milhares de pessoas passam por isso enquanto outras vivem em lugares como esse!"
    p"- Voltei, melhor vocês irem pegar mais antes que eu coma tudo."
    n"- Fiquem à vontade, eu não preciso comer."
    sw"- Como assim?"
    n"- Eu sou um robô."
    p"- Que foda! Me conta mais sobre como é ser um andróide."
    n"Continuamos a conversa e damos risada de piadas e histórias engraçadas que Penny conta ao longo do jantar, faz algum tempo que não vivo algo assim…"
    jump laboratorio_com_garotas

label laboratorio_com_garotas:
    pause(0.5)
    scene lab with fade
    nar"Laboratórios Linklaster - Andar 78 - 19/08/2699"
    show robo_esquerda
    show robo_esquerda at left with move
    n"Um novo dia começou, eu, Penny e Sarah estamos no laboratório para ver como estamos."
    show samuel_direita
    show samuel_direita at right with move
    n"- Garotas, acompanhem o Samuel, além de cientista, é um ótimo doutor. Vou ser reparada enquanto isso."
    c"- Me sigam."
    hide robo_esquerda with moveoutleft
    hide samuel_direita with moveoutright

    pause(0.5)
    show penny_esquerda
    show penny_esquerda at left with move
    p"- Que lugar incrível!"
    show samuel_direita
    show samuel_direita at right with move
    c"- Temos tecnologia de última geração aqui, querem ver algo?"

    menu tecnologia:
        "Computadores":
            jump pcs
        "Protótipos de robô":
            jump prototipos

label pcs:
    show sarah_direita
    sw"- Quero ver aqueles computadores ali, parecem ser incríveis."
    c"- Eles são os melhores que temos, suportam diversos aplicativos e códigos que precisamos que rodem para o trabalho!"
    p"- Pode me ensinar a mexer neles qualquer hora?"
    c"- Com certeza, você pode trabalhar aqui se Sabrina deixar."
    sw"- Penny, pare de se oferecer!"
    p"- Me deixa, estou gostando desse lugar."
    hide sarah_direita with moveoutright
    hide penny_esquerda with moveoutleft
    hide samuel_direita with moveoutright
    jump exames

label prototipos:
    c"- Aqui temos alguns robôs que estamos trabalhando, nenhum é tão complexo como [nome_robo], mas ainda sim fazem diversas funções."
    show sarah_direita
    sw"- Que surreal, estão testando eles?"
    c"- Sim, eles passam por um longo período de testes para depois serem liberados para uso."
    hide sarah_direita with moveoutright
    hide penny_esquerda with moveoutleft
    hide samuel_direita with moveoutright
    jump exames

label exames:
    show samuel_esquerda
    show samuel_esquerda at left with move
    c"-Vamos fazer os exames!"
    show sarah_direita
    show sarah_direita at right with move
    sw"Enquanto a robô era consertada, fizemos uma bateria de exames para ver se estávamos bem."
    sw"Os resultados saíram rapidamente por causa da alta tecnologia, sofri apenas alguns arranhões."
    sw"Penny passou por um procedimento para higienizar a ferida da perna e fechá-la."
    sw"Samuel e os outros médicos receitaram remédios para ela, as coisas vão melhorar."
    hide samuel_esquerda with moveoutleft
    hide sarah_direita with moveoutright

    pause(0.5)
    scene sala with fade
    nar"Torres Brancas - Andar 83 - 19/08/2699"
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Fomos até o laboratório para fazer um check-up e [nome_robo] se consertar, tudo lá é incrível pra porra."
    sw"Penny pareceu gostar mais do que eu, até mesmo queria mexer nos aparelhos."
    sw"Voltamos para a casa que estamos e ainda não sei quem é a mulher que a robô estava discutindo ontem."
    sw"Conseguimos ouvir tudo, ela não nos deseja aqui."
    hide sarah_esquerda with moveoutleft
    nar"Horas depois..."
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Uma mulher grisalha entra pela sala enquanto assistíamos TV."
    show sabrina_direita
    show sabrina_direita at right with move
    s"- Boa tarde... Vocês são as garotas que foram resgatadas do inferno?"
    show penny_direita
    p"- Oi, me chamo Penny Campbell e agradeço pela recepção."
    hide penny_direita with moveoutright
    sw"- Olá, sou Sarah Winter."
    sw"Não consigo falar muito mais que isso, que mulher imbecil."
    show robo_direita
    n"- Sabrina, voltou cedo."
    s"- Voltei, queria ver se as coisas estavam no lugar."
    n"- Por qual motivo não estariam?"
    s"- Não sei, é preciso tomar cuidado."
    hide sabrina_direita with moveoutright
    sw"A tal de Sabrina cospe a acusação e vai embora."
    n"- Me desculpem, ela pode ser um pouco dura às vezes."
    sw"- Às vezes parece até elogio."

    pause(0.5)
    scene lab with fade
    nar"Laboratórios Linklaster - Andar 78 - 20/08/2699"
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Ando muito estressada, outras pessoas na minha casa me deixam irritada,tenho que me certificar que elas não roubem ou destruam nada."
    s"Enquanto trabalho no laboratório, sinto meu pulso acelerar e minha cabeça e meu corpo doerem demasiadamente."
    s"Meus exames! Eles estão prontos, não sei se devo abri-los..."

    menu exame_pronto:
        "Abrir exames":
            jump exame_aberto
        "Guardar exames":
            jump exame_guardado

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#EXAME ABERTO

label exame_aberto:
    s"Com minhas mãos trêmulas, abro o envelope lentamente..."
    s"- Desconhecido? Não é possível, como assim o que tenho nunca foi listado no banco de dados?"
    s"- QUE INFERNO!"
    cientistas"- Doutora, está tudo bem?"

    menu como_agir:
        "Gritar com funcionário":
            jump gritar
        "Jogar algo na parede":
            jump jogar

label gritar:
    s"- Você aí, vá fazer seu trabalho direito, não se intrometa nos meus assuntos. AGORA!"
    s"- Como são incompetentes, tenho que fazer tudo mesmo, QUE ODIO!"
    s"A porra desses cientistas de merda não servem nem para descobrir o que eu tenho, que bom que me deixaram em paz!"
    s"Preciso fazer tudo sozinha, gastos e mais gastos com estudos para salvar a humanidade e agora quem está doente sou eu."
    s"Após um longo período de reflexão, decido que preciso ir para casa e conversar com a minha amada."
    jump final_exame_aberto

label jogar:
    s"Eu definitivamente estou surtando, preciso extravasar."
    s"Pego um frasco de vidro de cima da bancada e antes mesmo de arremessar ele se parte em pedaços finos e afiados pela minha mão."
    s"O impacto da minha força assusta a todos e os olhares se voltam para mim, saio em passos firmes e rápidos de lá."
    jump final_exame_aberto

label final_exame_aberto:
    hide sabrina_esquerda with moveoutleft
    pause(0.5)
    scene sala with fade
    nar"Torres Brancas - Andar 83 - 23/08/2699"
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Chego em casa e ela parece vazia, acho que estou sozinha. Observo o mar pela janela e ele parece mais escuro e profundo."
    s"- Preciso de um café!"
    pause(0.5)
    scene cozinha with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Mando a máquina preparar um café e o cheiro toma não apenas a cozinha, mas também a casa como um todo."
    s"Esse cheiro me conforta um pouco, mas sinto que preciso tomar uma decisão..."
    s" Sei que da maneira como estamos lidando com os desertos não vamos aguentar muito mais tempo ou manter os níveis de recursos que temos hoje em dia."
    s"Tudo que está acontecendo me incomoda e sinto um leve ataque de pânico se aproximando, o mau pressentimento não é à toa."
    s"- Não consigo aceitar! Por que tudo sempre se volta contra mim?"
    s"Não consigo suportar a ideia de que essa doença foi traga para mim pelas imundas que chegaram a pouco tempo com [nome_robo]."
    s" Mas sei como posso me vingar por isso..."
    s"- Aaaaah é muita coisa para se pensar ao mesmo tempo."
    s"- Preciso me livrar de todos esses desertistas infernais... Eles só me trazem problemas."
    pause(0.5)
    scene escritorio with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s" Começo a escrever uma cartilha sobre como poderíamos acabar com todos os problemas das Torres Brancas eliminando os gastos que temos com os desertistas."
    s" Dessa forma, permaneço em casa por dias finalizando esse projeto."

    pause(0.5)
    stop music
    scene quarto with fade
    play music "audio/suspense.mp3"
    nar"Torres Brancas - Andar 83 - 20/09/2699"
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Os dias continuam passando com uma regularidade disforme. Tenho tido poucos confrontos ultimamente, expondo minha repulsa em meu novo projeto de vida."
    s"A poucos dias atrás, meu projeto foi aprovado pela Cúpula da Terra e será colocado em prática nos próximos meses."
    s"Entretanto, isso ainda é um segredo que ficará guardado entre nós."
    pause(0.5)
    scene tela_final with fade
    pause(10)
    return
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#EXAME GUARDADO

label exame_guardado:
    s"Acho melhor não abrir, eu preciso focar no trabalho, tento tantas coisas pendentes para resolver."
    s"Minha saúde está bem, só estou cansada."
    s"Devo parar por hoje?"

    menu trabalhar_descansar:
        "Ficar e trabalhar mais":
            jump continuar_trabalho
        "Ir para casa":
            jump para_casa

label continuar_trabalho:
    s"Não! Eu preciso entregar alguns relatórios urgentemente, não posso me dar o luxo de deixar nada acumular."
    s"Trabalho até tarde da noite e entrego o que preciso, o que tira meus pensamentos daquele envelope de exames."
    hide sabrina_esquerda with moveoutleft
    jump plano_projeto

label para_casa:
    s"Acho que preciso descansar, sinto meus olhos ardendo de tanto olhar para a tela do computador e minha cabeça latejar, são tantos problemas ultimamente..."
    pause(0.5)
    scene quarto with fade
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"Vou para casa dormir cedo a fim de me sentir melhor, depois me dedico em tempo quase integral a partir de agora."
    jump plano_projeto

label plano_projeto:
    pause(0.5)
    scene sala with fade
    nar"Torres Brancas - Andar 83 - 25/08/2699"
    show robo_esquerda
    show robo_esquerda at left with move
    n"Faz dias que não vejo muito Sabrina, as vezes ela passa aqui para buscar algumas coisas no escritório e vai embora rapidamente."
    n"Eu vou fazer algo que chame a atenção dela o suficiente, quero ver se ela não vai me escutar dessa vez!"
    n"Estou agindo por impulso, mas que se foda."
    n"- Garotas, podem me ajudar com uma coisa?"
    show sarah_direita
    show sarah_direita at right with move
    sw"- Claro!"
    n"Então, arquitetamos todo um plano."
    hide robo_esquerda with moveoutleft
    hide sarah_direita with moveoutright

    pause(0.5)
    show robo_esquerda
    show robo_esquerda at left with move
    n"Mais tarde, quando o laboratório só tem a presença de Sabrina, ligo para ela a fim de começar o que planejamos."
    show sabrina_direita
    show sabrina_direita at right with move
    s"- [nome_robo]? Precisa de algo urgente? Estou ocupada agora."
    n"- Sim, tenho um assunto de última hora para ser tratado, um comandante pediu para responder até amanhã."
    s"- Tudo bem, mas não demore."
    n"- Não! Ele só pode ser tratado pessoalmente."
    s"- Que droga, estou indo aí!"
    hide sabrina_direita with moveoutright
    n"Ligo em seguida para o celular que dei para as garotas."
    show penny_direita
    show penny_direita at right with move
    p"- Tá tudo limpo?"
    n"- Está, ela disse que vai descer, fiquem preparadas para pegar o elevador."
    p"- Certo!"
    hide penny_direita with moveoutright
    pause(0.5)
    n"10 minutos depois, Sabrina finalmente chega em casa."
    show sabrina_direita
    show sabrina_direita at right with move
    s"- O que precisa?"
    n"- Então..."
    hide robo_esquerda with moveoutleft
    hide sabrina_direita with moveoutright

    pause(0.5)
    scene lab with fade
    nar"Laboratórios Linklaster - Andar 78 - 25/08/2699"
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"- A barra tá limpa, vamos entrar."
    show penny_direita
    show penny_direita at right with move
    p"- Vamo no silêncio pra não fazer barulho."
    sw"Entramos no laboratório devagar e procuramos uma maleta prateada."
    sw"Penny retira uma chave e coloca na maleta para termos acesso ao que procurávamos."
    p"-Era isso?"
    sw"-Sim, agora vamos logo, [nome_robo] disse que as câmeras estarão desativadas por meia hora, mas não quero arriscar."
    hide penny_direita with moveoutright
    hide sarah_esquerda with moveoutleft

    pause(0.5)
    scene sala with fade
    nar"Torres Brancas - Andar 83 - 26/08/2699"
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Voltamos depois de meia noite para casa, a robô nos esperava."
    show robo_direita
    show robo_direita at right with move
    n"- Conseguiram?"
    sw"- Sim, está aqui o que pediu."
    n"- Muito obrigada, estou fazendo tudo para chamar a atenção de Sabrina, já que roubar o projeto de minha construção atrapalharia a criação dos novos robôs."
    show penny_direita
    p"- Tá tranquilo, você nos salvou!"
    n"- Meninas, vou ter que pedir uma coisa, agora mesmo quero que voltem para o deserto e levem o projeto, em seguida, enterrem-no em algum lugar."
    sw"- Por que ser tão extrema assim? Não que eu não tenha curtido a ideia, adoraria ferrar toda essa merda de hierarquia, mas por quê?"
    n"- Sabrina não me escuta, só está obcecada com o trabalho sempre, pensei que sumir com o recurso mais valioso do projeto faça ela esquecer isso tudo."
    n"- Tenho como ajudar vocês, arrumarei uma mala com o essencial, como dinheiro e roupas. Pedirei que levem vocês de avião para uma localização secreta."
    hide penny_direita with moveoutright
    hide robo_direita with moveoutright
    hide sarah_esquerda with moveoutleft

    pause(0.5)
    nar"Mais tarde..."
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"A [nome_robo] saiu para pegar umas coisas e nos deixou a sós."
    show penny_direita
    show penny_direita at right with move
    p" - Você acha esse plano uma boa ideia? Não sei, mas tudo já está feito, para onde iriamos?"
    sw"- Não aguento mais viver essa vida de merda, tendo que lutar pra sobreviver. Vamos confiar na robô e ir embora daqui antes que sobre pra gente."
    p"- Tudo bem..."
    pause(0.5)
    nar"Por volta de 21h da noite..."
    sw"Vamos partir agora, estaremos seguras em algum lugar secreto no deserto, estou com medo..."
    show robo_direita
    n"- Estão prontas? \nQuero que vão para o térreo e de lá poderão ver um avião de carga."
    n"A partir de agora, vocês trabalharão fazendo serviços básicos para os militares, não serão nem mesmo identificadas nos sistemas."
    p"- Tem certeza que é seguro?"
    n"- Sim, eles não se importam com ninguém."
    n"- Obrigada pela ajuda, mal nos conhecemos, mas aprendi a ver o mundo diferente."
    sw"- Digo o mesmo, vocês nos deu a chance de viver novamente, obrigada."
    p"- Por mais que aqui seja incrível, talvez nosso destino não seja esse. Tudo que vivemos desde o trem até aqui foi diferente, valeu pela oportunidade!"
    sw"Eu e Penny fomos até o avião e partimos em busca do desconhecido, que esse recomeço deixe todas as dores, desgraças e necessidades para trás..."
    hide robo_direita with moveoutright
    hide penny_direita with moveoutright
    hide sarah_esquerda with moveoutleft

    pause(0.5)
    nar"Torres Brancas - Andar 78 - 27/08/2699"
    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"- [nome_robo], preciso de você, o projeto sumiu, você o pegou?"
    show robo_direita
    show robo_direita at right with move
    n"- Não, eu estava carregando minha bateria, fiquei inconsciente por horas."
    s"- Foram aquelas malditas garotas, eu tenho certeza!"
    n"- Ei, pare de acusá-las, você nem as conhece."
    s"- Nem você."
    n"- Acho que as conheci em dias mais do que te conheço por todo esse tempo. Elas foram embora, está feliz?"
    s"- Se elas não tivessem roubado o projeto sim."
    n"- Para com isso, droga!"
    s"- Como não foram elas? A droga da chave estava aqui em casa e só eu e você sabemos onde está..."
    s"- ESPERA! Você roubou a porra do negócio?"
    n"Acho que eu não tinha saída além de admitir, ela podia ir atrás das meninas e não queria isso."
    n"- Sim, fui eu."
    s"- Por quê? Você me traiu!"
    n"- Você só anda obcecada com essa merda de criar novos robôs, não se preocupa com sua vida? Eu precisava fazer algo."
    s"- Você não devia..."
    n"- Eu cansei de acatar tudo que pede e ter que ver o mundo lá fora desmoronando enquanto não faz nada."
    s"- Está bem, eu entendo o que está dizendo, vem aqui."
    n"Estranho essa reação dela, seus braços abertos e sorriso no rosto, ela me perdoou tão fácil?"
    n"Encaixo minha cabeça em seu pescoço e me aconchego em seus braços. Sabrina passa a mão entre meus fios de cabelo e pousa o polegar na nuca."
    n"Não pode ser, ela vai me deslig-"
    hide robo_direita with moveoutright
    hide sabrina_esquerda with moveoutleft


    pause(0.5)
    play music "audio/suspense.mp3"
    scene lab with fade
    nar"Laboratórios Linklaster - Andar 83 - 05/09/2699"


    show sabrina_esquerda
    show sabrina_esquerda at left with move
    s"- Vamos, continuem estudando os sistemas para podermos obter informações do projeto, temos que prosseguir com as criações."
    pause(0.5)
    scene tela_final with fade
    pause(10)
    return
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#HISTORIA SEM A PENNY

label abandonar_penny_obrigatoriamente:
    menu deixe_penny:
        "Salvar Penny":
            jump penny_abandonada_de_qualquer_jeito
        "Abandonar Penny":
            jump sem_penny

label penny_abandonada_de_qualquer_jeito:
    sw"- Penny, se segura em mim."
    p"- Okay."
    sw"Não conseguia levantá-la, Penny estava bem machucada e sem forças."
    sw"- Vamos, Penny!"
    p"- Eu não consigo, vai logo, você vai ficar para trás!"
    hide penny_direita with moveoutright
    sw"Com medo, fiz o que ela disse."
    jump sem_penny

label sem_penny:
    hide penny_direita with moveoutright
    sw"Meu corpo continuou a se mover sem parar, eu precisava sobreviver custe o que custar, eu prometi para mim mesma."
    sw"Giro meu pescoço para trás e vejo a cena da garota sendo engolida pela tempestade de areia."
    sw"Não tenho tempo para me lamentar e lembrar do passado, sigo em frente com a gana incessante de sobreviver à desgraça que a vida me sujeitou."
    "Corro mais alguns metros de forma desenfreada e sinto minhas pernas falhando."
    sw"- Merda, eu não vou conseguir escapar!"
    sw"Estava prestes a desmoronar no meio do nada e quase não enxergando devido ao excesso de partículas de areia no ar."
    sw"De repente, tropeço em algo enorme, apenas sinto braços luminosos e quentes me abraçarem."
    sw"Em meio ao grande caos barulhento das rajadas de areia me vejo na exaustão completa, não tenho forças para me mover e meus músculos doem."
    sw"A escuridão enfim chega e me percebo em posição fetal como em um grande ventre, enfim apago."
    stop music
    pause(2)
    play music "audio/story time.ogg"
    nar"Algumas horas depois - Localização desconhecida:"
    sw"Acordo com o forte sol em meu rosto e cheia de areia. Há pedaços de imundos por todos os lados..."
    sw"Uma bela moça está deitada ao meu lado e seu corpo ainda meio enterrado na areia, as finas camadas de pó ainda permanecem pelo ar."
    sw"Tenho a sensação de ter sido levada com a tempestade. Lembro de Penny e fico em prantos."
    sw"Não posso ficar aqui chorando, vou ajudar quem me salvou."

    menu verificar_robo:
        "Ver sangramento":
            jump sangramento
        "Verificar pulso":
            jump pulso

label sangramento:
    sw" Um corte profundo em sua coxa já com o sangramento seco envolto em areia úmida trás consigo o que imagino ser uma forte infecção."
    sw"Pego um pouco da água presente no meu cantil, na tentativa de limpar o local da ferida, mas quando a toco, percebo algo estranho."
    sw"Aperto sua pele e parece metal, ela é um robô?"
    sw"Realizo um torniquete bem feito sobre sua coxa com partes de sua armadura para não vazar esse 'sangue'."
    pause(0.5)
    scene tunel with fade
    sw" A carrego até o túnel negro e gelado que abre caminho para o grande trem."
    hide sarah_esquerda with moveoutleft
    jump trem_sem_penny

label pulso:
    sw"O pulso da moça bate muito rápido, ninguém tem a pulsação assim, apenas robôs. Olho atrás de sua nuca e vejo seu número de série HRF - 492."
    sw"Seus cabelos pretos fogem do usual das terras vermelhas, me parece uma viajante distante."
    sw"A pego no colo e com muita dificuldade a passo pelas costas na tentativa de levá-la comigo."
    pause(0.5)
    scene tunel with fade
    sw" A duras penas, alcanço o enorme túnel em que perpassa o trem."
    jump trem_sem_penny

label trem_sem_penny:
    pause(0.5)
    scene tunel with fade
    nar"Grande Trem - A  Caminho das Torres Brancas - 17/08/2699"
    sw"Chego à estação mais próxima e me jogo no chão por não suportar tamanho peso e lá permaneço enquanto percebo minha visão embaçada."
    hide sarah_esquerda with moveoutleft

    pause(0.5)
    nar"Algumas horas depois..."

    pause(0.5)
    play sound "audio/trem.mp3"
    scene grandetrem with fade
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Acordei em uma maca, pelo que vejo estou no grande trem, uma enfermeira faz caminho para o meu quarto."
    sw"-Cadê a moça que salvou a minha vida?"
    sw"Permaneço naquele lugar com uma vista linda pela janela, a pressão da velocidade é tamanha que as vezes parece que vou cair da maca."
    pause(0.5)
    sw"Um pouco mais de duas horas depois que acordo, observo a porta do meu quarto abrindo rapidamente e o ar gelado do corredor entra, escuto uma voz feminina pedindo licença."
    sw"Entra então a humanoide que salvou minha vida, meu coração relaxa e meus batimentos voltam ao normal."
    show robo_direita
    show robo_direita at right with move
    n"-Olá, bom dia Sarah, me chamo [nome_robo], está melhor?"
    sw"- Oi, tô bem melhor sim, foi você quem me salvou né?"
    n"- Sim, isto mesmo..."
    sw"-Hrr... não sei nem o que te dizer, o que fez foi incrível...."
    n"- Só fiz aquilo para o qual fui construída."
    hide sarah_esquerda with moveoutleft
    hide robo_direita with moveoutright

    pause(0.5)
    scene torres with fade
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Em menos de 6 horas sem paradas chegamos em um lugar lindo, que fica em baixo do oceano protegido."
    sw"Aqui o nível de segurança é o maior que eu já vi, ao sair do Trem pareceu que estava sendo acompanhada por alguém importante."
    sw"A robô que me salvou conseguiu furar todas as paradas de segurança apenas com seu nome."
    show robo_direita
    show robo_direita at right with move
    n"- Vou te levar para minha casa até sua melhora, tudo bem? Sei que não tem tido dias fáceis..."
    sw"- Tudo bem, por mim sem problemas.."
    sw"Estou sozinha no mundo, sem ninguém que sentirá minha falta caso eu suma, não pode ser tão ruim ficar num lugar como esse...."
    hide sarah_esquerda with moveoutleft
    hide robo_direita with moveoutright

    pause(0.5)
    scene sala with fade
    nar"Torres Brancas - Andar 83 - 17/08/2699"
    show robo_esquerda
    show robo_esquerda at left with move
    n"- Pode entrar, fica à vontade."
    show sarah_direita
    show sarah_direita at right with move
    sw"- Obrigada."
    sw" Fazemos um tour pela casa e ela me mostra todos os cômodos, aos poucos vejo o mundo incrível de oportunidades que poderia ter aqui."
    n"- Vou precisar atender um chamado do trabalho, volto o mais rápido que der, posso te deixar aqui em casa?"
    sw"- Claro, vai lá."
    n"- Não vou demorar mesmo, só peço que não saia do apartamento! Vou indo, se precisar temos comida na geladeira e no armário."
    hide robo_esquerda with moveoutleft
    sw"A porta principal se fecha, estou livre nessa casa enorme..."

    menu oQueFazer:
        "Andar pela casa":
            jump andar_casa
        "Olhar a vista pela janela":
            jump olhar_janela

label olhar_janela:
    sw"Nossa, quanta água! Acho que nunca vi algo tão lindo na minha vida..."
    sw"Nossa, que fome, acho que vou catar algo pra comer!"
    jump ir_comer

label andar_casa:
    pause(0.5)
    scene quarto with fade
    sw"Corro pelos corredores, subo na cama e pulo sobre ela, bagunçando toda a coberta, minha barriga ronca de fome..."
    sw" Deveria procurar alguma das comidas que a [nome_robo] comentou!"
    jump ir_comer

    label ir_comer:
    pause(0.5)
    scene cozinha with fade
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Abro o armário e tem muita comida aqui, o que eu vou escolher?"

    menu comida_do_armario:
        "Cereal com leite":
            sw"Vou comer cereal. Encontro o leite na geladeira e o pote e colher nos armários depois de muita procura."
            sw"Fazia muito tempo que não escolhia o que comer."
            hide sabrina_direita with moveoutright
            jump sabrina_chega

        "Bolacha de chocolate":
            sw"Nem ferrando! Essa bolacha é muito boa, vou comer o pacote todo."
            hide sabrina_direita with moveoutright
            jump sabrina_chega

label sabrina_chega:
    stop music
    pause(0.5)
    scene sala with fade
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Estava dormindo na sala quando de repente escuto o barulho da porta sendo destrancada."

    menu sabrina_sarah:
        "Se esconder dentro de um armário":
            jump armario
        "Ir para a porta encontrar com a robô":
            jump porta

label armario:
    play music "audio/alarm rythm sinus.mp3"
    pause(0.5)
    scene quarto with fade
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Corro para dentro do quarto que estive mais cedo e me escondo no primeiro armário que vejo..."
    sw"Tá tudo bagunçado... quer quem seja vai perceber minha presença."
    show sabrina_direita
    show sabrina_direita at right with move
    d"- Ai meu deus...Olá? Tem alguém ai?"
    sw"Me mantenho parada forçando uma respiração calma, mas consigo sentir meu coração batendo rapidamente."
    sw"Pelo pequeno espaço vejo uma moça bem vestida e com saltos altos chegando cada vez mais próximo."
    d"-Eu sei que tem alguém aqui! Apareça!"
    sw"Me movo e deixo um pacote cair ao meu lado, fez um puta barulho, fudeu!"
    pause(0.5)
    scene sala with fade
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Saio do armário correndo em direção a porta da sala."
    sw"Quando tento abri-la, ela está bloqueada por um sistema de segurança por íris."
    sw"No final do corredor posso ver a silhueta da então desconhecida..."
    show sabrina_direita
    show sabrina_direita at right with move
    d"- Ai está você! PARADA! Como foi que entrou aqui?"
    jump sabrina_descobre_sarah

label porta:
    play music "audio/alarm rythm sinus.mp3"
    sw"Aguardo para ver [nome_robo] entrar, mas na verdade dou de cara com outra mulher que enlouquece ao me ver."
    jump sabrina_descobre_sarah

label sabrina_descobre_sarah:
    d"- QUEM É VOCÊ?"
    sw"- Calma! Calma! Não é o que você tá pensando!"
    d"- Como você entrou aqui na minha casa? Que absurdo sem cabimento."
    sw"Ela retira de sua bolsa uma arma e a aponta para mim."
    sw"- Não, calma! Sou uma amiga da [nome_robo]!"
    d"- Nem morta que eu vou acreditar numa merdinha como você! Anda, coloca a mão na cabeça que eu já acionei a polícia."
    d"- Eu não acredito que uma imbecil como você conseguiu chegar até aqui sem ninguém perceber...."
    sw"Começo a chorar, não acredito que a robô armou para mim, me trouxe para casa de uma desconhecida dizendo ser sua."
    sw"Como a vida pode ser tão cruel comigo?"
    sw"Duas sentinelas policiais me arrastam e me batem com força na nuca."

    menu reacao:
        "Gritar":
            jump grito
        "Se manter calada":
            jump silencio

label grito:
    sw"As sentinelas liberam seus pulsos elétricos em mim e caio no chão sem forças para continuar..."
    jump prisao_dos_esquecidos

label silencio:
    sw"Vejo a mulher de cabelos curtos e brancos que chamou a policia ligando para alguém... Espero que seja a robô e não mais sentinelas."
    sw"Me mantenho calma e busco respeitar as ordens dessas sentinelas fudidas!"
    jump prisao_dos_esquecidos

label prisao_dos_esquecidos:
    play music "audio/alarm rythm sinus.mp3"
    sw"Aos poucos, bloqueiam minhas mãos, pés, olhos e boca..."
    sw"Me colocam na viatura aquática que imagino ter como sentido a prisão dos esquecidos."

    pause(0.5)
    scene prisao with fade
    nar"Prisão dos Esquecidos - No meio do nada - ??/08/2699"
    show sarah_esquerda
    show sarah_esquerda at left with move
    sw"Me lançam com força para dentro da minha nova cela, sem muitos olhares me torno mais uma no meio delas."
    sw" No canto do lado esquerdo consigo ver uma garota com os cabelos cobrindo o rosto que me lembraminha melhor amiga..."
    sw"Acabo caindo em lágrimas novamente... Vou ao encontro da garota."
    sw"- Penny...?"
    sw"A garota até então desconhecida levanta o rosto e me dou conta que realmente é a Penny."
    show penny_direita
    show penny_direita at right with move
    p"- AAAAA não acredito! É você mesmo!"
    sw"Nos abraçamos com força e no calor de seus braços me mantenho como nunca antes..."
    sw"Achei que nunca mais fosse sentir seu calor novamente."
    sw"- Me desculpa por não te salvar, agora estou aqui com você nesse inferno."
    sw"Ela toca o Band-aid que coloquei na minha testa, onde as sentinelas bateram dias antes."
    p"Tá tudo bem, eu te perdoo, somos só eu e você nesse mundo, não podemos brigar."
    sw"Caímos em lágrimas novamente, mas ainda sim havia felicidade em mim por reencontrá-la."
    sw"Naquela noite, fizemos uma promessa de nunca mais nos desgrudarmos."
    sw"Fazendo uma refeição, nossas lágrimas dão abertura à uma lembrança constante da ameaça mortal que está logo ali fora."
    pause(0.5)
    scene tela_final with fade
    pause(10)
    return








#
