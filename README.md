## Gerenciador de Notícias 🗞️
API construída com FastAPI para gerenciar notícias. A estrutura dos dados é validada usando Pydantic e suas principais funcionalidades são: cadastro, edição, remoção e listagem de dados.

## Pré-requisitos 📋
- Python (preferencialmente 3.8 ou superior);
- Bibliotecas: FastAPI, Pydantic, Uvicorn.

## Instalação ⚙️
1. **Clonar o repositório:**
   ```sh
   git clone <https://gitlab.com/back-end3322036/GerenciadorDeNoticias.git>
   cd <NOME_DO_REPOSITORIO>
   ```

2. **Criar e ativar um ambiente virtual:**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Executar a aplicação:**
   ```sh
   uvicorn main:app --reload
   ```

5. **Acessar a documentação da API:**
   - Abra um navegador e vá para `http://127.0.0.1:8000/docs`.

## Utilizando a API 🚀
A API possui 4 rotas principais:

- **POST /cadastrar**: Cadastra uma nova notícia.
    1. Em 'http://127.0.0.1:8000/docs`, selecione o método POST;
    2. Selecione "Try it out";
    3. Edite o JSON;
    4. Clique em Execute.  

- **GET /listar**: Retorna todas as notícias cadastradas.
    1. Vá para a rota `/listar`.

- **GET /listar/{id}**: Retorna uma notícia específica.
    1. Vá para a rota `/listar/{id}`.

- **PUT /editar/{id}**: Edita uma notícia existente.
    1. Em 'http://127.0.0.1:8000/docs`, selecione o método PUT;
    2. Selecione "Try it out";
    3. Edite o JSON;
    4. Clique em Execute.

- **DELETE /deletar/{id}**: Remove uma notícia existente.
    1. Em 'http://127.0.0.1:8000/docs`, selecione o método DELETE;
    2. Selecione "Try it out";
    3. Edite o JSON;
    4. Clique em Execute.
