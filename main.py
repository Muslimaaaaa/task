import psycopg2 as psql

class Database:
    @staticmethod
    def connect(query: str, query_type:str): #databaseni konnekt qilish
        fld = psql.connect(
            database = 'market_1',
            user = 'postgres',
            password = 'muslima2004',
            host = 'localhost',
            port = '5432'
        )
        cursor = fld.cursor()
        cursor.execute(query)
        data = ['create', 'insert', 'alter', 'update', 'delete']
        if query_type in data:
            fld.commit()
            if query_type == 'create':
                return f"created successfully"
            return f"{query_type} query successfully"
        else:
            return cursor.fetchall()

class Check:
    @staticmethod
    def login_check(username: str, password: str):
        query = f"SELECT * FROM customers WHERE username = '{username}' and password = '{password}'"
        data = Database.connect(query, "select")
        if len(data) == 1:
            return True

        else:
            return False
def add_column():
    # query_1 = "ALTER TABLE customers ADD COLUMN username VARCHAR(20)"
    # query_2 = "ALTER TABLE customers ADD COLUMN password VARCHAR(20)"
    # Database.connect(query_1, "alter")
    # Database.connect(query_2, "alter")

    query = f"""
            INSERT INTO customers(first_name, last_name, username, password, birth_date) 
            VALUES('Guli', 'Axmedova', 'guli12', 'guli4530', '2002-02-14')"""
    return Database.connect(query, "insert")





