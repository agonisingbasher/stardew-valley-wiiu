# V0.11 R2 — 25/10/2026

Cache por região e preparação de chegada; inventário GamePad por alteração; UI e iluminação otimizadas; correção da profundidade do carro do Lewis; culinária do Content nas cozinhas melhoradas; medição por etapa. Meta 40–60 FPS em validação. Fonte e executáveis no mesmo ZIP. Detalhes em COBERTURA_V011R2.md.

# V0.11 R1 — 25/10/2026

Apresentação Full HD corrigida e verificada no Cemu 2.6, saída independente para GamePad; partículas originais do lixo; interação por tile à frente; esgotamento diário de falas; divisórias/ícones de amizades; habilidades e fabricação com Content; 286 ações originais de mapas; distribuição de peixes por toda a água e port parcial identificado de VisibleFish. Novo save R3 com migração. Entrega padrão unificada: fonte e RPX no mesmo ZIP. Detalhes e limites em COBERTURA_V011R1.md.

# V0.11 — 24/10/2026

Apresentação GX2 sem substituir scan buffers; Gus por proprietário da loja; profundidade de balcões separada de bancos; jukebox sem duplicação; cartas originais paginadas/indicador; remessas em 12 colunas; 3 casas com camas contidas e móveis originais; ícones alinhados; 16 poças e som de água; atlas de peixes corrigido (passo vertical48), 71 definições/25 espécies externas, algas/lixo; pássaros/coelhos; partículas do lixo; heavyEngine/tubo/fumaça originais do ferreiro; 83 variantes WAV embutidas; migração para save V0.11. Veja COBERTURA_V011.md. Sem execução do Cemu/Wii U nesta sessão.

# V0.10 revisão 2 — 24/10/2026

Resolução com escala inteira nas duas saídas de TV; superfícies/sons originais; paredes; moradores; tampa do lixo; aceitação de pedidos; calendário; palavras da loja; moldura e sobreposição de erros; MoneyDial e G; ganhos com categorias/detalhes; pesca com dados/sprites originais; jukebox e 74 variantes de áudio embutidas. Catálogo e pacote integral dos 3.556 arquivos Content. Detalhes e limites em COBERTURA_V010R2.md.

# V0.10 revisão 1 — 24/10/2026

Correções de ouro/ponteiro, cama e tela de remessas, ferramentas reais e entrega da vara, transições/portas/passos, calendário original e pedidos, lixeiras, retratos/loja, sombras e campo de visão. Oito cenários de festivais e adaptação parcial dos mods recebidos. Detalhes, testes e limites em COBERTURA_V010R1.md. Save novo preserva V0.10.

# Histórico de versões

Este arquivo reúne os updates entregues nesta conversa. A partir da v0.4, cada pacote deve atualizar este histórico, o README, o roteiro de teste e o manifesto de compilação. As versões anteriores já tinham documentação própria; o histórico consolidado começa nesta entrega.

## v0.1 — Base de exploração

- Inventário dos recursos recebidos e seleção da fazenda, seus quatro tilesets e sprite temporário.
- Conversão dos XNB selecionados com xnb.js e leitor próprio do formato tBIN10.
- Reconstrução da fazenda de 80 × 65 blocos e seis camadas.
- Movimento, animação de Abigail como avatar temporário, câmera e colisão aproximada.
- Visualização no navegador e simulação de TV/GamePad com alternância mapa/jogo.
- Núcleo C++ de exploração e renderer OSScreen em duas telas.
- Primeiro RPX compilado com devkitPPC/WUT e instruções para o Cemu. Corrigida a ligação de WHB: integrada à libwut usada na compilação.
- Sem construções dinâmicas, vegetação gerada, agricultura, áudio ou salvamento.

**Validação:** testes do núcleo e interface simulada; usuário confirmou execução correta no Cemu.

## v0.2 — Estruturas e controles

- Casa inicial, estufa em ruínas, caixa de remessa e correio nos pontos de referência do código fornecido.
- Colisão conservadora das quatro estruturas e posição inicial diante da casa.
- Ordem de desenho das estruturas em relação ao avatar.
- Caminhada com inclinação leve do analógico; corrida com inclinação forte/direcional; A segurado força caminhada.
- Relação corrida/caminhada de 5/2, ou 2,5×. Zona morta radial e diagonais normalizadas.
- Movimento convertido à escala dos tiles nativos, inicialmente 33/82,5 pixels por segundo.

