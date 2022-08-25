# https://gist.github.com/slavakurilyak/d3418446179f98cde5b7d6b53eefa09d

# https://github.com/cat-milk/Anime-Girls-Holding-Programming-Books

# https://stackoverflow.com/questions/63252337/how-to-open-and-display-images-from-a-github-repository#

from PIL import Image
import requests
from io import BytesIO
import json

data = requests.request('GET', ' https://api.github.com/repos/cat-milk/Anime-Girls-Holding-Programming-Books/contents/')
ghJson = data.json()
ghPlain = json.load(ghJson)

url = \
    'https://raw.githubusercontent.com/cat-milk/Anime-Girls-Holding-Programming-Books/master/C/Shalltear_Overlord_Holding_C_Programming_Language.png'

response = requests.get(url)
img = Image.open(BytesIO(response.content))

img.show()
