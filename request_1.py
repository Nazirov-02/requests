import requests
import psycopg2

data_base = {'host':'localhost',
             'database':'month_5',
             'user':'postgres',
             'password':'KA1275147',
             'port':5432}

url = 'https://dummyjson.com/products'
r = requests.get(url)

# Connect database and create posts table

def create_table():
    with psycopg2.connect(**data_base) as conn:
     with conn.cursor() as curr:
         curr.execute("""CREATE TABLE IF NOT EXISTS posts(
         id serial primary key,
         title varchar(255),
         description text,
         category varchar(30),
         price numeric,
         rating numeric,
         stock int); """)
         conn.commit()
         print('Table successfully created')

# Connect posts table and add data

def add_data(products):
    if r.status_code == 200:
        with psycopg2.connect(**data_base) as conn:
            with conn.cursor() as curr:
                query = """INSERT INTO posts(title,description,category,price,rating,stock)
                           Values(%s,%s,%s,%s,%s,%s);"""
                products = r.json()
                for i in products['products']:
                  data = (i['title'],i['description'],i['category'],i['price'],i['rating'],i['stock'])
                  curr.execute(query,data)
                  conn.commit()
                print('data successfully added')

# create_table()
# add_data(r)
