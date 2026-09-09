"""
Exceções personalizadas do Farm de Orbs.

Keep it small — one base class + a few specific ones.
"""


class OrbshackerError(Exception):
    """Erro base para todos os erros do Farm de Orbs."""


class NetworkError(OrbshackerError):
    """Uma chamada de API/HTTP falhou."""


class SteamNotFoundError(OrbshackerError):
    """A instalação do Steam não pôde ser localizada."""


class DatabaseLoadError(OrbshackerError):
    """Não foi possível carregar o banco de dados de jogos de nenhuma fonte."""
