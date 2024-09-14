# Projeto E-commerce Backend

## Descrição do Projeto

Este projeto é um backend para um sistema de e-commerce, implementado com SQLite como banco de dados. Ele inclui funcionalidades básicas para gerenciar pedidos, produtos e o carrinho de compras. O projeto é composto por scripts Python para manipulação de dados no banco de dados e testes automatizados para garantir a integridade do código.

## Instruções para Configuração e Execução da Aplicação

### Requisitos

- Python 3.x
- SQLite (incluso no Python padrão)

### Configuração

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seuusuario/seurepositorio.git
    cd seurepositorio
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```

3. **Instale as dependências (se houver):**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados:**

    O banco de dados SQLite será criado automaticamente quando você executar os testes ou iniciar a aplicação pela primeira vez. Certifique-se de que o arquivo `test_db.sqlite3` não exista na pasta antes de iniciar os testes.

### Execução da Aplicação

- **Adicionar Produto:**

    Importe o módulo e use a função `add_product` para adicionar um novo produto ao banco de dados.

    ```python
    from products import add_product
    conn = sqlite3.connect('test_db.sqlite3')
    add_product(conn, "Nome do Produto", "Descrição do Produto", 20.0, 100)
    ```

- **Editar Produto:**

    Use a função `edit_product` para atualizar um produto existente.

    ```python
    from products import edit_product
    conn = sqlite3.connect('test_db.sqlite3')
    edit_product(conn, 1, "Novo Nome", "Nova Descrição", 30.0, 150)
    ```

- **Remover Produto:**

    Use a função `remove_product` para deletar um produto.

    ```python
    from products import remove_product
    conn = sqlite3.connect('test_db.sqlite3')
    remove_product(conn, 1)
    ```

- **Listar Produtos:**

    Use a função `list_products` para obter todos os produtos.

    ```python
    from products import list_products
    conn = sqlite3.connect('test_db.sqlite3')
    products = list_products(conn)
    ```

- **Visualizar Produto por ID:**

    Use a função `view_product_by_id` para obter os detalhes de um produto específico.

    ```python
    from products import view_product_by_id
    conn = sqlite3.connect('test_db.sqlite3')
    product = view_product_by_id(conn, 1)
    ```

## Instruções para Execução dos Testes

1. **Execute os testes automatizados:**

    Certifique-se de que o ambiente virtual esteja ativado e que todas as dependências estejam instaladas. Então, execute:

    ```bash
    python -m unittest discover -s tests
    ```

    Isso executará todos os testes localizados na pasta `tests` e fornecerá um relatório sobre a integridade do código.

## Assumptions e Decisões de Design

- **Banco de Dados SQLite:** O projeto utiliza SQLite para simplicidade e portabilidade. Ideal para protótipos e aplicações pequenas.
- **Validações Básicas:** As funções para manipulação de produtos incluem validações básicas para garantir que as entradas sejam válidas antes de executar operações no banco de dados.
- **Testes Automatizados:** Testes automatizados foram implementados para garantir que as operações básicas do banco de dados funcionem conforme o esperado e para verificar a manipulação de entradas inválidas.

## Aprendizados e Tecnologias Usadas

- **SQLite:** Utilizado como sistema de gerenciamento de banco de dados relacional.
- **Python:** Linguagem de programação principal para desenvolvimento da lógica de backend.
- **Unittest:** Framework de testes para garantir a qualidade do código.
- **Validações e Controle de Acesso:** Implementações básicas para garantir a integridade e segurança dos dados manipulados pelo sistema.

---

Se você tiver alguma dúvida ou precisar de mais informações, sinta-se à vontade para entrar em contato ou consultar a documentação adicional.

