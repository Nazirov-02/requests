import json
import threading
import time

import requests

url_posts = 'https://jsonplaceholder.typicode.com/posts'
url_products = 'https://dummyjson.com/products'

# Requests data and add json file

def add_posts(url):
    posts = requests.get(url)
    if posts.status_code == 200:
        with open('posts.json','w') as f:
            json.dump(posts.json(),f,indent = 4)
            print('data successfully added')

# Requests data and add json file

def add_products(url):
    products = requests.get(url)
    if products.status_code == 200:
        with open('products.json','w') as f:
            json.dump(products.json(),f, indent = 4)
            print('products data successfully added')

# Calls function by Threading method

posts = threading.Thread(target=add_posts,args=(url_posts,))
products = threading.Thread(target=add_products,args=(url_products,))

# posts.start()
# time.sleep(1)
# products.start()
# posts.join()
# products.join()