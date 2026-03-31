# Análise de Performance - Mix de Serviços 📊

Uma análise completa de performance e rentabilidade dos serviços, com visualizações interativas e insights de mix de produtos.

## 🎯 Objetivo

Este projeto realiza uma análise detalhada do desempenho de diferentes serviços, identificando padrões de rentabilidade, composição do mix de produtos e tendências ao longo do tempo.

## ⚠️ Dados de Teste

**Os dados exibidos nos outputs deste projeto são FAKES (dados simulados para demonstração).** Este é um projeto de exemplo e prototipagem. Para uso em produção, conecte-o a um banco de dados real alterando as credenciais no arquivo `.env`.

## 📋 Pré-requisitos

- Python 3.8+
- pip ou conda
- Acesso ao banco de dados SQL configurado no `.env`

## 🚀 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/analise-de-performance-mix-de-servicos.git
cd analise-de-performance-mix-de-servicos
```

### 2. Configure o ambiente

Crie um arquivo `.env` na raiz do projeto (use `.env.example` como referência):
```bash
cp .env.example .env
```

Edite o `.env` com suas credenciais de banco de dados:
```
DB_SERVER=seu-servidor
DB_DRIVER=seu-driver
DB_DATABASE=seu-banco
DB_USER=seu-usuario
DB_PASSWORD=sua-senha
TRUST_CERT=yes/no
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a análise

Abra o Jupyter Notebook:
```bash
jupyter notebook notebooks/analise_performance.ipynb
```

Ou use VSCode com a extensão Jupyter.

## 📦 Estrutura do Projeto

```
├── notebooks/
│   └── analise_performance.ipynb    # Análise principal com visualizações
├── src/
│   └── config.py                    # Configurações e funções reutilizáveis
├── docs/
│   └── README.md                    # Documentação adicional
├── requirements.txt                 # Dependências do projeto
├── .env.example                     # Template de variáveis de ambiente
├── .gitignore                       # Arquivos a ignorar no Git
└── README.md                        # Este arquivo
```

## 📊 O que a análise inclui

- ✅ Carregamento de dados do SQL Server
- ✅ Limpeza e transformação de dados
- ✅ Análise de performance por período
- ✅ Visualização de mix de serviços (Pie/Sunburst charts)
- ✅ Identificação de melhores e piores períodos
- ✅ Cálculo de métricas-chave (ticket médio, taxa, repasse, resíduo)
- ✅ Geração de relatórios interativos com Plotly

## 🔧 Dependências Principais

- **pandas** - Manipulação e análise de dados
- **SQLAlchemy** - ORM para conexão com SQL Server
- **pyodbc** - Driver ODBC para SQL Server
- **plotly** - Visualizações interativas
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## ⚠️ Segurança

⚠️ **NUNCA** faça commit do arquivo `.env` - ele contém credenciais sensíveis!

Use o arquivo `.env.example` como template e mantenha `.env` no `.gitignore`.

## 📝 Licença

MIT

## 👤 Autor

Matheus Marquezin | https://github.com/matheusmarquezinhub

## 💬 Contribuindo

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro.

