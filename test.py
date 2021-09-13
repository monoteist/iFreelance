from random import choice

import requests
from bs4 import BeautifulSoup as BS

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]

jobs = []


def habr_parsing(word):
    url = f'https://freelance.habr.com/tasks?page=1&q={word}'
    res = requests.get(url, headers=choice(headers))
    pagination = len(BS(res.content, 'html.parser').find(
        'div', id='pagination').find_all('a'))

    for u in range(pagination):
        url = f'https://freelance.habr.com/tasks?page={u}&q={word}'
        if res.status_code == 200:
            soup = BS(res.content, 'html.parser')
            ul = soup.find('ul', id='tasks_list')
            li = ul.find_all('li', class_='content-list__item')
            for i in li:
                url = 'https://freelance.habr.com/' + i.a['href']
                title = i.a.text
                price = 'Договорная'
                if i.find('span', class_='count'):
                    price = i.find('span', class_='count').text
                views = i.find('span', class_='icon_task_views').text.strip()
                responses = ''
                if i.find('span', class_='icon_task_responses'):
                    responses = i.find(
                        'span', class_='icon_task_responses').text.strip()
                time = i.find(
                    'span', class_='icon_task_publish_at').text.strip()
                jobs.append({'url': url, 'title': title, 'price': price,
                            'views': views, 'responses': responses, 'time': time})
    return jobs
