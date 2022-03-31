import requests
from bs4 import BeautifulSoup

link = 'https://znanija.com/app/ask?entry=hero&q=' #начальная ссылка
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
question = input(" какой вопрос: ").split()
for el in question:
	link += f'{el}+'
r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)