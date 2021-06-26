import requests
from bs4 import BeautifulSoup

file = open('box.csv', 'w', encoding='UTF-8_sig')
file.write('სათაური,ნახვები')


def bruh():
    sia = []
    i = 1
    for i in range(6):
        url = f'https://mangakakalot.com/manga_list?type=topview&category=all&state=all&page={i + 1}'
        r = requests.get(url)
        content = r.text
        soup = BeautifulSoup(content, 'html.parser')
        section = soup.find('div', {'class': 'truyen-list'})

        mangalist = section.find_all('div', {'list-truyen-item-wrap'})

        for each in mangalist:
            info = each.find('h3')
            title = info.a.text
            sia.append(title)
            print(sia)
        return sia


bruh()
