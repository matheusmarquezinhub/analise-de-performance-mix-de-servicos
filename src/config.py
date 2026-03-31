"""
Configurações centralizadas do projeto.

Este módulo carrega as variáveis de ambiente e fornece
configurações para conexão com o banco de dados.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)


class DatabaseConfig:
    """Configurações de conexão com o banco de dados."""

    SERVER = os.getenv("DB_SERVER")
    DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
    DATABASE = os.getenv("DB_DATABASE")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    TRUST_CERT = os.getenv("TRUST_CERT", "yes").lower() == "yes"

    # String de conexão para SQLAlchemy
    @classmethod
    def get_connection_string(cls) -> str:
        """Gera a string de conexão para o banco de dados."""
        trusted = "yes" if cls.TRUST_CERT else "no"
        conn_str = (
            f"mssql+pyodbc://{cls.USER}:{cls.PASSWORD}@{cls.SERVER}"
            f"/{cls.DATABASE}?driver={cls.DRIVER}&TrustServerCertificate={trusted}"
        )
        return conn_str


class AppConfig:
    """Configurações gerais da aplicação."""

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    PROJECT_NAME = "Análise de Performance - Mix de Serviços"
    PROJECT_VERSION = "1.0.0"


def validate_database_config() -> bool:
    """
    Valida se as configurações de banco de dados estão corretas.

    Returns:
        bool: True se todas as configurações estão presentes, False caso contrário.
    """
    required_fields = [
        DatabaseConfig.SERVER,
        DatabaseConfig.DATABASE,
        DatabaseConfig.USER,
        DatabaseConfig.PASSWORD,
    ]

    return all(required_fields)
