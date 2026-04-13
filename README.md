# 🛒 Cashier System Python

Sistema de caixa e gestão de mercado desenvolvido em Python, com operação via terminal. O projeto simula o fluxo completo de um pequeno estabelecimento: abertura de caixa, atendimento de clientes, emissão de nota fiscal, controle de estoque e um módulo administrativo (SIG) para consultas gerenciais.

---

## ✨ Funcionalidades

### 🧾 Módulo Caixa (`mercado.py`)
- Abertura e fechamento de caixa com resumo do expediente.
- Cadastro automático de clientes no primeiro atendimento (persistido em JSON).
- Adição de múltiplos itens por compra, com validação de estoque em tempo real.
- Geração de **nota fiscal agrupada** por produto utilizando `pandas`, com exibição formatada via `tabulate`.
- Baixa automática no estoque ao finalizar o atendimento.
- Relatório de produtos em falta ao final do expediente.

### 📊 Módulo Administrativo — SIG (`sig.py`)
- **Clientes:** consulta de compras por cliente, ranking dos que mais compram / mais gastam e listagem de clientes sem compras.
- **Produtos:** CRUD completo (listar, cadastrar, alterar, remover).
- **Consultas gerenciais:** produtos mais vendidos, menos vendidos, com pouco estoque e fornecedores por produto.

### 🌐 Integrações
- **Web Scraping** com `BeautifulSoup` e `requests` para importar o catálogo de produtos diretamente de uma página HTML.
- **Importação via Excel** (`openpyxl`) para carga inicial de produtos e fornecedores.
- **Persistência dupla:** banco SQLite (via SQLAlchemy ORM) + arquivos JSON/CSV para dados auxiliares.

---

## 🧱 Arquitetura

```
CashierSystemPython/
├── mercado.py              # Ponto de entrada do caixa
├── sig.py                  # Ponto de entrada do módulo administrativo
├── requirements.txt
│
├── caixa/                  # Fluxo operacional do caixa
│   ├── atendimento.py
│   ├── encerramento.py
│   └── menus.py
│
├── admin/                  # Módulo SIG (gestão)
│   ├── consultas_clientes.py
│   ├── consultas_produtos.py
│   ├── crud_produtos.py
│   ├── importar_clientes.py
│   ├── importar_excel.py
│   ├── importar_produtos.py
│   └── menus_admin.py
│
├── comum/                  # Infraestrutura compartilhada
│   ├── conexao_sql.py      # Engine / sessão SQLAlchemy
│   ├── constantes.py       # Constantes de menu e fluxo
│   ├── crud.py             # Operações genéricas de banco
│   ├── modelos.py          # Entidades ORM
│   └── utils.py
│
└── dados/                  # Camada de dados
    ├── banco.db            # Banco SQLite
    ├── carga_sig.xlsx      # Carga inicial (Excel)
    ├── clientes.json       # Persistência de clientes
    ├── produtos.csv        # Catálogo raspado da web
    ├── scraping_produtos.py
    └── sqlite_script.sql
```

### 🗃️ Modelo de Dados
O banco segue um modelo relacional com as entidades:
`Cliente`, `Produto`, `Compra`, `Item`, `Fornecedor` e `Fornecimento`, conectadas por chaves estrangeiras (ver `comum/modelos.py`).

---

## 🛠️ Tecnologias

| Categoria          | Ferramenta                              |
| ------------------ | --------------------------------------- |
| Linguagem          | Python 3                                |
| ORM / Banco        | SQLAlchemy + SQLite                     |
| Manipulação dados  | Pandas                                  |
| Planilhas          | openpyxl                                |
| Web Scraping       | BeautifulSoup4 + Requests               |
| Formatação CLI     | Tabulate                                |

---

## 🚀 Como executar

### Pré-requisitos
- Python 3.10 ou superior

### Instalação
```bash
git clone https://github.com/<seu-usuario>/CashierSystemPython.git
cd CashierSystemPython
pip install -r requirements.txt
```

### Executando o caixa
```bash
python mercado.py
```

### Executando o módulo administrativo (SIG)
```bash
python sig.py
```

> Na primeira execução, o `mercado.py` realiza automaticamente o scraping dos produtos e a importação dos clientes, populando o banco de dados.

---

## 🔄 Fluxo típico de uso

1. Execute `mercado.py` e abra o caixa.
2. Informe o ID do cliente (novos são cadastrados automaticamente).
3. Adicione os produtos desejados ao atendimento.
4. Finalize o atendimento — a nota fiscal agrupada é gerada e o estoque é atualizado.
5. Ao fechar o caixa, visualize o resumo e os produtos em falta.
6. Use `sig.py` para consultas gerenciais, CRUD de produtos e análise de clientes.

---

## 📌 Destaques técnicos

- **Separação de responsabilidades** em pacotes (`caixa`, `admin`, `comum`, `dados`).
- **Reutilização de código** via camada `comum` (CRUDs genéricos, modelos e utilitários).
- **ETL leve** integrando web scraping → CSV → banco relacional.
- **Agrupamento de itens repetidos** da nota fiscal com `pandas.groupby`, evitando linhas duplicadas na baixa de estoque.
- **Constantes centralizadas** para controle de menus, facilitando manutenção.

---

## 👤 Autor

**João Pedro**
Projeto desenvolvido como evolução contínua de estudos em Python, modelagem de dados e boas práticas de organização de código.
