import json
from random import choice

import requests
from bs4 import BeautifulSoup as BS

url = 'https://freelance.habr.com/tasks?q=python&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]


def habr_parsing(url):
    jobs = []
    res = requests.get(url, headers=choice(headers))
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
                responses = i.find('span', class_='icon_task_responses').text.strip()
            time = i.find('span', class_='icon_task_publish_at').text.strip()
            jobs.append({'url': url, 'title': title, 'price': price,
                        'views': views, 'responses': responses, 'time': time})
    return jobs

# with open('jobs.json', 'w', encoding='utf-8') as f:
#     json.dump(jobs, f, indent=4, ensure_ascii=False)

