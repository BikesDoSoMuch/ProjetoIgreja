# ProjetoIgreja

Sistema web desenvolvido em **Django** para gerenciar famílias atendidas por uma instituição religiosa, incluindo cadastro, edição, exclusão e exportação de dados em CSV.


## Funcionalidades do Sistema

- Listagem de famílias cadastradas com paginação;
- Cadastro de novas famílias;
- Edição e exclusão de famílias existentes;
- Visualização detalhada de cada família;
- Exportação de dados das famílias em formato CSV;
- Filtros por ano/mês e programas sociais;
- Busca por nome, endereço e telefone.


## Tecnologias utilizadas

- **Backend:** Python 3.12, Django 5.2.7  
- **Banco de dados:** SQLite (padrão Django)  
- **Frontend:** HTML5, Bootstrap 5  
- **Controle de versões:** Git  

---

## Estrutura do projeto:
A estrutura segue o padrão **MVC/MTV do Django**:

ProjetoIgreja/
│
├── igreja/ # Configurações globais do projeto
│ ├── settings.py # Configurações do Django
│ ├── urls.py # URLs globais
│ └── wsgi.py # WSGI para deploy
│
├── familias/ # Aplicação de gerenciamento de famílias
│ ├── migrations/ # Histórico de migrações do banco
│ ├── templates/ # Templates HTML (família_list, form, detail)
│ │ └── familias/
│ │ ├── familia_list.html
│ │ ├── familia_form.html
│ │ ├── familia_detail.html
│ │ └── familia_confirm_delete.html
│ ├── admin.py # Configuração do Django Admin
│ ├── models.py # Modelos (ex.: Família)
│ ├── forms.py # Formulários Django
│ ├── views.py # Views (List, Create, Update, Delete, Detail, Export CSV)
│ └── urls.py # URLs da aplicação
│
├── db.sqlite3 # Banco de dados SQLite
├── manage.py # Script de gerenciamento do Django
└── README.md # Este arquivo

## Como Rodar o Projeto

# 1. Clone o repositório

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows (descomente se usar Windows)

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute as migrações do banco de dados
python manage.py migrate

# 5. Crie um superusuário para acessar o Django Admin
python manage.py createsuperuser

    # meu usuario: laura
    # senha: 123

# 6. Rode o servidor de desenvolvimento
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser   # se necessário
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt || pip install "Django==5.2.7"
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# 7. Acesse o sistema pelo navegador
# Abra: http://127.0.0.1:8000/
