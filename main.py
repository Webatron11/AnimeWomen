# https://gist.github.com/slavakurilyak/d3418446179f98cde5b7d6b53eefa09d

# https://github.com/cat-milk/Anime-Girls-Holding-Programming-Books

# https://stackoverflow.com/questions/63252337/how-to-open-and-display-images-from-a-github-repository#

from PIL import Image
import requests
from io import BytesIO
import random
import os
from dotenv import load_dotenv

load_dotenv('config.env')
Bearer = 'Bearer ' + os.getenv('HEADER')
headers = {'Authorization': Bearer}

data = requests.get('https://api.github.com/repos/cat-milk/Anime-Girls-Holding-Programming-Books/contents/', headers=headers)
ghJson = data.json()
folders = []


for x in ghJson:
    if not x['path'].__contains__("."):
        data2 = requests.get(x['url'], headers=headers)
        ghJson2 = data2.json()
        for x2 in ghJson2:
            folders.append(x2["download_url"])

print(len(folders))

url = folders[random.randint(0, len(folders)-1)]

response = requests.get(url)
img = Image.open(BytesIO(response.content))

img.show()
