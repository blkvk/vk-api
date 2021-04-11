import base64
import os
import time
from collections import Counter
from io import BytesIO

import matplotlib.pyplot as plt
import requests
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()

plt.switch_backend('Agg')
VK_TOKEN = os.getenv('TOKEN')
api_v = 5.92
BASE_URL = 'https://api.vk.com/method/'
POST_METHOD_URL = 'wall.get/'
COMMENTS_METHOD_URL = 'wall.getComments/'


def analize(request):
    owner_id = request.GET['owner_id']
    data = {'access_token': VK_TOKEN,
            'v': api_v,
            'owner_id': owner_id,
            'count': 10,
            }
    response = requests.post(BASE_URL+POST_METHOD_URL, data=data)
    posts = response.json()['response']['items']
    posts_id = []
    for i in posts:
        posts_id.append(i['id'])

    del data['count']
    comments = {}
    authors_id = []
    for i in posts_id:
        data['post_id'] = i
        response1 = requests.post(BASE_URL+COMMENTS_METHOD_URL, data=data)
        print(response1.json())
        post_comments = response1.json()['response']['items']
        for j in post_comments:
            authors_id.append(j['from_id'])
        comments[i] = authors_id
        time.sleep(1)

    graphic = pie_graphic(authors_id)
    return render(request, 'mari/analize.html', {'graphic': graphic})


def pie_graphic(authors_id):
    count = dict(Counter(authors_id).most_common())
    labels = list(count.keys())
    values = list(count.values())
    print(count)
    plt.pie(values, labels=labels)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return graphic


def index(request):
    return render(request, 'mari/index.html')
