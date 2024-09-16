# E-commerce Backend Project

## Project Description

This project is a backend for an e-commerce system, implemented with SQLite as the database. It includes basic functionalities for managing orders, products and the shopping cart. The project consists of Python scripts for manipulating data in the database and automated tests to ensure code integrity.

## Instructions for Configuring and Running the Application

### Requirements

- Python 3.x
- SQLite (included in standard Python)

### Configuration

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

2. **Create and activate a virtual environment (optional, but recommended):**

```bash
python -m venv venv
source venv/bin/activate # For Windows: venv\Scripts\activate
```

3. **Install dependencies (if any):**

```bash
pip install -r requirements.txt
```

4. **Configure the database:**

The SQLite database will be created automatically when you run the tests or start the application for the first time. Make sure the `test_db.sqlite3` file does not exist in the folder before starting the tests.

### Running the Application

- **Add Product:**

Import the module and use the `add_product` function to add a new product to the database.

```python
from products import add_product
conn = sqlite3.connect('test_db.sqlite3')
add_product(conn, "Product Name", "Product Description", 20.0, 100)
```

- **Edit Product:**

Use the `edit_product` function to update an existing product.

```python
from products import edit_product
conn = sqlite3.connect('test_db.sqlite3')
edit_product(conn, 1, "New Name", "New Description", 30.0, 150)
```

- **Remove Product:**

Use the `remove_product` function to delete a product.

```python
from products import remove_product
conn = sqlite3.connect('test_db.sqlite3')
remove_product(conn, 1)
```

- **List Products:**

Use the `list_products` function to get all products.

```python
from products import list_products
conn = sqlite3.connect('test_db.sqlite3')
products = list_products(conn)
```

- **View Product by ID:**

Use the `view_product_by_id` function to get the details of a specific product.

```python
from products import view_product_by_id
conn = sqlite3.connect('test_db.sqlite3')
product = view_product_by_id(conn, 1)
```

## Instructions for Running the Tests

1. **Run the automated tests:**

Make sure the virtual environment is activated and all dependencies are installed. Then, run:

```bash
python -m unittest discover -s tests
```

This will run all the tests located in the `tests` folder and provide a report on the integrity of the code.

## Assumptions and Design Decisions

- **SQLite Database:** The project uses SQLite for simplicity and portability. Ideal for prototypes and small applications.
- **Basic Validations:** The product handling functions include basic validations to ensure that inputs are valid before performing database operations.
- **Automated Tests:** Automated tests were implemented to ensure that basic database operations work as expected and to verify the handling of invalid inputs.

## Learnings and Technologies Used

- **SQLite:** Used as a relational database management system.
- **Python:** Primary programming language for developing backend logic.
- **Unittest:** Testing framework to ensure code quality.
- **Validations and Access Control:** Basic implementations to ensure the integrity and security of data handled by the system.

---

If you have any questions or need more information, feel free to contact us or consult the additional documentation.