import requests
from celery import shared_task
from main.utils.pg import Pg
from main.utils.mongo import Mongo

@shared_task
def fetch_and_store_users(count:int):
    """
    Task to fetch and store users data from API
    """

    print(f'Task # {count+1} executing')

    # Fetch data from API
    
    response = requests.get('https://fakestoreapi.com/users')
    data = response.json()

    # Store data in PostgreSQL database

    pg_obj = Pg()
    pg_obj.store_data(data)

    # Store data in MongoDB collection

    mongo_obj = Mongo()
    mongo_obj.store_data(data)

from django.core.cache import cache
from main.models import Product

def get_product(product_id):
    """
    Get Product Id from Cache or from DB if misses Cache
    """

    cache_key = f'product_{product_id}'

    product = cache.get(cache_key)

    if product is None:

        print('Cache not found. Getting product from DB')

        product = Product.objects.filter(id=product_id).values()[0]
        
        if product is not None:
            cache.set(cache_key, product)

        return product
    
    else:
        
        print('Cache found. Returning cached product.')
        
        return product