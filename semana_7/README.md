# Semana 07: Django Web

Este repositório contém o código e os recursos desenvolvidos como parte do estudo da Semana 07 do Bootcamp Back-End Python e Django.

## Status Atual

Resumo do progresso:

### Django Web

- [x] Fundamentos de arquitetura e o padrão MTV
  - "Framework é uma caixa de ferramentas";
  - MTV - Model (Banco de dados) | View (Camada Lógica de Visualização) | Template (Front-end);
  - MVC.
- [x] Diferença entre MTV e MVC
  - MVC - Model | View | Controller (Responsável pelo controle geral);
  - MTV (Django) - Laravel (MVC).
- [x] Django framework
- [x] Instalando o ambiente virtual e conhecendo nosso projeto
  - python -m venv nome_do_ambiente;
  - nome_do_ambiente\Scripts\Activate.ps1;
  - Deactivate;
  - Ambiente Virtual é para garantir que as instalações estejam locamente naquele diretório.
- [x] Instalando o Django e iniciando nosso primeiro aplicativo
  - Instalar o Django:
  `pip install django`
  - Iniciar o projeto:
  `django-admin startproject projeto_womakers .`
  - Inicializar o servidor
  `python manage.py runserver`
  - Criar a estrutura do padrão MVP
  `python manage.py startapp base`
  - Registrar o aplicativo instalado no 'settings.py'
- [x] Views
  - Views são funções do python para indicar quais funcionalidades vão ter o sistemas e vão responder as rotas bem definidas (URL);
  - Cada página de um sistema é representada por uma view.
- [x] URLs
- [x] Template parte 1
  - Cada página do sistema tem uma view e uma url.
- [x] Template parte 2
  `pip install django-bootstrap-v5`
  - Html fica em templates;
  - Css e JS fica em static.
- [x] Forms
  - Composto por três bases principais
- [x] Models e ModelForm
  - O banco de dados fica no arquivo models;
  - Models é como se fosse uma abstração;
  - Quando houver alteração no banco de dados, precisamos rodar os comandos de migração;
    - gera arquivo do que precisa ser enviado para o banco
    `python manage.py makemigrations`
    - envia as informações para o banco:
    `python manage.py migrate`
- [x] Filtros, buscas e admin
  `python manage.py createsuperuser`
  
Obrigada por visitar este repositório!
