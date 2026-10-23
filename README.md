<div align="center">

# orbshacker · Edição PT-BR

[![Plataforma](https://img.shields.io/badge/Plataforma-Windows%20Only-555555?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/rissveil/farmdeorbs)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-GPL%20v3-c0392b?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](./LICENSE)
[![Versão](https://img.shields.io/github/v/release/rissveil/farmdeorbs?style=for-the-badge&logo=semanticrelease&color=4ade80&logoColor=white)](https://github.com/rissveil/farmdeorbs/releases)

*Porque ninguém quer instalar centenas de gigabytes só para conseguir alguns orbes.*

[Começar](#instalação) · [Como funciona](#como-funciona) · [Modo Steam](#modo-steam-quest) · [Uso](#como-usar) · [Aviso legal](#aviso-legal)

</div>

## O que é o orbshacker?

O orbshacker é uma ferramenta para Windows que simula processos de jogos para que o Discord os reconheça durante missões de Orbes, sem precisar instalar os jogos correspondentes. A ferramenta consulta a API pública do Discord para obter os nomes de processos esperados, cria cópias de um executável-base com esses nomes e inicia os processos em segundo plano.

> **Uso educacional.** Este projeto é disponibilizado para estudo do funcionamento da detecção de jogos do Discord e de técnicas de manipulação de processos. Use por sua conta e risco e respeite os termos de serviço aplicáveis. O uso pode contrariar as regras da plataforma.

## Modo Steam Quest

Alguns jogos exigem uma verificação adicional: além do nome do processo, o Discord pode conferir informações de instalação da Steam. O modo Steam Quest tenta reproduzir os arquivos locais que essa verificação procura.

### Como funciona

Você pesquisa o jogo pelo nome dentro da ferramenta. Ela consulta metadados públicos da Steam, identifica informações como a pasta de instalação e o executável e tenta obter automaticamente o ID da conta Steam pelo Registro do Windows. Em seguida, gera um arquivo `appmanifest_<appid>.acf` e coloca um executável com o nome esperado na pasta correspondente.

**Observação:** o método pode deixar de funcionar se o Discord ou a Steam alterarem seus mecanismos de verificação. Jogos, demos e DLCs podem ter IDs diferentes.

## Recursos

- **Busca automática de jogos:** consulta a lista pública de jogos detectáveis pelo Discord e permite pesquisar por nome ou abreviação.
- **Modo manual:** permite informar um nome de executável personalizado.
- **Modo Steam Quest:** pesquisa jogos na Steam e gera os arquivos locais usados pelo método.
- **Temporizador:** mantém o processo simulado em execução pelo período configurado.
- **Limpeza automática opcional:** pode remover os arquivos criados pela ferramenta quando o temporizador termina.
- **Integração com APIs:** utiliza a API do Discord para consultar jogos detectáveis e a API da Steam para buscar informações dos jogos no modo Steam Quest.
- **Interface no terminal:** menus, mensagens coloridas e indicadores de carregamento.

## Requisitos

- Windows.
- Python compatível com as dependências do projeto, caso execute a partir do código-fonte.
- Conexão com a internet para consultar as APIs.
- Discord em execução para que a detecção de processos possa ocorrer.

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/rissveil/farmdeorbs.git
cd farmdeorbs
pip install -r requirements.txt
```

## Como usar

Execute pelo Python:

```bash
python orbshacker.py
```

Ou use o ponto de entrada do pacote:

```bash
python -m orbshacker
```

### Opções do menu

1. Pesquisar no banco de jogos do Discord.
2. Usar o modo manual e informar um nome de executável.
3. Abrir o modo Steam Quest.
4. Consultar os créditos e as informações do projeto.
5. Sair.

### Configurações

As opções editáveis ficam em `settings.py`, na raiz do projeto. Entre elas estão a pasta de destino, a remoção automática dos arquivos criados e a duração do temporizador. Confira as configurações antes de usar a ferramenta.

## Como funciona

A ferramenta consulta o endpoint público de jogos detectáveis do Discord e procura o nome de processo associado ao jogo selecionado. Depois, copia o executável-base para a pasta configurada e usa o nome esperado pelo Discord. No modo Steam Quest, também tenta criar um manifesto local na pasta da Steam.

Os nomes de arquivos, caminhos, respostas das APIs e versões da plataforma podem mudar. Portanto, não há garantia de que o método funcione com todos os jogos ou continue funcionando após atualizações.

## Estrutura do projeto

```text
orbshacker/
├── orbshacker.py          Ponto de entrada
├── orbshacker/
│   ├── __init__.py        Versão e metadados
│   ├── __main__.py        Entrada do pacote
│   ├── config.py          Configurações
│   ├── faker.py           Criação e inicialização dos processos simulados
│   ├── discord_db.py      Consulta e seleção de jogos
│   ├── steam.py           Integração com metadados da Steam
│   ├── updater.py         Atualização automática
│   ├── net.py             Funções de rede
│   ├── ui.py              Interface do terminal
│   └── errors.py          Exceções do projeto
├── tests/                 Testes automatizados
├── settings.py            Configurações editáveis
├── requirements.txt       Dependências
└── .github/workflows/     Automação de versões
```

## Atualizador automático

Quando o projeto é distribuído como executável e há uma nova versão publicada, a ferramenta pode consultar as versões disponíveis no GitHub e tentar atualizar o arquivo executável. Essa função não é usada quando o programa é executado diretamente a partir do código-fonte.

## Aviso legal

Este projeto é desenvolvido por Rissa para fins educacionais e de pesquisa. O uso é de responsabilidade de quem o executa. Respeite os termos de serviço do Discord, da Steam e de quaisquer outros serviços envolvidos. Rissa não se responsabiliza por consequências decorrentes do uso indevido.

## Créditos

**Desenvolvido por Rissa.**

Consulte o arquivo `LICENSE` para os termos da licença.