**Retorno do usuário:** telhado atravessado pela cerca, tampa de remessa faltando e percurso mais rápido que no jogo original. Esses pontos foram tratados na v0.3.

## v0.3 — Profundidade, tampa e calibração

- Correção da cerca sobre o telhado: profundidade por pixel para Front e composição ordenada com casa/avatar. AlwaysFront mantém prioridade alta.
- Faixa original de 13 frames da tampa de remessa integrada; abertura por aproximação e fechamento ao afastar-se.
- Velocidade multiplicada por 2/3 conforme a comparação do usuário: 2 s no protótipo versus 3 s no original.
- Novas velocidades de 22/55 pixels nativos por segundo, mantendo a relação 2,5×.
- Testes do cruzamento real casa/cerca, calibração de deslocamento e ciclo da tampa.

**Validação:** compilação e testes passaram; usuário aprovou a versão como perfeita. Não foi realizado teste no Wii U real.

## v0.4 — Mundo conectado e vegetação

- Nove cenários: Fazenda, Ponto de ônibus, Vila Pelicanos, Floresta, Caminho dos fundos, Montanha, Praia, Caverna da fazenda e Casa inicial.
- Camadas Back adicionais e Buildings adicionais dos mapas expandidos renderizadas; exteriores de casas, lojas e outras construções presentes nos mapas incluídos.
- 185 árvores e 403 pontos de grama, nas posições dos marcadores Paths 9/10/11/22 dos mapas enviados; três espécies de árvores e grama de primavera.
- Troncos com colisão; vegetação estática composta por profundidade. A grama é caminhável e ainda não possui corte, crescimento ou redução de velocidade.
- Passagens entre regiões selecionadas a partir das propriedades Warp. Saídas cujos destinos não estão nesta lista não foram habilitadas.
- B entra/sai da casa inicial e da caverna; a casa ainda está sem mobiliário e sem funcionalidades.
- L/R selecionam regiões para inspeção rápida; Y continua alternando mapa/jogo na segunda tela; X reposiciona na entrada atual.
- Câmera, colisão e limites passam a considerar as dimensões de cada mapa. Pontos de chegada são ajustados à célula caminhável mais próxima, quando necessário.
- Intervalo de proteção entre transições para reduzir retornos involuntários.
- Mapa geral no GamePad acompanha a região atual.
- Atlas estático de nove mapas em preview/index.html. O RPX passa a ser a interface de exploração desta versão; o antigo protótipo HTML de movimento permanece nos pacotes anteriores.
- Histórico consolidado, roteiro de teste, manifesto da compilação e pipeline reproduzível com os dois ZIPs de recursos.
- Testes de dimensões, posições de chegada, detecção de portais e navegação do conjunto de nove cenários desde a fazenda.

**Validação desta entrega:** testes e compilação para PowerPC. A execução da v0.4 no Cemu ainda precisa de validação pelo usuário. Sem teste no Wii U real.

## Ainda não implementado

Fazendeiro personalizado, NPCs/rotinas/diálogos, agricultura, ferramentas, inventário, remessa de itens, salvamento, áudio, relógio/estações, eventos, progresso de desbloqueios e a maioria dos interiores. A montagem dos mapas não equivale a um port completo do jogo. O renderer continua por software e ainda não há comprovação de 60 FPS.


## v0.5 — Bases das árvores, vegetação e sobreposição

**Retorno sobre a v0.4:** bases das árvores ausentes, objetos de vegetação faltando, personagem aparecendo inteiro sobre cercas/canteiros/postes conforme a aproximação, grama isolada em tufos separados.

- Inclusão do recorte de base/raízes das 185 árvores adultas (16 × 32 em x32/y96 da textura original), combinado com a copa.
- Grama reconstruída com quatro tufos por célula, variação de sprite, espelhamento e deslocamento determinístico: 403 áreas, 1.612 tufos. A composição representa grama madura e une visualmente áreas vizinhas; não reproduz um salvamento específico.
- 1.691 objetos adicionados a partir dos marcadores Paths: arbustos, ervas daninhas, pedras pequenas, galhos, mudas, tocos, troncos e pedras grandes. Recortes das texturas springobjects e bushes dos arquivos enviados.
- Buildings sólidos deixam de ficar fixos no chão; entram na composição com profundidade. As faixas verticais de Front/Buildings compartilham a profundidade da base, evitando alternância por pedaço do objeto. Faixas horizontais não são agrupadas, preservando o cruzamento cerca/telhado da fazenda. Passable e AlwaysFront mantêm tratamentos próprios.
- Origem vertical do avatar ajustada em quatro pixels: a extremidade dos pés coincide com a borda inferior usada pela colisão.
- Novos objetos recebem colisão; entradas e destinos são ajustados após a montagem da vegetação. Os nove cenários continuam conectados.
- Histórico, instruções de conversão com o terceiro arquivo, roteiro de teste e manifesto atualizados.

