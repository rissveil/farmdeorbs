"""
main.py – Ponto de entrada e loop principal da aplicação.
"""

import os
import sys
import subprocess
import time

from . import config
from .ui import Colors, print_color, print_banner, print_menu, show_credits
from .faker import GameFaker, manual_mode
from .discord_db import DiscordGamesDB, database_mode
from .steam import steam_quest_mode
from .updater import auto_update
from .errors import DatabaseLoadError


def main() -> None:
    """Loop principal da aplicação."""
    try:
        auto_update()
    except Exception:
        pass

    print_banner()
    print_color("Inicializando o Farm de Orbs...", Colors.CYAN)
    print_color("[*] Conectando à API do Discord...", Colors.GRAY)

    try:
        db = DiscordGamesDB()
    except DatabaseLoadError as e:
        print_color(f"[ERRO] {e}", Colors.RED, bold=True)
        sys.exit(1)

    faker = GameFaker()
    print_color("[OK] Pronto para simular alguns jogos!", Colors.GREEN)
    time.sleep(0.5)

    try:
        while True:
            try:
                subprocess.run(
                    'cls' if os.name == 'nt' else 'clear',
                    shell=True,
                    check=False,
                )
                print_banner()

                if db.source:
                    print_color(f"   Banco de dados ativo: {db.source} ({len(db.games)} jogos)", Colors.GRAY)

                print_menu()
                choice = input(f"{Colors.BOLD}Selecione uma opção{Colors.RESET} [1-5]: ").strip()

                if choice == '1':
                    database_mode(db, faker)
                elif choice == '2':
                    manual_mode(faker)
                elif choice == '3':
                    steam_quest_mode(faker)
                elif choice == '4':
                    show_credits()
                elif choice == '5':
                    print_color(f"\n[*] Obrigado por usar o Farm de Orbs!", Colors.CYAN, bold=True)
                    print_color(f"[*] Desenvolvido por {config.DEVELOPER}", Colors.GRAY)
                    print_color("\n[*] Que seus orbes sejam abundantes!", Colors.MAGENTA)
                    break
                else:
                    print_color("\n[ERRO] Opção inválida - tente 1, 2, 3, 4 ou 5", Colors.RED)
                    time.sleep(config.SLEEP_SHORT)

            except KeyboardInterrupt:
                print_color("\n\n[!] Interrompido pelo usuário", Colors.YELLOW)
                print_color("[*] Obrigado por usar o Farm de Orbs!\n", Colors.CYAN)
                break
    finally:
        faker.cleanup()
