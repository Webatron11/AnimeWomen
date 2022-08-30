# https://github.com/cat-milk/Anime-Girls-Holding-Programming-Books
# https://stackoverflow.com/questions/63252337/how-to-open-and-display-images-from-a-github-repository#

from PIL import Image
import requests
from io import BytesIO
import random
import os
from os.path import exists
import pickle
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv('config.env')
Bearer = 'Bearer ' + os.getenv('HEADER')
headers = {'Authorization': Bearer}

folders = []

if exists('folders.txt'):
    with open('folders.txt', 'rb') as f:
        folders = pickle.load(f)
else:
    data = requests.get('https://api.github.com/repos/cat-milk/Anime-Girls-Holding-Programming-Books/contents/', headers=headers)
    ghJson = data.json()

    for x in tqdm(ghJson):
        if not x['path'].__contains__("."):
            data2 = requests.get(x['url'], headers=headers)
            ghJson2 = data2.json()
            for x2 in ghJson2:
                folders.append(x2["download_url"])

    file = open('folders.txt', 'x')
    pickle.dump(str(folders), file)
    file.close()

url = folders[random.randint(0, len(folders)-1)]

response = requests.get(url)
img = Image.open(BytesIO(response.content))

img.show()
