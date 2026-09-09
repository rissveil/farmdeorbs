"""
ui.py – Auxiliares da interface do terminal: cores, banners, animações, menus e créditos.
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
    """Exibe um título dentro de uma caixa com bordas ASCII."""
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
    """Exibe o banner do programa."""
    banner = rf"""
{Colors.CYAN}{Colors.BOLD}
 _______                    _              _        ____            _     
|__   __|                  | |            | |      |  _ \          | |    
   | | ___ _ __ ___  _ __  | |__   ___  __| | ___ | |_) | ___ _ __ | |___ 
   | |/ _ \\ '_ ` _ \\| '_ \\ | '_ \\ / _ \\/ _` |/ _ \\|  _ < / _ \\ '_ \\| / __|
   | |  __/ | | | | | | | | | |_) |  __/ (_| | (_) | |_) |  __/ | | | | \\__ \\
   |_|\\___|_| |_| |_|_| |_| |_.__/ \\___|\\__,_|\\___/|____/ \\___|_| |_|_|___/

{Colors.RESET}
    {Colors.GRAY}Projeto: {Colors.CYAN}Farm de Orbs{Colors.RESET}
    {Colors.GRAY}Desenvolvedora: {Colors.CYAN}{config.DEVELOPER}{Colors.RESET}
    {Colors.GRAY}Versão: {Colors.WHITE}{config.VERSION}{Colors.RESET}
    {Colors.GRAY}Banco de dados: {Colors.GREEN}API oficial do Discord + arquivo de backup do GitHub{Colors.RESET}
"""

    print(banner)


def loading_animation(text: str, duration: float = 1.5) -> None:
    """Exibe uma animação de carregamento."""
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
    """Solicita uma confirmação S/n. Retorna True se o usuário confirmar."""
    answer = input(f"\n{Colors.BOLD}{prompt}{Colors.RESET} [S/n]: ").strip().lower()
    return answer in ('', 's', 'sim', 'y', 'yes')


def print_menu() -> None:
    """Exibe o menu principal."""
    print_boxed_title("MENU PRINCIPAL", width=50, color=Colors.CYAN)
    print(f"  {Colors.BOLD}{Colors.GREEN}1.{Colors.RESET} Pesquisar banco de dados do Discord (API oficial)")
    print(f"  {Colors.BOLD}{Colors.GREEN}2.{Colors.RESET} Modo manual (executável personalizado)")
    print(f"  {Colors.BOLD}{Colors.YELLOW}3.{Colors.RESET} Modo de missão do Steam  {Colors.YELLOW}[NOVO - para Marathon, Toxic Commando…]{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.GREEN}4.{Colors.RESET} Créditos e informações")
    print(f"  {Colors.BOLD}{Colors.RED}5.{Colors.RESET} Sair\n")


def show_credits() -> None:
    """Exibe os créditos."""
    print_boxed_title("CRÉDITOS", width=65, color=Colors.CYAN)
    credits_text = f"""
    {Colors.BOLD}Desenvolvedor:{Colors.RESET} {Colors.CYAN}{config.DEVELOPER}{Colors.RESET}
    {Colors.BOLD}Versão:{Colors.RESET}   {Colors.WHITE}{config.VERSION}{Colors.RESET}

    {Colors.BOLD}Descrição:{Colors.RESET}
    Esta ferramenta simula processos de jogos. Ela faz o Discord pensar que
    um jogo está em execução ao criar processos simulados com os
    nomes exatos que o Discord espera.
    
    {Colors.BOLD}IMPORTANTE:{Colors.RESET} {Colors.RED}o Discord DEVE estar em execução para isso funcionar!{Colors.RESET}
    
    {Colors.BOLD}Como funciona (simulação de jogos):{Colors.RESET}
    1. Conecta-se à API oficial do Discord para obter a lista atualizada de jogos
    2. Encontra o nome exato do processo esperado pelo Discord para cada jogo
    3. Copia o executável para Desktop/Win64/ e renomeia para corresponder
    4. Inicia o processo simulado em segundo plano
    5. O Discord verifica os processos em execução e detecta o nome simulado
    6. O Discord entende que você está jogando (correspondência do processo)
    7. O processo simulado precisa continuar em execução para ser detectado
    
    {Colors.BOLD}Modo de missão do Steam:{Colors.RESET}
    Alguns jogos (Marathon, Toxic Commando...) exigem que o Discord verifique
    se o Steam iniciou pelo menos parte do download.
    O modo de missão do Steam contorna essa verificação:
    1. Obtém automaticamente as informações do aplicativo pela API pública do SteamCMD
    2. Gera um appmanifest_<appid>.acf simulado na pasta steamapps/
    3. Coloca o executável simulado diretamente em steamapps/common/<installdir>/
    O Discord encontra um manifesto válido do Steam e um processo em execução, ativando a missão.
    
    {Colors.BOLD}Fontes do banco de dados:{Colors.RESET}
    • Principal: API oficial do Discord
    • Backup: arquivo do GitHub mantido por Cynosphere
    
    {Colors.BOLD}Dicas importantes:{Colors.RESET}
    • Use o modo de missão do Steam para jogos não detectados pelos modos 1 ou 2
    • Encontre AppIDs no SteamDB
    • O processo simulado precisa permanecer em execução para o Discord detectá-lo
    
    {Colors.BOLD}{Colors.GREEN}Simulação de vários jogos:{Colors.RESET}
    • Execute esta ferramenta várias vezes para simular vários jogos ao mesmo tempo
    • Conclua todas as missões de Orbes simultaneamente em apenas 15 minutos
    
    {Colors.BOLD}{Colors.RED}AVISO - APENAS PARA FINS EDUCACIONAIS{Colors.RESET}
    • Os usuários são os únicos responsáveis por cumprir os Termos de Serviço do Discord
    • A desenvolvedora não se responsabiliza por quaisquer consequências
    • Use por sua própria conta e risco
    
    {Colors.GRAY}Feito por {config.DEVELOPER}{Colors.RESET}
    {Colors.GRAY}Pressione Enter para voltar ao menu...{Colors.RESET}
"""
    print(credits_text)
    input()
