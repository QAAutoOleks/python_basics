import sqlite3


class DatabaseGit():

    def __init__(self):
        self.connection = sqlite3.connect(
            # r"C:\\Users\\User\\Desktop\\python_basics\\" + r"become_qa_auto.db"
            r"C:\\Users\\User\\Desktop\\python_basics\\" + r"python_basics_database.db"
        )
        self.cursor = self.connection.cursor()

    def create_table_customers(self):
        # if table 'customers' exists, query 'DROP TABLE' deletes it
        self.cursor.execute("DROP TABLE IF EXISTS customers")
        table = """CREATE TABLE customers (
            id.customers INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(255) NOT NULL,
            first_name CHAR(25) NOT NULL,
            last_name CHAR(25),
            FOREIGN KEY (id.customers) REFERENCES orders (id.orders)
        )"""
        self.cursor.execute(table)
        print("Ready")

    def create_table_orders(self):
        # if table 'customers' exists, query 'DROP TABLE' deletes it
        self.cursor.execute("DROP TABLE IF EXISTS orders")
        table = """CREATE TABLE orders (
            id.orders INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            date_and_time CHAR(25) NOT NULL,
            FOREIGN KEY (id.orders) REFERENCES customers (id.customers)
        )"""
        self.cursor.execute(table)
        print("Ready")

    def insert_in_table_customers(self, email, first_name, last_name):
        query = f"INSERT OR REPLACE INTO customers \
            (email, first_name, last_name) \
                VALUES ('{email}', '{first_name}', '{last_name}')"
        self.cursor.execute(query)
        self.connection.commit()   

    def insert_in_table_orders(self, name, date_and_time):
        date_and_time = str(date_and_time)
        query = f"INSERT OR REPLACE INTO orders (name, date_and_name) \
            VALUES ('{name}', '{date_and_name}')"
        self.cursor.execute(query)
        self.connection.commit()     

    def get_data(self, name):
        query = f"SELECT email FROM customers WHERE first_name = '{name}'"            
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

base = DatabaseGit()
base.create_table_customers()
base.insert_in_table_customers('mark.twain@mail.com', 'Mark', 'Twain')
print(base.get_data('Mark'))
# insert_empty_email = base.insert_in_table(None, 'Nicola', 'Tesla')
# print(base.get_data('Nicola'))



