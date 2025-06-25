from bs4 import BeautifulSoup
import requests
import tabulate


url = 'https://www.kp.ru/'

def parser(url):

    novelty = []
    time = []

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    allNews = soup.find_all(class_ = "sc-jba0vw-0 kfDYSs")
    scr1 = soup.find_all(class_ = "sc-1tputnk-9 gpa-DyG")

    for new in allNews:
        novelty.append(new.text)

    for new in scr1:
        time.append(new.text)

    return novelty, time

novelty, time = parser(url)
vtulka =[]

for i in range(len(novelty)):
    vtulka.append([novelty[i], time[i]])

print(tabulate.tabulate(vtulka, tablefmt="fancy_grid"))