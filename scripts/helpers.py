# from datetime import datetime
import os
import pickle
from typing import Dict, List
import requests
import db


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


def save_thumbnail(image_url: str, book_id: str, location: str = "files/thumbnails/"):
    if not os.path.exists(location):
        os.makedirs(location)
    img_data = requests.get(image_url).content
    image_location = os.path.join(
        location, str(book_id) + '.' + get_image_extension(image_url))
    with open(image_location, 'wb') as handler:
        handler.write(img_data)


def get_image_extension(image_url: str):
    return image_url.split('.')[-1]


def check_if_image_exists(conn, base_location: str, book_id: int, extension: str) -> bool:
    image_location = get_image_location(conn, book_id)
    return os.path.isfile(os.path.join(base_location, image_location, book_id + '.' + extension))


# def get_image_location(conn, book_id: int) -> str:
#     cursorObj = conn.cursor()
#     rows = cursorObj.execute("""SELECT CREATED_AT
#                         FROM BOOKS
#                         WHERE BOOK_ID = ?;""", (book_id,))
#     created_at = rows.fetchone()
#     if not created_at:
#         raise Exception("Could not find")
#     created_at_iso = datetime.fromisoformat(created_at[0])
#     year = created_at_iso.year
#     month = created_at_iso.month
#     return os.path.join(str(year), str(month))

def parse_tables_from_html(conn, bs):
    tables = bs.find('table', {'class': 'c'})
    tables_all = tables.find_all('table')
    for child in tables_all[::2]:
        res = process_tables(child)
        db.sql_insert(conn, res)


def url_builder(keyword, number_per_page, page):
    return f"https://libgen.is/search.php?&req={keyword}&phrase=1&view=detailed&res={number_per_page}&column=def&sort=year&sortmode=DESC&page={page}"