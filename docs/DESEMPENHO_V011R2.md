# Medição de desempenho — V0.11 R2

Cemu 2.6, Linux/Vulkan, Mesa llvmpipe, host compartilhado. TV 1920×1080. Movimento programado, seis cenários. Médias em janelas de 60 quadros, excluindo a primeira janela de cada visita para aquecimento. Não é medição do Wii U físico.

| Cenário | FPS médio | Menor média de janela | Pior quadro (ms) | Quadros acima de 25 ms |
|---|---:|---:|---:|---:|
| Fazenda em movimento | 49.7 | 45.2 | 127.879 | 52/360 |
| Fazenda com chuva | 54.2 | 46.9 | 31.567 | 28/360 |
| Fazenda à noite | 54.4 | 50.4 | 38.533 | 28/360 |
| Cidade / carro Lewis | 60.0 | 59.1 | 29.408 | 1/360 |
| Cidade / rio | 60.2 | 59.9 | 23.816 | 0/360 |
| Interior Pierre | 60.0 | 59.4 | 29.526 | 3/360 |

O teste mostrou médias acima de 40 FPS e várias próximas de 60. Existem picos: portanto, mínimo contínuo de 40 FPS ainda NÃO foi atingido/garantido. O pior pico observado fora das janelas de aquecimento foi 127,879 ms na fazenda. Ambiente compartilhado e renderização Vulkan por software também afetam a comparação.

Os logs brutos contêm inclusive aquecimento e troca de cenário. O log do executável de distribuição confirma o funcionamento sem movimento programado. A versão compatível foi inicializada separadamente.
