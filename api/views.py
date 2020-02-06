from django.shortcuts import render
from django.http import HttpResponse
from requests import RequestException
import requests
import base64

# Create your views here.


def index(request):
    return HttpResponse("", content_type="application/json")


def products(request):
    src = '%s:%s' % ('DUMMY',
                     'DUMMY')
    token = 'Basic %s' % base64.b64encode(src.encode('utf-8')).decode('ascii')
    print(token)
    try:
        r = requests.get('https://gigastation.jp/api/products',
                         headers={
                             'Authorization': token},
                         params={'items_per_page': 5000})
        return HttpResponse(r, content_type="application/json")
    except RequestException as e:
        print(e)
