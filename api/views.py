from django.shortcuts import render
from django.http import HttpResponse
from requests import RequestException
import requests
import base64
import environ
import json

# Create your views here.


def index(request):
    return HttpResponse("", content_type="application/json")


def products(request):
    env = environ.Env()
    src = '%s:%s' % (env('EMAIL'), env('SECRET_KEY'))
    token = 'Basic %s' % base64.b64encode(src.encode('utf-8')).decode('ascii')
    ITEMS_PER_PAGE = 10
    try:

        r = requests.get('https://gigastation.jp/api/products',
                         headers={'Authorization': token},
                         params={'items_per_page': ITEMS_PER_PAGE})
        t = r.text
        j = json.loads(r.text)
        # print(t)
        # j = json.dumps(r.text)
        print(len(j['products']))
        return HttpResponse(t, content_type="application/json")
    except RequestException as e:
        print(e)
