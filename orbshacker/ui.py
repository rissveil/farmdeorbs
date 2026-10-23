"""
ui.py – Terminal UI helpers: colors, banners, animations, menus, credits.
"""

import sys
import time

from . import config


class Colors:
    RESET   = '\033[0m'
    BOLD    = '\033[1m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    GRAY    = '\033[90m'


def print_color(text: str, color: str = Colors.WHITE, bold: bool = False) -> None:
    """Print colored text."""
    style = Colors.BOLD if bold else ''
    print(f"{style}{color}{text}{Colors.RESET}")


def print_boxed_title(title: str, width: int = 50, color: str = Colors.CYAN) -> None:
    """Print a boxed title with ASCII borders."""
    border = f"{Colors.BOLD}{color}{'+' + '-' * (width - 2) + '+'}{Colors.RESET}"
    title_padding = (width - len(title) - 4) // 2
    extra_space = (width - len(title) - 4) % 2
    title_line = (
        f"{Colors.BOLD}{color}|{Colors.RESET}"
        f"{' ' * title_padding}{Colors.BOLD}{title}{Colors.RESET}"
        f"{' ' * (title_padding + extra_space)}"
        f"{Colors.BOLD}{color}|{Colors.RESET}"
    )
    print(f"\n{border}")
    print(title_line)
    print(f"{border}\n")


def print_banner() -> None:
    """Display ASCII banner."""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
                                                                
 _____ _____ _____ _____    _____ _____ _____ _____ _____ _____ 
|     | __  | __  |   __|  |  |  |  _  |     |  |  |   __| __  |
|  |  |    -| __ -|__   |  |     |     |   --|    -|   __|    -|
|_____|__|__|_____|_____|  |__|__|__|__|_____|__|__|_____|__|__|
                                                                
{Colors.RESET}
    {Colors.GRAY}Responsável: {Colors.CYAN}{config.DEVELOPER}{Colors.RESET}
    {Colors.GRAY}Versão: {Colors.WHITE}{config.VERSION}{Colors.RESET}
    {Colors.GRAY}Banco de dados: {Colors.GREEN}Discord API + Steam API{Colors.RESET}
"""
    print(banner)


def loading_animation(text: str, duration: float = 1.5) -> None:
    """Display loading animation."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    ascii_frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        try:
            sys.stdout.write(f"\r{Colors.CYAN}{frames[i % len(frames)]}{Colors.RESET} {text}")
            sys.stdout.flush()
        except UnicodeEncodeError:
            try:
                sys.stdout.write(f"\r{Colors.CYAN}{ascii_frames[i % len(ascii_frames)]}{Colors.RESET} {text}")
                sys.stdout.flush()
            except Exception:
                pass
        except Exception:
            pass
        time.sleep(0.1)
        i += 1
    try:
        sys.stdout.write("\r" + " " * (len(text) + 5) + "\r")
        sys.stdout.flush()
    except Exception:
        pass


def ask_confirm(prompt: str = "Criar e iniciar?") -> bool:
    """Ask a Y/n confirmation question. Returns True if user confirms."""
    answer = input(f"\n{Colors.BOLD}{prompt}{Colors.RESET} [S/n]: ").strip().lower()
    return answer in ('', 's', 'sim', 'y', 'yes')


def print_menu() -> None:
    """Display main menu."""
    print_boxed_title("MENU PRINCIPAL", width=50, color=Colors.CYAN)
    print(f"  {Colors.BOLD}{Colors.GREEN}1.{Colors.RESET} Pesquisar no banco de jogos do Discord (API oficial)")
    print(f"  {Colors.BOLD}{Colors.GREEN}2.{Colors.RESET} Modo manual (executável personalizado)")
    print(f"  {Colors.BOLD}{Colors.YELLOW}3.{Colors.RESET} Modo Steam Quest  {Colors.YELLOW}[NOVO: para Marathon, Toxic Commando…]{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.GREEN}4.{Colors.RESET} Créditos e informações")
    print(f"  {Colors.BOLD}{Colors.RED}5.{Colors.RESET} Sair\n")


def show_credits() -> None:
    """Display credits."""
    print_boxed_title("CRÉDITOS", width=65, color=Colors.CYAN)
    credits_text = f"""
    {Colors.BOLD}Responsável:{Colors.RESET} {Colors.CYAN}{config.DEVELOPER}{Colors.RESET}
    {Colors.BOLD}Versão:{Colors.RESET}   {Colors.WHITE}{config.VERSION}{Colors.RESET}

    {Colors.BOLD}Descrição:{Colors.RESET}
    Esta ferramenta simula processos de jogos para que o Discord pense
    que um jogo está em execução, criando processos com os
    nomes exatos esperados pelo Discord.
    
    {Colors.BOLD}IMPORTANTE:{Colors.RESET} {Colors.RED}O Discord precisa estar aberto para que isso funcione!{Colors.RESET}
    
    {Colors.BOLD}Como funciona (simulação de processos):{Colors.RESET}
    1. Consulta a API oficial do Discord para obter a lista atualizada de jogos
    2. Encontra o nome de processo esperado pelo Discord para cada jogo
    3. Copia o executável para Desktop/Win64/ e altera seu nome para corresponder ao jogo
    4. Inicia o processo simulado em segundo plano
    5. O Discord verifica os processos em execução e encontra o nome simulado
    6. O Discord interpreta que o jogo está aberto porque o nome do processo corresponde
    7. O processo simulado precisa continuar aberto para ser detectado pelo Discord
    
    {Colors.BOLD}Modo Steam Quest (NOVO):{Colors.RESET}
    Alguns jogos (como Marathon e Toxic Commando) exigem que o Discord verifique
    se a Steam iniciou o download do jogo.
    O modo Steam Quest tenta contornar essa verificação:
    1. Obtendo automaticamente os dados do jogo pela API pública do SteamCMD
    2. Gerando um arquivo appmanifest_<appid>.acf na pasta steamapps/
    3. Colocando o executável simulado em steamapps/common/<installdir>/
    O Discord pode encontrar o manifesto e o processo em execução e reconhecer a missão.
    
    {Colors.BOLD}Fontes do banco de dados:{Colors.RESET}
    • Discord API: consulta a lista de jogos detectáveis
    • Steam API: pesquisa jogos e obtém metadados para o modo Steam Quest
    • Cópia de segurança: usada caso a fonte principal esteja indisponível
    
    {Colors.BOLD}Dicas:{Colors.RESET}
    • Use o modo Steam Quest para jogos que não funcionam nos modos 1 ou 2
    • Consulte os AppIDs em https://steamdb.info
    • O processo simulado precisa permanecer aberto para ser detectado pelo Discord
    
    {Colors.BOLD}{Colors.GREEN}Simulação de vários jogos:{Colors.RESET}
    • Use a ferramenta para manter mais de um processo simulado em execução
    • As missões podem exigir cerca de 15 minutos, conforme as regras de cada uma
    
    {Colors.BOLD}{Colors.RED}AVISO: APENAS PARA FINS EDUCACIONAIS{Colors.RESET}
    • Cada usuário é responsável por respeitar os termos de serviço do Discord
    • Os responsáveis pelo projeto não se responsabilizam por consequências do uso
    • Use por sua conta e risco
    
    {Colors.GRAY}Desenvolvido por {config.DEVELOPER}{Colors.RESET}
    {Colors.GRAY}Pressione Enter para voltar ao menu...{Colors.RESET}
"""
    print(credits_text)
    input()
