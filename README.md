# User Management API

API REST para gerenciamento de usuários, desenvolvida com **FastAPI**, utilizando **PostgreSQL**, **SQLAlchemy** e **JWT** para autenticação.  
O projeto também conta com uma **interface HTML simples** para demostração do fluxo de login e acesso a rotas protegidas.

Este repositório faz parte do meu **portfólio como desenvolvedor back-end**.

---

## Tecnologias Utilizadas

- Python 3.14
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Passlib (bcrypt)
- JWT (python-jose)
- Jinja2
- Uvicorn

---

## Funcionalidades

- Cadastro de usuários
- Hash seguro de senha com **bcrypt**
- Validação de dados com **Pydantic**
- Autenticação com **JWT**
- Proteção de rotas com **Bearer Token**
- Interface HTML simples para demonstração
- Tratamento de erros (credenciais inválidas, usuário não encontrado)

---

## Interface de Demonstração

O projeto possui uma interface HTML básica para facilitar a visualização do funcionamento da API.

Funcionalidades da interface:
- Login de usuário
- Armazenamento do token JWT no navegador
- Acesso a rota protegida (`/me`) usando autenticação Bearer

A interface pode ser acessada em:
http://127.0.0.1:8000/


---

## Autenticação (JWT)

### Login
Endpoint responsável por autenticar o usuário e gerar o token JWT:

POST /login

Exemplo de body:

{
  "email": "usuario@email.com",
  "password": "123456"
}

Resposta:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

Rota protegida

Exemplo de rota protegida por JWT:
GET /me

Header necessário:
Authorization: Bearer <access_token>

Resposta:
{
  "id": 1,
  "email": "usuario@email.com"
}

Estrutura do Projeto
user-management-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── auth.py
├── templates/
│   └── index.html
├── README.md
└── venv/

Como Executar o Projeto

1 - Clonar o repositório
git clone <URL_DO_REPOSITORIO>
cd user-management-api

2 - Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate

3 - Instalar dependências
pip install -r requirements.txt

4 - Executar a aplicação
python -m uvicorn app.main:app --reload

Acesse:

Interface: http://127.0.0.1:8000/

Swagger: http://127.0.0.1:8000/docs

Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

Boas práticas de back-end

Organização de código

Segurança básica com JWT

Demonstração prática de autenticação e autorização

Autor: Fernando Kleinau
Desenvolvedor Back-end em formação


