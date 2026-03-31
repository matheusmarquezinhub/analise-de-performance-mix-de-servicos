"""
Módulo principal do projeto de Análise de Performance.

Este pacote contém funções reutilizáveis para análise de dados
e conexão com o banco de dados.
"""

__version__ = "1.0.0"
__author__ = "Seu Nome"

from .config import DatabaseConfig, AppConfig, validate_database_config

__all__ = [
    "DatabaseConfig",
    "AppConfig",
    "validate_database_config",
]
