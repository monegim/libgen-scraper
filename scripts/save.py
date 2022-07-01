import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from helpers import save_to_var

sys.setrecursionlimit(50000)
keyword = "manning"
page_n = 25
page = 1

url = f"https://libgen.is/search.php?&req={keyword}&phrase=1&view=detailed&res={page_n}&column=def&sort=year&sortmode=DESC&page={page}"

# html_file = "files/test.html"
vars_file = "files/objs.pkl"
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
save_to_var(vars_file, bs)