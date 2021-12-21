from json import encoder
import lxml
import requests
from bs4 import BeautifulSoup
import json


def main():
    url = 'https://freelance.ru/project/search/pro?c=&q=python&m=or&e=&f=&t=&o=0&o=1'
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    task_list = soup.find_all(class_='box-title')

    task_options_list = []
    for task in task_list:
        task_title = task.find_next('h2').text.rstrip().lstrip()
        task_link = 'https://freelance.ru' + task.find_next('a').get('href')
        task_finance = task.find_next(class_='cost').text.rstrip().lstrip()
        task_description = task.find_next(class_="description").text.rstrip().lstrip()

        task_options = {
            'title': task_title,
            'link': task_link,
            'finance': task_finance,
            'description': task_description
        }

        task_options_list.append(task_options)
        # print(task_options)
        with open('fl_tasks_list.json', 'w', encoding='utf-8') as file:
            json.dump(task_options_list, file, indent=4, ensure_ascii=False)
        # print(task_description)

if __name__ == '__main__':
    main()
