import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://olympteka.ru/olymp/game/profile/50.html'

def parser(url):
    rowdata = []; fp = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all(class_ = "main-tb tb-medals")
    for quote in quotes:
        rowdata.append(quote.text)
    for i in rowdata:
        fp.append(i.split())
    fp = fp[0]
    fp[0] = 'Место'
    change = fp.index('Корея')
    fp[change] = str(fp[change] + ' ' + fp[change + 1])
    fp. pop(change + 1)

    change = fp.index('Всего', 8)
    fp[change] = str(fp[change] + ' ' + fp[change + 1])
    fp[change + 1] = ' '
    return fp

def create():
    con = sqlite3.connect("olymp.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS olymp (
                   country TEXT NOT NULL,
                   gold FLOAT NOT NULL,
                   silver FLOAT NOT NULL,
                   bronze FLOAT NOT NULL,
                   total FLOAT NOT NULL
                );""")
    con.commit()
    con.close()

def insert(fp):
    for i in range(0, len(fp), 6):
        con = sqlite3.connect("olymp.db")
        cur = con.cursor()
        cur.execute(f"INSERT INTO olymp ("
                    f"country, gold, silver, bronze, total) VALUES (?, ?, ?, ?, ?);", [fp[i], fp[i+1], fp[i+2], fp[i+3], fp[i+4]])
        con.commit()
        con.close()

create()
insert(parser(url))