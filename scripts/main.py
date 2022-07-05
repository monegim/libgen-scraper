from urllib.request import urlopen
from helpers import parse_tables_from_html
from db import sql_close_connection, sql_connection, sql_insert
from bs4 import BeautifulSoup
import settings


def main():
    url = settings.url
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    conn = sql_connection(settings.database_path)
    parse_tables_from_html(conn, bs)
    sql_close_connection(conn)


if __name__ == '__main__':
    main()
