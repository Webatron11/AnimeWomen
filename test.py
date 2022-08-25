import requests
import json

data = requests.request('GET', ' https://api.github.com/repos/cat-milk/Anime-Girls-Holding-Programming-Books/contents/')
ghJson = data.json()
folders = []

for x in ghJson:
    if not ghJson[x]['path'].contains("."):
        data2 = requests.request('GET', ghJson[x]['url'])
        ghJson2 = data.json()
        for x2 in ghJson2:
            folders.append(ghJson2[x2]["download_url"])

print(folders)
