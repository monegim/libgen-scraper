from urllib.request import urlopen
from helpers import parse_tables_from_html, url_builder
from db import sql_close_connection, sql_connection, sql_create_table
from bs4 import BeautifulSoup
import settings


def main():
    # url = settings.url

    conn = sql_connection(settings.database_path)
    sql_create_table(conn)
    for page in range(1,2):
        url = url_builder(settings.keyword, settings.number_per_page, page)
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')
        parse_tables_from_html(conn, bs)
    sql_close_connection(conn)



if __name__ == '__main__':
    main()
