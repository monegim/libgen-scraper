from helpers import load_from_file, process_tables, wirte_to_file

vars_file = "files/objs.pkl"
bs = load_from_file(vars_file)

tables = bs.find('table', {'class': 'c'})
# wirte_to_file("files/tables.html", tables)
tables_all = tables.find_all('table',recursive=False)
# table = tables_all[2]
for child in tables_all:
    res = process_tables(child)
    # print(res)
    print(res)