**Validação:** testes de movimento, colisão, tampa, sobreposição real da cerca pelos dois lados, canteiro/poste, telhado da casa, portais e acesso aos nove mapas passaram. Teste dos recursos confirmou raízes na imagem final, 1.612 tufos e 1.691 objetos com colisão. Compilação devkitPPC/WUT e leitura do RPX com readrpl concluídas. Teste no Cemu pendente do usuário; Wii U real ainda não testado.

**Limites:** não há interação/corte/crescimento dos novos objetos nem reprodução do estado aleatório de uma partida. A colisão continua por tiles e a profundidade usa faixas verticais; conjuntos complexos ainda podem precisar de ajustes específicos após inspeção no Cemu. Mantidos os nove mapas da v0.4, sem novos interiores nesta versão.


## v0.6 — Leah e cenário animado

**Retorno sobre a v0.5:** usuário aprovou o resultado e pediu reação da grama, ônibus, efeitos do ferreiro, chuva com poças/reflexo, peixes por estação/local e Leah como avatar.

- Abigail substituída por Leah; a folha original de quatro direções é utilizada, incluindo o reflexo da animação atual.
- Os 1.612 tufos passam da imagem estática para sprites dinâmicos. Contato do personagem aciona inclinação e retorno amortecido, sem duplicação da grama antiga.
- Ativadas 2.288 posições de tiles animados a partir dos frames/repetições/intervalos do tBIN, além de brilho discreto da água.
- Ônibus original integrado com colisão e porta de seis frames por aproximação. Posição obtida do NPCWarp do mapa recebido para compensar diferença em relação ao código de referência 1.5.6. Não implementada viagem ao deserto.
- Tampa frontal da máquina do ferreiro vibra sobre a imagem estática com profundidade correta; fumaça sobe/expande/desaparece na saída superior e no carrinho próximo. Efeitos visuais habilitados nesta demonstração, sem progressão de missões.
- Chuva visual, escurecimento do ambiente e 438 pontos de poças em terra/pedra livres nos cenários externos. Formação/secagem gradual, reflexo vertical da Leah com ondulação, máscara restrita à água e ondulações por passos.
- 17 espécies visuais de peixes. Habitats separados para rio da vila, rio/lago da floresta, lago da montanha e oceano. Filtros conjuntos de estação, clima e horário; nado limitado à água, cauda animada e reação de velocidade à aproximação. Sem pesca ou importação do mod de PC.
- − alterna chuva; ZL alterna estação da fauna; ZR altera horário; R3 percorre pontos de inspeção. Configuração inicial: primavera, 12:00 e sol. Cenários ainda usam as texturas de primavera.
- Renderizador portátil compartilhado com testes; composição por profundidade dos elementos estáticos/dinâmicos e reaproveitamento do quadro entre as telas no modo jogo. Mapa geral usa miniaturas com vegetação e ônibus.
- Mantidos os nove cenários, as raízes, os 1.691 objetos, velocidades 22/55 px/s, passagens e tampa da remessa.

**Validação:** testes do núcleo, compositor, mundo e recursos; verificações do renderizador real para grama/retorno, ônibus/porta, fumaça/tampa, reflexo/ondulações, chuva em interiores, cerca e telhado. Avaliadas 640 combinações de mapa/estação/clima/horário e trajetórias aquáticas. Imagens de conferência produzidas no computador, não no Cemu. Compilação RPX e verificação de formato registradas no manifesto da entrega.

**Limites:** fauna contém a seleção documentada, sem tabela completa de Data/Locations 1.6; estações controlam a fauna, sem troca visual integral dos mapas. Clima e horário são de teste, sem calendário/salvamento. Sem áudio dos efeitos, agricultura, inventário ou novos interiores. Execução no Cemu e no Wii U real pendente.

## v0.7 — Interiores, moradores e início da partida

