# Sistema ERP EntreIrmaos - Controle de Estoque para Doações

Um Sistema ERP (Enterprise Resource Planning) simples e eficiente desenvolvido para a instituição beneficente **Conexão Entre Irmãos**. Este sistema tem como objetivo principal controlar o fluxo de doações (entradas) e saídas do estoque de forma intuitiva, mantendo um armazenamento local através de planilhas Excel.

## 🌟 Objetivo Social
O **EntreIrmaos** auxilia no gerenciamento dos itens arrecadados e destinados a pessoas em situação de vulnerabilidade, oferecendo painéis e controles para garantir transparência, disponibilidade de estoque e rastreabilidade nas saídas e entradas de roupas, alimentos, itens de higiene e limpeza.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**: Linguagem principal do backend.
- **Flask (v3.0+)**: Framework web utilizado para as rotas e regras de negócio.
- **Pandas (v2.2+) & Openpyxl (v3.1+)**: Manipulação de dados e gravação na planilha .xlsx.
- **FileLock (v3.13+)**: Controle seguro de concorrência de acesso ao arquivo de banco de dados.
- **HTML5, CSS3, JS Puro**: Frontend do sistema com identidade visual personalizada e design responsivo.

## 📋 Pré-requisitos
Para rodar este projeto, você precisa ter instalado no seu sistema:
- Python 3.10 ou superior
- Pip (gerenciador de pacotes do Python)

## 🚀 Instalação Passo a Passo

1. **Clone ou extraia o repositório** para uma pasta local:
   `ash
   cd Projeto-Estoque-EntreIrmaos
   `

2. **Crie um ambiente virtual (Recomendado)**:
   `ash
   python -m venv venv
   # Ative o ambiente virtual (Windows)
   venv\Scripts\activate
   # Ative o ambiente virtual (Linux/macOS)
   source venv/bin/activate
   `

3. **Instale as dependências** listadas no arquivo equirements.txt:
   `ash
   pip install -r requirements.txt
   `

## ▶️ Como Executar o Sistema

1. Com o ambiente virtual ativado (e as dependências instaladas), rode o servidor:
   `ash
   python app.py
   `
2. Após iniciar, acesse o sistema no seu navegador:
   **[http://localhost:5000](http://localhost:5000)**

## 🔍 Descrição de Cada Seção do Sistema

* **Painel (Dashboard):** Visão geral de todos os itens cadastrados no estoque com os seus status (Estável, Atenção ou Sem itens). Os cards superiores resumem o total de itens no Instituto e no Bazar.
* **Entrada (Doações):** Interface para registro de novos produtos no estoque. Caso o produto (mesmo nome e local) já exista, sua quantidade será apenas acrescida de forma inteligente. Há campos dinâmicos adicionais, dependendo da categoria do produto (ex: Roupas ou Alimentos).
* **Baixa (Saídas):** Tela para registro da retirada de itens. É obrigatório registrar o nome e telefone do responsável por essa retirada, atualizando assim essas informações para o histórico na planilha.

## 📁 Estrutura de Pastas

`	ext
Projeto-Estoque-EntreIrmaos/
│
├── app.py                        ← Ponto de entrada do Servidor Flask
├── requirements.txt              ← Lista das bibliotecas Python utilizadas
├── estoque.xlsx                  ← Gerado automaticamente na 1ª execução, é o nosso Banco de Dados
├── estoque.xlsx.lock             ← Arquivo de trava criado ao manipular o Excel
│
├── services/
│   ├── lock_excel.py             ← Context Manager para filelock (protege escrita simultânea)
│   └── estoque_service.py        ← Lógica principal das operações (CRUD) e cálculos
│
├── templates/
│   ├── base.html                 ← Template base do layout visual (header, nav)
│   ├── painel.html               ← Visualização da tabela e dos cards informativos
│   ├── entrada.html              ← Formulário condicional de novas doações
│   └── baixa.html                ← Formulário de saídas do sistema
│
├── static/
│   ├── css/
│   │   └── style.css             ← Estilos visuais integrados, com adição de cores para flash messages
│   ├── js/
│   │   └── script.js             ← Lógica de frontend e campos condicionais
│   └── img/
│       └── logo-conexao-entre-irmaos.jpg ← Logo principal da aplicação
│
└── README.md                     ← Este arquivo
`

## 🔒 Nota sobre o Arquivo .lock
Durante o uso normal do sistema, será criado o arquivo estoque.xlsx.lock. Ele garante que requisições ou processos simultâneos não corrompam o arquivo do Excel ao salvar ou dar baixa ao mesmo tempo. Nunca apague este arquivo manualmente enquanto o sistema estiver ativo.

---
*Projeto acadêmico e social desenvolvido para a instituição **Conexão Entre Irmãos**.*
