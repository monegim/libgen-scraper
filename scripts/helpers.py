import pickle
from typing import Dict, List

import requests


def save_to_var(vars_file: str, obj: List) -> None:
    with open(vars_file, "wb") as f:
        pickle.dump(obj, f)


def wirte_to_file(path: str, content) -> None:
    with open(path, "w") as f:
        f.write(str(content))


def load_from_file(vars_file):
    with open(vars_file, 'rb') as f:
        return pickle.load(f)


def process_tables(table) -> Dict:
    # wirte_to_file("files/table.html", table)
    tbody = table.tbody
    trs = tbody.find_all('tr')
    image_url = trs[1].find_all('td')[0].img.attrs['src']
    download_url = trs[1].find_all('td')[0].a.attrs['href']
    # Name
    name = trs[1].select_one('td[colspan]').find('a').text
    # Author
    # name = trs[2].select_one('td[colspan]').find('a').text
    # Series, Periodical\

    # Publisher, City

    # Year, Edition
    year_edition = trs[5].find_all('td')
    year = year_edition[1].text
    edition = year_edition[3].text

    # Language, Pages
    # name = trs[6].select_one('td[colspan]').find('a').text
    lang_pages = trs[6].find_all('td')
    lang = lang_pages[1].text
    pages = lang_pages[3].text

    # ISBN, ID
    # name = trs[7].select_one('td[colspan]').find('a').text
    isbn_id = trs[7].find_all('td')
    isbn = isbn_id[1].text
    id = isbn_id[3].text

    # Time added, Time modified
    # name = trs[7].select_one('td[colspan]').find('a').text

    # Size, Extension
    # name = trs[9].select_one('td[colspan]').find('a').text
    size_extenstion = trs[9].find_all('td')
    size = size_extenstion[1].text.split()
    size_in_m = size[0]
    size_in_b = size[2][1:-1]
    extention = size_extenstion[3].text
    return {
        'name': name,
        'year': year,
        'edition': edition,
        'lang': lang,
        'pages': pages,
        'image_url': image_url,
        'download_url': download_url,
        'book_id': int(id),
        'extention': extention,
        'size_in_b': int(size_in_b),
    }


def save_thumbnail(image_url: str, id: str, location: str = "files/thumbnails/"):
    img_data = requests.get(image_url).content
    image_location = location + id + '.' + get_image_extension(image_url)
    with open(image_location, 'wb') as handler:
        handler.write(img_data)


def get_image_extension(image_url: str):
    return image_url.split('.')[-1]