- Mundo ampliado de 9 para 48 cenários; 35 ações de entrada de locais e 28 portas internas animadas.
- 34 NPCs com sprites/retratos, 2.236 registros de diálogo em português, 398 variantes de agenda e 191 textos de agenda. Arquivo integral para consulta e interpretador inicial de rotinas normais, caminhos e poses.
- Conversar/presentear, corações, quartos com dois corações e acesso compartilhado/permanente; horários de fachadas e condições especiais de algumas entradas.
- Inventário de 12 espaços, 27 tipos de itens, contador de dinheiro, calendário/relógio e barras de energia/vida. Barras ainda sem ferramentas/combate para consumi-las.
- Remessa com A, envio de unidade/pilha, recuperação do último depósito e pagamento único no dia seguinte.
- Coleta diária por estação/região, respeitando colisão/capacidade do inventário e pontos já recolhidos no save.
- Sono/desmaio, passagem do dia, obras em três dias, três melhorias de casa, interiores ampliados, móveis básicos e porão. Materiais ainda parcialmente dependentes do laboratório.
- Salvamento próprio com checksum e escrita temporária, condicionado à montagem do SD. Carregamento restaura sistemas da partida e reinicia posição na fazenda.
- Peixes com oito direções e curvas, exclusão da cachoeira e verificação do corpo contra margens; corrigido caso de centro do peixe entrar em uma borda irregular.
- Apresentação principal migrada para GX2 com espera da troca de quadros; passos de simulação fixos e arredondamento consistente de câmera/avatar. RPX OSScreen alternativo para compatibilidade.
- 202 árvores, 1.751 objetos, 1.612 tufos de grama, 2.382 posições de tiles animados e 607 pontos de poças nos mapas ampliados.
- Roteiro Cemu, matriz de cobertura, dados importados, prévias reais do renderer portátil e documentação de reprodução atualizados.

**Validação:** compilação PowerPC dos dois backends, verificação de RPX, testes portáteis do núcleo/render/world/assets/effects/life. Simulação de segunda-feira com 28 NPCs em deslocamento; inventário, remessa, pagamento único, obras, calendário, checksum, quartos, coleta persistente e limites da fauna exercitados. Cemu e hardware real ainda pendentes de execução nesta entrega.

**Limites:** importação integral dos dicionários selecionados não representa implementação de todos os eventos. Casamento, festivais, missões, agricultura, áudio, mineração completa e condições especiais de todas as rotinas continuam pendentes. As texturas do cenário permanecem na primavera; calendário altera fauna/coleta/agendas. O estágio atual está detalhado no README e em COBERTURA_V07.md.

## v0.8 — Interface original, colisão, bancos e noite

- Substituída a fonte DejaVu pelos glifos do Content. Molduras, slots, barra, abas, relógio, clima/estação, dinheiro e indicador de energia usam as texturas originais. Removido o painel “Leah”. Inventário em doze colunas/três linhas, com as linhas adicionais bloqueadas.
- Corrigidas direções 0/2 das agendas e o alinhamento vertical dos sprites. No interior, profundidade por linha evita balcões/prateleiras encobrindo moradores indevidamente.
- Mensagens de quartos mostram o proprietário, sem título genérico. Nomes são localizados com Strings/NPCNames.pt-BR.
- Jogador e moradores ganham colisão; NPC bloqueado aguarda, treme, mostra expressão e depois atravessa acelerado, sem reduzir amizade. Construções colocáveis/destruíveis ainda não existem.
- Corrigidos pontos de assento, aplicação de poses ao chegar e combinação pose/fala; Maru e Penny apoiadas no banco.
- Adicionada interação de sentar/levantar para jogador, com ocupação e saída segura. Data/ChairTiles fornece os bancos e outros assentos nos mapas; 53 lugares de banco passaram nos testes, de um conjunto de 275 lugares importados.
- Noite contínua por estação, 229 mudanças de tiles de dia/noite e 111 fontes de iluminação dos mapas. Luzes aplicadas ao cenário/personagens antes da interface; máscara calculada somente nos limites visíveis dos focos.
- Relógio vermelho/emote de sono, bloqueio de controle às 02h, queda adaptada da Leah, fade, resgate, retorno perto da cama e penalidades corrigidas: sem taxa em casa, limite de 1.000g fora e energia anterior preservada quando maior que a recuperação.
- Save mantém formato V0.7 e tenta copiá-lo ao iniciar V0.8 quando o arquivo novo não existe. Originais não são apagados.
- Dois RPX, recursos/fontes/nomes rastreáveis, roteiro, cobertura e prévias do renderer atualizados. A execução no Cemu e no Wii U real permanece pendente de conferência externa.


## v0.9 — Agricultura sazonal, regador e economia inicial

