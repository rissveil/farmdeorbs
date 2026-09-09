<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0a0a,60:0d1f0d,100:1a4a1a&height=200&section=header&text=Farm%20de%20Orbs&fontSize=60&fontColor=4ade80&fontAlignY=55&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.7+-3572A5?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Plataforma](https://img.shields.io/badge/Plataforma-Windows%20Only-555555?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Rissa/farm-de-orbs)
[![Discord](https://img.shields.io/badge/Discord-Missões%20de%20Orbes-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)
[![Licença](https://img.shields.io/badge/Licença-GPL%20v3-c0392b?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](./LICENSE)

<br/>

*para aqueles que não conseguem instalar jogos pesados ou simplesmente não querem.*

<br/>

[Começar](#instalação) &nbsp;·&nbsp; [Como funciona](#como-funciona) &nbsp;·&nbsp; [Modo Steam](#modo-de-missão-do-steam) &nbsp;·&nbsp; [Uso](#uso) &nbsp;·&nbsp; [Estrutura](#estrutura-do-projeto) &nbsp;·&nbsp; [Legal](#aviso-legal)

</div>

<br/>

## O que é isto

**Farm de Orbs** é uma ferramenta para Windows que cria processos de jogos simulados para missões de Orbes do Discord sem instalar os jogos reais. Ela consulta a API pública do Discord para obter os nomes exatos dos processos esperados, copia um executável base, renomeia-o e o inicia em segundo plano. O Discord verifica a lista de processos e pode reconhecer o processo correspondente à missão.

Sem modificação do cliente. Sem injeção de código. A ferramenta trabalha com a identificação do processo.

> **Apenas para fins educacionais.** Use por sua conta e risco e respeite os termos de serviço aplicáveis.

## Modo de missão do Steam

Alguns jogos utilizam uma verificação adicional relacionada ao Steam. Nesse caso, o modo de missão do Steam cria um `appmanifest_<appid>.acf` e coloca o executável simulado no diretório correspondente.

### Como funciona

1. Pesquise o jogo pelo nome.
2. Selecione o resultado correto.
3. A ferramenta obtém as informações do aplicativo.
4. Um manifesto do Steam é criado na pasta `steamapps/`.
5. O executável simulado é colocado na pasta correspondente.
6. Ao terminar, a ferramenta pode limpar os arquivos criados.

**Compatível com jogos que exigem manifesto do Steam.**

> **Dica:** demos e jogos completos podem possuir AppIDs diferentes. Sempre selecione o resultado correto.

## Recursos

- **Detecção automática de jogos:** obtém a lista atualizada de jogos detectáveis pela API do Discord.
- **Pesquisa por nome ou abreviação:** facilita encontrar jogos rapidamente.
- **Modo manual:** permite informar um nome de executável personalizado.
- **Modo de missão do Steam:** cria os arquivos necessários para jogos que possuem uma verificação adicional.
- **Temporizador integrado:** mantém o processo simulado em execução pelo período configurado.
- **Exclusão automática:** remove arquivos simulados ao terminar, quando `AUTO_DELETE` está ativado.
- **Vários jogos:** permite executar processos simulados para diferentes jogos ao mesmo tempo.
- **Banco de dados de backup:** utiliza uma fonte alternativa caso a API principal esteja indisponível.
- **Interface de terminal:** menu simples com cores e animações.

## Como funciona

A ferramenta consulta a API oficial do Discord para obter os jogos detectáveis e seus nomes de processo. Ao selecionar um jogo, o programa cria uma cópia do executável e a renomeia de acordo com o processo esperado.

Quando o processo simulado é iniciado, ele mantém um temporizador em execução. O objetivo é permitir que o Discord encontre o nome do processo durante o período da missão.

O modo Steam acrescenta a criação de um manifesto `appmanifest_<appid>.acf` e o posicionamento do executável dentro da estrutura `steamapps/common/`.

## Requisitos

- Windows
- Python 3.7 ou superior
- Conexão com a internet
- Discord em execução durante a missão

## Instalação

```bash
git clone https://github.com/Rissa/farmdeorbs.git
cd farmdeorbs
pip install -r requirements.txt
```

## Uso

```bash
python orbshacker.py
```

Ou:

```bash
python -m orbshacker
```

### Opções do menu

`1` Pesquisar jogos no banco de dados do Discord

`2` Usar o modo manual

`3` Usar o modo de missão do Steam

`4` Ver créditos e informações

`5` Sair

### Concluindo várias missões

1. Abra a ferramenta.
2. Escolha um jogo.
3. Aguarde o processo ser iniciado.
4. Volte ao menu.
5. Escolha outro jogo.
6. Repita conforme necessário.
7. Mantenha os processos em execução durante o período da missão.

## Estrutura do projeto

```text
farm-de-orbs/
├── orbshacker.py
├── orbshacker/
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py
│   ├── faker.py
│   ├── discord_db.py
│   ├── steam.py
│   ├── updater.py
│   ├── net.py
│   ├── ui.py
│   └── errors.py
├── tests/
├── settings.py
├── requirements.txt
└── .github/
    └── workflows/
        └── release.yml
```

## Configuração

As configurações editáveis ficam em `settings.py`.

As principais opções são:

- `CHOSEN_FOLDER`: pasta onde os arquivos simulados serão criados.
- `AUTO_DELETE`: remove automaticamente os arquivos ao terminar.
- `TIMER_MINUTES`: duração do temporizador em minutos.

## Atualização automática

Quando uma nova versão é publicada no GitHub, o programa compilado pode verificar a versão disponível e atualizar o executável automaticamente.

## Aviso legal

**Apenas para fins educacionais e de pesquisa.**

Esta ferramenta foi criada para estudar o funcionamento da detecção de jogos e processos. O usuário é responsável por verificar e respeitar as leis, os termos de serviço do Discord, do Steam e de qualquer outro serviço utilizado.

A desenvolvedora não se responsabiliza por consequências decorrentes do uso inadequado da ferramenta.

## Licença

Este projeto utiliza a licença **GPL v3**. Consulte o arquivo `LICENSE` para os termos completos.

<br/>

<div align="center">

feito por **Rissa**

</div>
