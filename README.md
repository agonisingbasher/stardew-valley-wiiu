<h1 align="center">🌱 Stardew Valley — conceito experimental para Wii U</h1>

<h3 align="center">Wii U Homebrew • C++ • GamePad • Exploração de mapas</h3>

<p align="center">
  <img alt="Versão do projeto" src="https://img.shields.io/badge/Vers%C3%A3o-v0.1-79bd68?style=for-the-badge">
  <img alt="Plataforma-alvo" src="https://img.shields.io/badge/Plataforma-Wii%20U-00a6c8?style=for-the-badge">
  <img alt="Linguagem nativa" src="https://img.shields.io/badge/C%2B%2B-prot%C3%B3tipo-00599C?style=for-the-badge&logo=cplusplus&logoColor=white">
</p>

> **Um protótipo de exploração, não um port de Stardew Valley.** Este laboratório experimental estuda como uma adaptação para Wii U poderia aproveitar a TV e o GamePad. A versão v0.1 reconstrói uma fazenda a partir dos assets do projeto, com movimento, câmera, colisão aproximada e simulação de segunda tela.

## 🚀 Sobre o projeto

O conceito nasceu da ideia de dar à tela do GamePad um papel próprio: manter mapa, inventário, calendário e informações úteis à mão enquanto a TV mostra a fazenda. Em vez de apenas espelhar a imagem, as duas telas poderiam trabalhar juntas e reduzir interrupções durante a exploração.

Este repositório documenta a primeira base técnica desse conceito. O que existe hoje é um protótipo pequeno para investigar leitura de mapa, movimento e apresentação em duas telas — não uma versão jogável completa de Stardew Valley.

### 🌐 Apresentação e demonstração