- Ciclo agrícola expandido para seis culturas: chirívia (4 dias), batata (6) e couve-flor (12) na primavera; melão (12) no verão; abóbora (13) no outono; melão-poeiro (7) no inverno. Cada cultura tem metadados para semente, produto, estação, crescimento e custo.
- O melão-poeiro foi adicionado com base nas páginas da Wiki de Stardew Valley 1.6. Como o jogo original usa chaves textuais para esse objeto e semente, os IDs internos 9000/9001 são aliases locais do protótipo, não IDs numéricos oficiais.
- Atlas agrícola com 24 quadros (quatro estágios compactos por cultura) e atlas de itens com 38 slots, sem deslocar os índices antigos. Solo arado continua renderizado como ator dinâmico por profundidade.
- Regador com 40 unidades, decremento por rega, bloqueio quando vazio, indicador no HUD e reabastecimento ao pressionar A perto da água da fazenda. Arar/regar consomem 2 de energia; regar consome também 1 unidade.
- Loja de Pierre sazonal: chirívia/batata/couve-flor na primavera, melão no verão (80g) e abóbora no outono (100g). O melão-poeiro não está disponível para compra por ouro, conforme a Wiki.
- Semente de melão-poeiro acessível através de um ponto sazonal na Floresta no dia 9 do inverno, posicionado em (18,18). A implementação representa o ponto como pickup e não como solo a cavar com a enxada, o que segue como melhoria futura.
- Batata pode fornecer colheita extra com aproximação determinística baseada em save/dia/terreno; não corresponde ao algoritmo completo de sorte diária do jogo original.
- Sidecar agrícola v2 mantém o layout do `SaveData` legado intacto; leitura de sidecar v1 continua suportada. Testes incluem checksum inválido, estado inválido, seis ciclos de crescimento, chuva, colheita, loja sazonal e fonte de semente do inverno.
- Pipeline de atlas repetível em `tools/build_farming_assets.py`; testes de regressão e prévia do renderer portátil atualizados.

**Validação local:** `bash tools/test_release.sh` passou: core, render, world, effects, life, farming e assets. Foram testadas as seis culturas, os preços e filtros de estação da loja, o pickup sazonal, o tanque de água e o round-trip do sidecar.

**Limites:** o toolchain devkitPPC/WUT não está instalado neste ambiente, portanto um novo RPX v0.9 não foi compilado. Os RPX incluídos em `executavel/referencia_v08/` continuam sendo v0.8 e não contêm estas alterações. Execução no Cemu e Wii U real ainda pendente. Permanecem fora do escopo ferramenta/enxada real para Seed Spots, ferramentas separadas/animadas, upgrades do regador, qualidade, fertilizantes, XP de cultivo, culturas extras, lavoura gigante e sorte original completa da batata.


## v0.9.3 — Culturas de colheita repetida

- Incluídos mirtilo (Verão; 13 dias até a primeira colheita; 3 frutos base; recresce em 4 dias irrigados) e oxicoco (Outono; 7 dias; 2 frutos base; recresce em 5 dias irrigados).
- O catálogo de Pierre passou a mostrar ambos os cultivos nas estações corretas, por 80g (mirtilo) e 240g (oxicoco).
- A colheita agora consulta os metadados de rendimento-base, período de recrescimento e limite de frutos extras. Plantas de colheita repetida permanecem no terreno; o contador regride para o próximo ciclo sem exigir novas sementes.
- Slots 38–41 foram anexados ao inventário para os dois produtos e sementes, preservando todos os índices legados. O atlas agrícola passa a 32 quadros (512×16); o atlas de itens passa a 42 slots (672×16).
- Os testes de host cobrem crescimento, primeira colheita, recrescimento, segunda colheita, preço/estação da loja, assets e regressão dos sistemas antigos.

**Validação local:** `bash tools/test_release.sh` passou para core, render, world, effects, life, farming e assets. Os sprites são arte procedural de protótipo e os extras da colheita usam uma aproximação determinística, não toda a lógica original de sorte diária.

**Ainda pendente:** RPX v0.9 compilado (devkitPPC/WUT ausentes neste ambiente), execução real no Cemu/Wii U, arte oficial completa de todos os estágios e implementação integral de fertilizantes, qualidade, XP e ferramentas.


## v0.9.4 — Seed Spot de inverno por ferramenta contextual

