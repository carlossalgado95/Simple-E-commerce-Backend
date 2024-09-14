from users import create_user_table, register_user, login_user, list_users
from products import add_product, list_products
from cart import create_cart_table, add_to_cart, view_cart, remove_from_cart
from orders import create_orders_table, place_order

# Criar tabelas (execute apenas uma vez)
create_user_table()
create_cart_table()
create_orders_table()

# Teste de registro de usuário
register_user('carlos', 'minhasenha')  # Deve registrar o usuário
register_user('admin', 'adminsenha')  # Deve registrar o admin

# Teste de adicionar produto
add_product('Produto 1', 'Descrição 1', 100.0, 10)  # Adicione mais produtos conforme necessário

# Teste de adicionar produto ao carrinho
add_to_cart(1, 1, 2)  # Adicionar produto ao carrinho do usuário com ID 1

# Teste de visualizar carrinho
view_cart(1)  # Verifique se o produto foi adicionado ao carrinho

# Teste de colocar pedido
place_order(1)  # Fazer um pedido para o usuário com ID 1

# Teste de listar usuários
list_users()
