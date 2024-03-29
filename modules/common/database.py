import sqlite3


class DatabaseGit:
    def __init__(self):
        self.connection = sqlite3.connect(
            # r"C:\\Users\\User\\Desktop\\python_basics\\" + r"become_qa_auto.db"
            r"C:\\Users\\User\\Desktop\\python_basics\\"
            + r"python_basics_database.db"
        )
        self.cursor = self.connection.cursor()

    def create_table_customers(self):
        # if table 'customers' exists, query 'DROP TABLE' deletes it
        self.cursor.execute("DROP TABLE IF EXISTS customers")
        table = """CREATE TABLE customers (
            id_customers INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(255) NOT NULL,
            first_name CHAR(25) NOT NULL,
            last_name CHAR(25),
            FOREIGN KEY (id_customers) REFERENCES orders (id_orders)
        )"""
        self.cursor.execute(table)
        print("Ready")

    def create_table_orders(self):
        # if table 'customers' exists, query 'DROP TABLE' deletes it
        self.cursor.execute("DROP TABLE IF EXISTS orders")
        table = """CREATE TABLE orders (
            id_orders INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            date_and_time CHAR(25) NOT NULL,
            orders_id INTEGER,
            FOREIGN KEY (orders_id) REFERENCES customers (id_customers)
        )"""
        self.cursor.execute(table)
        print("Ready")

    def insert_in_table_customers(self, email, first_name, last_name):
        query = f"INSERT OR REPLACE INTO customers \
            (email, first_name, last_name) \
                VALUES ('{email}', '{first_name}', '{last_name}')"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_in_table_orders(self, name, date_and_time, orders_id):
        date_and_time = str(date_and_time)
        query = f"INSERT OR REPLACE INTO orders (name, date_and_time, orders_id) \
            VALUES ('{name}', '{date_and_time}', {orders_id})"
        self.cursor.execute(query)
        self.connection.commit()

    def get_data_customers(self, name):
        query = f"SELECT id_customers FROM customers WHERE first_name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_data_orders(self, name):
        query = f"SELECT orders_id FROM orders WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def inner_join_customers_orders(self):
        sql = """SELECT email, first_name, last_name
        FROM customers  
        INNER JOIN orders 
        ON customers.id_customers = orders.orders_id
        WHERE id_customers = 1;"""
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall() 
        for row in self.result: 
            print(row) 


base = DatabaseGit()
base.create_table_customers()
base.insert_in_table_customers("mark.twain@mail.com", "Mark", "Twain")
base.insert_in_table_customers("daniel.defoe@mail.com", "Daniel", "Defoe")
print(base.get_data_customers("Mark"))
# insert_empty_email = base.insert_in_table(None, 'Nicola', 'Tesla')
# print(base.get_data('Nicola'))
base.create_table_orders()
base.insert_in_table_orders("Phone SAMSUNG", "1/22/2024", 1)
base.insert_in_table_orders("Phone SAMSUNG", "2/22/2024", 2)
base.insert_in_table_orders("Laptop HP", "12/12/2023", 2)
base.insert_in_table_orders("Charger SAMSUNG", "1/20/2024", 1)
print(base.get_data_orders("Phone SAMSUNG"))
print(base.get_data_orders("Charger SAMSUNG"))
base.inner_join_customers_orders()
