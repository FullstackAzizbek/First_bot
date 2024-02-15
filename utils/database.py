import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_categories(self):
        categories = self.cursor.execute(
            "SELECT id, category_name FROM categories;"
        )
        return categories.fetchall()

    def get_products(self, cat_id):
        products = self.cursor.execute(
            "SELECT id, product_name, product_price, product_desc, product_image FROM products WHERE product_category=?;", (cat_id,)
        )
        return products.fetchall()
