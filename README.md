# 🌱 Stardew Valley — laboratório experimental para Wii U

**Wii U Homebrew · C++ · GamePad · Cemu · V0.14 R9**

> **Protótipo nativo, não um port oficial nem o jogo completo.** O laboratório estuda como Stardew Valley pode aproveitar a TV Full HD e o GamePad do Wii U. A **V0.14 R9** (17/11/2026) traz a frente de boot com slots e gerações, os sete tipos de fazenda com o chão reproduzido byte a byte, a ferraria, a mina em quatro setores e o combate inicial.

## 🌐 Página do projeto

**[agonisingbasher.github.io/stardew-valley-wiiu](https://agonisingbasher.github.io/stardew-valley-wiiu/?lang=pt-BR)** — estado atual, capturas do Cemu, histórico de desempenho e documentação da R9 (PT-BR / EN / ES / FR).

O preview no navegador (`preview/index.html`) permanece a **demo antiga da v0.1** e **não** representa a V0.14 R9. A R9 roda como RPX no Cemu / Wii U. As capturas publicadas na página são da **V0.11 R2** e continuam rotuladas como tal.

## 🎯 V0.14 R9 em resumo

- **Boot e saves:** título, criador de personagem, três slots com retrato, nome, fazenda, data e ouro lidos do manifesto; gerações recuperáveis em `gen-XXXX` e saves escritos por revisões anteriores preservados nos blocos r6 a r9, em `stardew_wiiu_v013_slotN/gen-XXXX/main.sav`.
- **Sete tipos de fazenda:** o chão da fazenda padrão sai byte a byte do atlas e das grades — 5.324.800 bytes, 0 divergências. A frente coincide em 96,779 % e a profundidade em 88,691 %; a ordem de bytes dos índices foi corrigida para little-endian no PowerPC.
- **Mina e combate:** melhorias de ferramenta na ferraria, quatro setores com escadas e elevador e, na R9, a espada de Marlon com 2 a 5 de dano, duas gosmas por setor, dano de contato e resgate com 25 de vida.
- **Mundo e sistemas:** 48 mapas, 34 NPCs com agenda, 51 cultivos, 15 construções da Robin, 58 cartas originais, lojas sazonais, áudio noturno sazonal e sidecar da fazenda em v4.
- **Entrega padrão:** pasta `Stardew_WiiU_v014r9` com `executavel/`, `fonte/` e evidências. Um ZIP só é feito sob pedido explícito.

Detalhes: [`docs/COBERTURA_V014R9.html`](docs/COBERTURA_V014R9.html) · [`docs/COBERTURA_V011R2.md`](docs/COBERTURA_V011R2.md) · [`docs/DESEMPENHO_V011R2.md`](docs/DESEMPENHO_V011R2.md) · [`docs/HISTORICO_VERSOES.md`](docs/HISTORICO_VERSOES.md) · [`docs/ENTREGA_PADRAO.md`](docs/ENTREGA_PADRAO.md)

## 📊 Desempenho: histórico da V0.11 R2

**FPS e RAM não são medidos desde a V0.11 R2.** O progresso registra as duas grandezas como `nao-medido` nas revisões seguintes, e a tabela abaixo descreve a R2, não a R9.

Ambiente da R2: Linux/Vulkan, Mesa llvmpipe, host compartilhado, TV 1920×1080. Janelas de 60 quadros; primeira janela de cada cenário excluída (aquecimento). **Não é medição do Wii U físico.**

| Cenário | FPS médio | Menor janela | Pior quadro | > 25 ms |
|---|---:|---:|---:|---:|
| Fazenda em movimento | 49.7 | 45.2 | 127.879 ms | 52/360 |
| Fazenda com chuva | 54.2 | 46.9 | 31.567 ms | 28/360 |
| Fazenda à noite | 54.4 | 50.4 | 38.533 ms | 28/360 |
| Cidade / carro Lewis | 60.0 | 59.1 | 29.408 ms | 1/360 |
| Cidade / rio | 60.2 | 59.9 | 23.816 ms | 0/360 |
| Interior Pierre | 60.0 | 59.4 | 29.526 ms | 3/360 |

Meta do projeto: mínimo 40 FPS, alvo 60 FPS, como **critério de validação**, não como garantia. Na R2 as médias passam de 40 e várias chegam perto de 60, **mas o mínimo contínuo de 40 FPS nunca foi atingido/garantido**; o pior pico fora do aquecimento foi 127,879 ms na fazenda.

## ✅ Validação desta compilação

- 49 suítes C++ de host e 24 verificações entre testes Python e verificadores de ferramenta, fechando com `SCRIPT_EXIT=0` e `BUILD_EXIT=0`.
- 948 objetos de assets PowerPC comparados byte a byte.
- RPXs `stardew_explorer_v014r9.rpx` (GX2 Full HD) e `stardew_explorer_v014r9_compat.rpx` (OSScreen) compilados.
- O que foi visto no Cemu está descrito como evidência da revisão, separado do que passou em teste de host.
- **Não validado no Wii U físico:** o build-info da R9 registra `nao-testado`; nenhum cenário desta revisão tem console físico.

## 🖥️ Conceito das duas telas

| TV | GamePad |
|:---:|:---:|
| Mundo Full HD (GX2) | Inventário / mapa / HUD independente |

O mundo lógico permanece compacto e é ampliado por vizinho mais próximo; Full HD descreve a saída da TV, não novos detalhes no mapa.

## 🕹️ Controles (resumo)

- Analógico esquerdo: mover (leve = andar) · **A** interagir/confirmar · **Y** ferramenta/espada · **X** inventário
- **L/R** seleção/abas · **+** pausa · **−** diário · **B** voltar
- Analógico direito / toque: cursor

## 📦 O que o laboratório já cobre (acumulado)

48 mapas · 34 NPCs · sete tipos de fazenda · agricultura sazonal · ferraria · mina em quatro setores · combate inicial · construções da Robin · correio · lojas · áudio XACT parcial · pesca · festivais parciais · interface original · saves por slot e geração com migração.

**Ainda pendente (entre outros):** a fazenda da praia, que não existe no dump local, e o tipo 6 (ilha 110×110), que segue sem resolução; as 120 plantas individuais da mina, os cofres por planta e a animação completa do mapa; cercas, nomes das galinhas, interior do galinheiro, rotinas diárias, casamento, festivais integrais, produção animal completa, VisibleFish, cooperativo — e toda validação no hardware real. Dentro do jogo, o texto existe apenas em português.

No escopo V1.0, 5 de 56 requisitos têm aceite demonstrado no host (8,9 %) e 52 de 56 têm implementação identificada. Isso é aceite técnico no computador, não validação de console.

## 🧰 Este repositório (GitHub Pages)

```text
index.html            página de apresentação (V0.14 R9)
idioma-pagina.js      motor de idioma compartilhado pelas páginas secundárias
site-development.html autoria do site
support.html          apoio aos futuros projetos
docs/                 cobertura R9/R2, desempenho, histórico, entrega, feedback
preview/              demo antiga v0.1 (não é a R9)
native/               núcleo histórico inicial da v0.1
```

O pacote da R9 (RPX + fonte + evidências) fica na pasta de entrega da versão, separado deste site. Nada de ROM, dump ou assets extraídos do jogo entra aqui.

## 🌍 Idioma

Todas as páginas — apresentação, `preview/`, as seis páginas de `docs/` (incluindo o formulário de feedback), `site-development.html` e `support.html` — trazem o seletor com os quatro botões `PT / EN / ES / FR`. Os textos em espanhol e francês vêm de dicionários escritos para o projeto; não há link nem chamada para o Google Translate. A decisão segue `?lang=` > escolha salva no navegador (chave única `stardew-wiiu-language`, compartilhada por raiz, `preview/` e `docs/`) > `navigator.languages` > pt-BR, e qualquer `pt-*` colapsa em `pt-BR`. Chave ausente em um idioma cai no texto português que já está no HTML, em vez de imprimir `undefined`. No preview, até o rótulo dinâmico da dupla tela (`Casilla 64, 15 · 80 × 65` / `Case 64, 15 · 80 × 65`) é montado pela função do próprio idioma.

Há três implementações do mesmo contrato: `index.html` e `preview/index.html` carregam motores próprios embutidos, e `idioma-pagina.js` atende as páginas de `docs/` mais as duas páginas secundárias da raiz. As páginas que usam `idioma-pagina.js` declaram `window.pageTranslations` antes do script; o idioma de navegação (`languageLabel`), o `<title>` e a `meta description` vêm de `pageTitle` / `pageDescription`. Traduzir uma página nova é escrever o dicionário e apontar o mesmo `<script src>` — raiz ou `docs/`.

O texto **dentro** do jogo prototipado continua em português: o seletor traduz o site, não o RPX.

## 📚 Aviso

Stardew Valley e os materiais originais pertencem aos respectivos titulares. Projeto experimental e não oficial, sem vínculo ou endosso da ConcernedApe ou de outros titulares. Não há alegação de port completo, versão oficial ou desempenho garantido no console físico.