- O marcador sazonal de sementes de melão-poeiro agora é desenhado como um ponto de solo próprio em vez de um pacote de semente no chão.
- O alvo está na Floresta, tile (18,18), no dia 9 do inverno; o jogador fica um tile ao norte, aponta para baixo e pressiona Y. A interação gasta 2 pontos de energia, entrega uma semente e grava o slot diário em `save.collected`. Pressionar A não coleta o ponto.
- O pacote agrícola preserva o layout legado e usa o slot sazonal apenas como registro de disponibilidade diária, de modo que o ponto não reaparece após uma atualização de lista no mesmo dia.
- Atlas de solo agora tem 48×16 pixels: solo arado seco, solo molhado e marcador Seed Spot.

**Validação local:** `bash tools/test_release.sh` passou para todos os testes normais do host, incluindo direção, energia, inventário, persistência diária e proibição de coleta com A. RPX v0.9 e execução no Cemu continuam pendentes por indisponibilidade do toolchain devkitPPC/WUT.

## v0.9.5 — sprites originais, Carpintaria e correio nativo (sprint 09b)

- Corrigida a direção de fidelidade visual: os atlas agrícolas sintéticos da etapa inicial foram removidos. A renderização aponta para as folhas originais de cultivos (256×832) e solo arado (192×192) que já estavam nas referências do projeto. A PNG do strip de ícones permanece intocada; posições sem sprite original ficam transparentes em vez de receber desenhos.
- Catálogo nativo de cultivos ampliado/estabilizado em 51 definições sazonais/especiais, sementes silvestres e fibra. As culturas novas apontam para quadros da folha original. Fontes de semente fora de Pierre, árvores frutíferas, fertilizantes/qualidade/XP e alguns sistemas da 1.6 seguem pendentes.
- Integrada a Carpintaria da Robin: 15 construções, seleção, validação da área, custo só após confirmação, colisão persistente, upgrades e tempo de obra por dias. O estado é salvo em `.buildings`; a representação de posicionamento usa somente contorno de UI, pois não há uma folha original identificada de todos os edifícios.
- Implementado o menu de correio na pausa e o sidecar `.mail`: 69 registros resumidos, cartas em datas do Ano 1/2, lembretes anuais, gatilho de evento, condição limitada do poço, marcação de leitura e teste de checksum. A lista não é ainda a cobertura completa de todas as cartas, gatilhos, anexos e recompensas do jogo original.
- Removida a gravação automática de imagens nos testes. Nenhuma imagem nova foi criada nesta revisão e não há diretório de prévias no pacote.
- Testes locais aprovados: `bash tools/test_release.sh` (core, render, world, effects, life, farming, buildings, mail e assets) e `python3 tools/test_content_catalogs.py` (51 culturas, 15 construções, 69 registros de correio).
- **RPX v0.9 ainda pendente:** esta é uma entrega de código-fonte; o usuário compilará com devkitPPC/WUT. Cemu e Wii U físico ainda não foram validados.

## V0.9 final — 24/10/2026

- Consolidação do sprint09b com auditoria por Content/folhas originais; 288 referências preservadas com hashes.
- 137 ícones originais, fonte 8×16, texto real de cartas, fases/endereços corretos das lavouras e construções com exteriores originais.
- Retirados corpo misto Leah/Maru, queda inventada e atlas deformado de peixes; efeitos experimentais fora da apresentação padrão.
- Abas funcionais, compra de mochila, fileiras, diário, opções de telas, Pro/Classic via KPAD, cursor e toque.
- Saída principal GX2 solicitando TV 1920×1080 e GamePad 854×480; compat 720p ocupa a tela.
- Coleta regional com máscara original e persistência, ponto de sementes no Caminho dos Fundos e correções de profundidade junto à água/cercas.
- Compatibilidade do save legado; lavoura v3 preserva regeneração e importa v1/v2.
- RPX principal/compat compilados com devkitPPC/WUT. Testes host e sanitizadores constam no TESTS_LOG; execução no Cemu/console e FPS ainda não validados.
- AUDITORIA_V09 e COBERTURA_V09 explicitam funcionalidades parciais; esta é a versão final da etapa, não o jogo completo.


## V0.10 — 24/10/2026

Fonte proporcional e números originais, nova composição de inventário/relógio, compra das mochilas na exposição do Pierre, importação dos 77 catálogos de lojas, transações/estoque condicional, gato preto e animais com A* incremental, árvores frutíferas, vento/nuvens, peixes originais e reflexos, protótipo Junimo Kart, opções de HUD/GamePad e áudio XACT original (463 samples/433 cues; 41 variantes embutidas). Principal e compat compilados. A cobertura permanece parcial conforme COBERTURA_V010.md; não foi executado em Cemu/Wii U nem medido fps.
