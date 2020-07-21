from bs4 import BeautifulSoup as bs
import requests


def get_info(url):
    data = requests.get(url)
    soup = bs(data.text, 'html.parser')
    total = soup.find('div', class_="maincounter-number").text
    total = total[1:len(total) - 2]
    other = soup.find_all('span', class_="number-table")
    recoverd = other[2].text
    deaths = other[3].text
    deaths = deaths[1:]
    ans = {'total': total, 'revoced cases': recoverd, 'total death': deaths}
    return ans


url = "https://www.worldometers.info/coronavirus/"
ans = get_info(url)
for i, j in ans.items():
    print(i + " : " + j)
