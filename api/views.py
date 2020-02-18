from django.shortcuts import render
from django.http import HttpResponse
from requests import RequestException
import requests
import base64
import environ
import json

# Create your views here.
env = environ.Env()


def index(request):
    return HttpResponse("", content_type="application/json")


def products(request):
    # env = environ.Env()
    # src = '%s:%s' % (env('EMAIL'), env('SECRET_KEY'))
    # token = 'Basic %s' % base64.b64encode(src.encode('utf-8')).decode('ascii')
    # token = generateToken(from
    ITEMS_PER_PAGE = 10
    url = apiUrl()
    # headers = {'Authorization': token}
    try:
        # get number of total records
        session = request.Session()
        session.headers.update(requestHeader())
        count = session.get(url, params={'items_per_page': 1})
        total_count = count.json()['params']['total_count']
        total_count = int(total_count)
        # num_of_loop = -(-total_count // ITEMS_PER_PAGE)
        num_of_loop = 1
        for page in range(1, num_of_loop):
            r = session.get(
                url, params={'items_per_page': ITEMS_PER_PAGE, 'page': page})
            print(page)

        # t = r.text
        # j = json.loads(r.text)
        # print(t)
        # j = json.dumps(r.text)
        print(len(j['products']))
        return HttpResponse(t, content_type="application/json")
    except RequestException as e:
        print(e)


def apiUrl():
    return env('CSCART_API_URL')


def requestHeader():
    src = '%s:%s' % (env('EMAIL'), env('SECRET_KEY'))
    token = 'Basic %s' % base64.b64encode(src.encode('utf-8')).decode('ascii')
    return {'Authorization': token}
