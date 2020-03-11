from django.shortcuts import render
from django.http import HttpResponse
from requests import RequestException
import requests
import base64
import environ
import json

# Create your views here.
env = environ.Env()
ITEMS_PER_PAGE = 10


def index(request):
    return HttpResponse("", content_type="application/json")


def products(request):

    try:
        total_count = getTotalItems()
        # num_of_loop = -(-total_count // ITEMS_PER_PAGE)
        num_of_loop = 1
        for page in range(1, num_of_loop):
            records = getProducts(page=page)
            for item in records:
                saveProduct(item)
                print(item)

        return HttpResponse("Successs", content_type="application/json")
    except RequestException as e:
        print(e)


def saveProduct(product):
    if not Product.exists():
        Product.create_table(read_capacity_units=1,
                             write_capacity_units=1, wait=True)
    Product.save(product)


def getTotalItems():
    return getResponse(items_per_page=1).json()['params']['total_items']


def getResponse(items_per_page=ITEMS_PER_PAGE, page=1):
    session = requests.Session()
    session.headers.update(requestHeader())
    r = session.get('%s/%s' % (apiUrl(), '/products'), params={
                    'items_per_page': items_per_page, 'page': page})
    return r


def getProducts(items_per_page=ITEMS_PER_PAGE, page=1):
    return getResponse(items_per_page, page).json()['products']


def apiUrl():
    return env('CSCART_API_URL')


def requestHeader():
    src = '%s:%s' % (env('EMAIL'), env('SECRET_KEY'))
    token = 'Basic %s' % base64.b64encode(src.encode('utf-8')).decode('ascii')
    return {'Authorization': token}
