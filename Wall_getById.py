import requests
import time
import csv

def get_by_id_100():
    token = 'f31a8679f31a8679f31a86798ff008b7e6ff31af31a867990a592bb8deb66574e67e639'
    version = 5.131
    domain = 'foodrumedia'
    posts = 0
    extended = 0
    all_posts = []

    while extended < 1000:
        response = requests.get('https://api.vk.com/method/wall.getById',
                            params={
                            'access_token': token,
                            'v': version,
                            'domain': domain,
                            'posts': posts,
                            'extended': extended
                            })

        data = response.json()['response']['items']
        all_posts.extend(data)
    return all_posts()
all_posts = get_by_id_100()