**[Acesse a página do projeto](https://agonisingbasher.github.io/stardew-valley-wiiu/)** para conhecer o conceito e o estágio atual.

**[▶ Abrir o PREVIEW interativo](preview/index.html)** — clone o repositório e abra `preview/index.html` em um navegador. A demonstração funciona sem servidor.

O preview foi testado com testes de integração que simulam o DOM e o canvas; isso não substitui uma validação visual em um navegador real. Ele roda no computador e **não** é um executável de Wii U nem uma medição de desempenho do console.

### GitHub Pages

A página do projeto já está publicada no GitHub Pages: **[agonisingbasher.github.io/stardew-valley-wiiu](https://agonisingbasher.github.io/stardew-valley-wiiu/)**. O botão **Abrir o PREVIEW** leva à demonstração interativa.

---

## 🖥️ Conceito das duas telas

| TV | GamePad |
|:---:|:---:|
| Exploração da fazenda | Mapa e informações |

O banner provisório está em `docs/banner.png`. Alguns recursos ainda são conceitos, não funções implementadas.

---

## 🎯 O que a v0.1 já faz

* 🗺️ **Reconstrói o mapa da fazenda:** leitura do mapa tBIN10 de 80 × 65 blocos, com seis camadas e quatro tilesets.
* 🚶 **Permite explorar o cenário:** movimento em oito direções, câmera acompanhando o avatar temporário e colisão aproximada.
* 🖥️ **Simula a segunda tela:** alternância entre mapa e jogo no GamePad do preview; no código C++ inicial, a saída é desenhada para TV e GamePad.
* 🧰 **Mantém ferramentas reproduzíveis:** scripts para preparar os arquivos selecionados, interpretar o mapa e construir os recursos da demonstração.
* ✅ **Testa regras básicas:** testes do núcleo C++ e um teste de integração do viewer com DOM/canvas simulados.

### O que ainda é apenas conceito

Inventário permanente na tela touch, arrastar e soltar, NPCs em movimento no mapa, relacionamentos, previsão do tempo, calendário e alternância completa para jogar só no GamePad são ideias para etapas futuras. Não fazem parte das funções implementadas na v0.1.

---

## 🧪 Evidências e limites

| Área | Estado nesta versão |
|---|---|
| Mapa e recursos | O mapa do projeto foi lido e convertido; animações são representadas pelo primeiro frame no preview. |
| Movimento e colisão | O núcleo C++ foi testado no computador para colisão, limites, movimento diagonal e posição inicial. A colisão é aproximada. |
| Preview de navegador | Testes com DOM/canvas simulados cobrem movimento, reinício, alternância de tela, limites e perda de foco. Não houve validação visual automatizada em navegador real. |
| Código nativo Wii U | Existe código C++ inicial baseado em WUT, com entrada do GamePad e saída nas duas telas. **Não foi compilado nem testado em um Wii U nesta entrega.** |
| Desempenho | Não há benchmark de FPS ou memória no console. O renderer nativo atual usa OSScreen e um viewport de teste por software; deve ser substituído por renderização acelerada. |

### ⚙️ O protótipo e um jogo completo

O cenário ainda não monta automaticamente casa, estufa, caixa de remessa, plantações, pedras, árvores dinâmicas e construções. Também não implementa agricultura, ferramentas, inventário, áudio, eventos, horários ou salvamento. A avatar atual é Abigail, usada temporariamente para testar a exploração.

Os arquivos enviados incluem código descompilado identificado como versão 1.5.6 e recursos com nomes associados a conteúdo mais recente. A compatibilidade geral entre essas versões ainda não foi validada; este projeto não compila o código C# original.

---

## 🛠️ Tecnologias e conceitos

* C++ e testes unitários do núcleo de movimento.
* HTML Canvas e JavaScript para o preview interativo.
* Node.js e `xnb.js` para a etapa de extração selecionada de recursos XNB.
* Python e Pillow para conversão e composição dos recursos.
* WUT / devkitPro como base do código nativo inicial de Wii U.
* Interpretação de formato binário, colisão por tiles, câmera e interação entre telas.

---

## ▶️ Executar o preview

Clone o projeto completo e abra `preview/index.html` no navegador. Os dados e imagens do preview estão incluídos neste repositório.

| Controle | Ação |
|---|---|
| Setas ou WASD | Mover |
| Shift | Correr |
| M | Alternar mapa / jogo no GamePad |
| C | Mostrar ou ocultar colisões |
| R | Voltar à posição inicial |
| Controle conectado | Analógico esquerdo/direcional para mover, A para correr, Y para alternar tela (mapeamento depende do navegador) |

---

## 🧱 Compilar o protótipo nativo

Para tentar compilar o código para Wii U, instale devkitPro com devkitPPC, WUT, libwhb e as ferramentas de empacotamento necessárias. Consulte a [documentação do WUT](https://github.com/devkitPro/wut).

```sh
cd native
make
```

O alvo do Makefile é `stardew_explorer_v01.rpx`. A compilação depende da toolchain configurada. Não foi validada nesta entrega e **este repositório não inclui um RPX pré-compilado**.

Controles previstos no código nativo: analógico esquerdo/direcional para mover, A para correr, Y para alternar mapa/jogo no GamePad, X para reiniciar e + para sair.

---

## 🧰 Reproduzir a conversão de recursos

Para reproduzir a conversão de recursos, use Python com Pillow, Node e o ZIP original da parte 1:

```sh
npm ci
python -m pip install -r requirements.txt
python tools/stage_assets.py "/caminho/Content part 1.zip"
node tools/unpack.cjs Maps/Farm Maps/spring_outdoorTileSheet_extra Maps/paths Maps/spring_outdoorsTileSheet Maps/spring_outdoorsTileSheet2 Characters/Abigail Characters/Farmer/farmer_base
python tools/build_assets.py
```

O estágio seleciona sete arquivos conhecidos do ZIP em vez de extrair caminhos arbitrários. O leitor XNB usa uma cópia com deslocamento zero para evitar a interpretação incorreta de Buffers compartilhados do Node.

Para repetir os testes do núcleo e do viewer, a partir da raiz:

```sh
g++ -std=c++17 -Wall -Wextra -Werror tests/core_test.cpp -o core_test
./core_test
node tests/viewer_test.cjs
```

---

## 🗂️ Estrutura do projeto

```text
assets/       recursos convertidos e dados do mapa
docs/         banner provisório da apresentação
native/       código C++ inicial, dados e Makefile para Wii U
preview/      demonstração interativa no navegador
tests/        testes do núcleo e do viewer
tools/        ferramentas de extração, leitura e conversão
index.html    página de apresentação do projeto
```

---

## 🛣️ Próximos marcos

1. Compilar o RPX com a toolchain Wii U e validar inicialização e comandos no console.
2. Substituir OSScreen por renderização acelerada e medir o custo das duas telas.
3. Montar o fazendeiro e aplicar construções e objetos dinâmicos da fazenda.
4. Implementar ferramentas, plantio, rega, colheita e persistência.
5. Evoluir o GamePad para interfaces interativas de mapa e inventário.

---

## 📚 Fontes, créditos e aviso

* **Stardew Valley** e os materiais originais relacionados pertencem aos seus respectivos titulares. Os assets deste protótipo foram fornecidos pelo desenvolvedor para este repositório; isso não implica afiliação, endosso ou licença sobre a propriedade intelectual de terceiros.
* Projeto experimental e não oficial, sem vínculo ou endosso da ConcernedApe ou de outros titulares de direitos.
* [xnb.js](https://github.com/lybell-art/xnb-js) — LGPL-3.0-or-later; dependência indicada em `package-lock.json`.
* [Formato tBIN — referência](https://github.com/colinvella/tIDE/blob/master/TileMapEditor/xTile/Format/TbinFormat.cs).
* [WUT — Wii U Toolchain](https://github.com/devkitPro/wut).

Não há alegação de que este protótipo seja um port completo, uma versão oficial ou uma compilação funcional para o console.

---

<p align="center"><strong>Um conceito de tela dupla, começando pela fazenda, pelo movimento e por uma primeira prova de exploração.</strong></p>
