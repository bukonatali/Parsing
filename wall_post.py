# get Wall
import requests
import time
import csv

method = 'wall.post'
token = 'f31a8679f31a8679f31a86798ff008b7e6ff31af31a867990a592bb8deb66574e67e639'
version = 5.131
domain = 'foodrumedia'
count = 100
offset = 0
all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                })

        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        # time.sleep(0.5)
    return all_posts()

def file_writer(data):
    with open('foodrumedia', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['urls']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow((post['likes']['count'],post['text'], img_url ))

all_posts = take_1000_posts()
file_writer(all_posts)


print(1)