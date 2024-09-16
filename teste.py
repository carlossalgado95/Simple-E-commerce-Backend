from users import create_user_table, register_user, login_user, list_users
from products import add_product, list_products
from cart import create_cart_table, add_to_cart, view_cart, remove_from_cart
from orders import create_orders_table, place_order

# Create tables (run only once)
create_user_table()
create_cart_table()
create_orders_table()

# User Registration Test
register_user('carlos', 'minhasenha')  # Must register user
register_user('admin', 'adminsenha')  # Must register admin

# Add product test
add_product('Produto 1', 'Descrição 1', 100.0, 10)  # Add more products as needed

# Test adding product to cart
add_to_cart(1, 1, 2)  # Add product to cart for user with ID 1

# View Cart Test
view_cart(1)  # Check if the product has been added to the cart
# Test placing order
place_order(1)  # Make a request for user with ID 1


list_users() # Testing listing users
