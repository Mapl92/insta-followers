from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re
import json
from django.http import JsonResponse

def count(request,username):
    url = 'https://www.instagram.com/{}'.format(username)
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    script_tag = soup.find('script', text=re.compile('window\._sharedData'))
    shared_data = script_tag.string.partition('=')[-1].strip(' ;')
    json_data = json.loads(shared_data)
    count = json_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']

    data = {
        'count':count
    }
    return JsonResponse(data)