# V0.11 R2 — desempenho e Content

Meta do projeto: mínimo de 40 FPS (25 ms/quadro), alvo de 60 FPS (16,7 ms/quadro), saída da TV em 1920×1080. A meta é um critério de validação, não uma garantia no Wii U físico.

## Mudanças

- Cache limitado a 160 blocos de 64×64 pixels, com descarte dos blocos menos usados. Guarda apenas terreno, primeiro plano, profundidade e máscara de água do Content. Animações, personagens, plantações e chuva continuam dinâmicos.
- Desenho apenas da câmera do mapa atual. Os NPCs fora dela mantêm suas rotinas; NPCs parados visíveis continuam aparecendo. Plantações fora da câmera não geram sprites.
- Preparação de até dois blocos por quadro perto de portas e transições, priorizando a região de chegada. A margem do mapa atual aumenta com a velocidade observada. Durante transições solicitadas, a chegada é priorizada. Se um bloco ainda faltar, ele é preparado antes de ser desenhado, sem buracos visuais.
- Os mapas brutos já estão embutidos em RAM nesta arquitetura. Isso é cache e preparação do desenho, não streaming de mapas a partir do SD. Viagens por carrinho, montaria e teletransporte ainda dependem da implementação dessas mecânicas; não são anunciadas como concluídas.
- Interface: coordenadas de amostragem calculadas uma vez por coluna/linha, cópia de imagem sem divisões no caso 1:1 e ampliação inteira do mundo por duplicação de pixels. A saída Full HD e os pixels originais são preservados.
- Inventário independente do GamePad reaproveitado enquanto itens, quantidades, seleção, capacidade, dinheiro, ganhos e data não mudarem. TV e GamePad permanecem independentes.
- Iluminação de noite e chuva usa tabelas dos mesmos cálculos de cor, invalidadas quando o ambiente muda. Nenhuma filtragem de cor em dia claro sem chuva.
- Carro do Lewis: 28 tiles originais do Town, com profundidade ancorada no fim do veículo (1376), sem herdar a cerca logo abaixo; 2756 pixels de profundidade corrigidos. A arte não foi alterada.
- Culinária: 81 registros originais de Data/CookingRecipes, 80 resolvidos pelo catálogo atual. Nove tiles `Action=kitchen` das casas melhoradas abrem a página. Ovo frito é a receita inicial e usa a categoria de ovos original. Consumo e resultado são atômicos. Receitas de cartas/TV/lojas permanecem bloqueadas enquanto o mecanismo real de aquisição não existir. Uso de geladeiras, tempero Qi, progresso de culinária e desbloqueios completos ainda não foram implementados.
- Save separado `stardew_wiiu_v011r2.sav`, com importação da R1 e versões anteriores. Sem alteração do formato binário do save.
- Medição no log: `PERF` informa microssegundos por etapa, pior quadro e quantidade acima de 25 ms em cada janela de 60 quadros. Não adiciona tutorial ou texto sobre o jogo.

## Limites

Não foi validado no Wii U físico. O relatório de desempenho diferencia médias de quedas pontuais. Emulador, processador e driver influenciam os resultados. VisibleFish continua parcial, assim como na R1. Nenhuma arte foi gerada; as adições de conteúdo vêm dos arquivos fornecidos.

Veja `TESTES_V011R2.txt` e `evidencias` para a validação desta compilação.
