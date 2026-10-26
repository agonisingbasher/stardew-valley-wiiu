# 🌱 Stardew Valley — laboratório experimental para Wii U

**Wii U Homebrew · C++ · GamePad · Cemu · V0.11 R2**

> **Protótipo nativo, não um port oficial nem o jogo completo.** O laboratório estuda como Stardew Valley pode aproveitar a TV Full HD e o GamePad do Wii U. A **V0.11 R2** (25/10/2026) adiciona cache por região, UI/iluminação otimizadas, correção do carro do Lewis, culinária original parcial e medições de desempenho no Cemu 2.6.

## 🌐 Página do projeto

**[agonisingbasher.github.io/stardew-valley-wiiu](https://agonisingbasher.github.io/stardew-valley-wiiu/?lang=pt-BR)** — estado atual, capturas do Cemu, tabela de FPS e documentação da R2 (PT-BR / EN).

O preview no navegador (`preview/index.html`) permanece a **demo antiga da v0.1** e **não** representa a R2. A R2 roda como RPX no Cemu / Wii U.

## 🎯 V0.11 R2 em resumo

- Cache limitado a 160 blocos 64×64 (LRU); desenho só da câmera; preparação de chegada perto de portas/transições.
- TV 1920×1080 via GX2; GamePad independente; inventário do GamePad reaproveitado até mudar.
- Iluminação de noite/chuva por tabelas; sem filtro de cor em dia claro sem chuva.
- Carro do Lewis: profundidade corrigida (2.756 px) sem herdar a cerca.
- Culinária: 81 receitas originais (80 resolvidas); nove cozinhas de casas melhoradas; ovo frito inicial.
- Save `stardew_wiiu_v011r2.sav` com importação da R1 e anteriores.
- Entrega padrão: **um ZIP** com `executavel/` + `fonte/`.

Detalhes: [`docs/COBERTURA_V011R2.md`](docs/COBERTURA_V011R2.md) · [`docs/DESEMPENHO_V011R2.md`](docs/DESEMPENHO_V011R2.md) · [`docs/HISTORICO_VERSOES.md`](docs/HISTORICO_VERSOES.md) · [`docs/ENTREGA_PADRAO.md`](docs/ENTREGA_PADRAO.md)

## 📊 Desempenho (Cemu 2.6)

Ambiente: Linux/Vulkan, Mesa llvmpipe, host compartilhado, TV 1920×1080. Janelas de 60 quadros; primeira janela de cada cenário excluída (aquecimento). **Não é medição do Wii U físico.**

| Cenário | FPS médio | Menor janela | Pior quadro | > 25 ms |
|---|---:|---:|---:|---:|
| Fazenda em movimento | 49.7 | 45.2 | 127.879 ms | 52/360 |
| Fazenda com chuva | 54.2 | 46.9 | 31.567 ms | 28/360 |
| Fazenda à noite | 54.4 | 50.4 | 38.533 ms | 28/360 |
| Cidade / carro Lewis | 60.0 | 59.1 | 29.408 ms | 1/360 |
| Cidade / rio | 60.2 | 59.9 | 23.816 ms | 0/360 |
| Interior Pierre | 60.0 | 59.4 | 29.526 ms | 3/360 |

Meta: mínimo 40 FPS, alvo 60 FPS. Médias passam de 40 e várias chegam perto de 60, **mas o mínimo contínuo de 40 FPS ainda não foi atingido/garantido**.

## ✅ Validação desta compilação

- 15 suítes C++; assets; ASan/UBSan.
- 35 capturas com pixels idênticos à R1 (exceto a correção do carro).
- 862 objetos de assets PowerPC comparados byte a byte.
- RPXs: `stardew_explorer_v011r2.rpx` e `stardew_explorer_v011r2_compat.rpx`.
- **Não validado no Wii U físico** nesta entrega.

## 🖥️ Conceito das duas telas

| TV | GamePad |
|:---:|:---:|
| Mundo Full HD (GX2) | Inventário / mapa / HUD independente |

O mundo lógico permanece compacto e é ampliado por vizinho mais próximo; Full HD descreve a saída da TV, não novos detalhes no mapa.

## 🕹️ Controles (resumo)

- Analógico esquerdo: mover (leve = andar) · **A** interagir · **Y** ferramenta · **X** inventário
- **L/R** seleção/abas · **+** pausa · **−** diário · **B** voltar
- Analógico direito / toque: cursor

## 📦 O que o laboratório já cobre (acumulado)

48 mapas · 34 NPCs · agricultura sazonal · construções da Robin · correio · lojas · áudio XACT parcial · pesca · festivais parciais · interface original · saves com migração.

**Ainda pendente (entre outros):** VisibleFish completo, casamento, festivais integrais, mineração completa, geladeiras/Qi seasoning, carrinho/montaria/teletransporte, e validação no hardware real.

## 🧰 Este repositório (GitHub Pages)

```text
docs/         capturas Cemu R2, cobertura, desempenho, histórico
preview/      demo antiga v0.1 (não é a R2)
index.html    página de apresentação
native/       núcleo histórico inicial da v0.1
```

O pacote completo da R2 (RPX + fonte + evidências) é entregue no ZIP da versão, separado deste site.

## 📚 Aviso

Stardew Valley e os materiais originais pertencem aos respectivos titulares. Projeto experimental e não oficial, sem vínculo ou endosso da ConcernedApe ou de outros titulares. Não há alegação de port completo, versão oficial ou desempenho garantido no console físico.
