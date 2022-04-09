import requests
import os
from bs4 import BeautifulSoup


soup = BeautifulSoup(requests.get("https://bindingofisaacrebirth.fandom.com/wiki/Items").content, "html.parser")

for item in soup.find_all("table")[1].find_all("tr"):
    item_att = item.find_all("td")
    if item_att:
        id=item_att[1]['data-sort-value']
        name=item_att[0]['data-sort-value'].lower().replace("/", "-").replace("'", "").replace("?", "")
        pic_url=item_att[2].find("img")['data-src']
        print(name)
        os.mkdir(id)
        img_data = requests.get(pic_url).content
        with open(f'{id}/sprite.webp', 'wb') as pic:
            pic.write(img_data)
        
