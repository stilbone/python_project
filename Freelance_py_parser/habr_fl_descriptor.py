from os import error
import requests
import json
from json import encoder
from bs4 import BeautifulSoup
import lxml


def main():
    url = 'https://freelance.habr.com/tasks?q=python'
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    all_tasks_dict = {}
    count = 0

    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    tasks_list = soup.find_all(class_='task__title')

    for task in tasks_list:
        tasks = task.find_next('a')
        task_name = tasks.text
        task_href = 'https://freelance.habr.com/' + tasks.get('href')

        all_tasks_dict[task_name] = task_href
        # print(f'{task_name} : {task_href}')

        # print(all_tasks_dict)

        # limit = 1
        # index = 0

    task_list = []
    for task in all_tasks_dict.items():
        task_title = task[0]
        task_link = task[1]
        task_id = task_link.split('/')[-1]

        req = requests.get(task_link, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, 'lxml')
        task_finance = soup.find(class_='task__finance').text
        task_description = soup.find(class_='task__description').text

        task_options = {
            'id': count,
            'title': task_title,
            'link': task_link,
            'finance': task_finance,
            'description': task_description
        }
        task_list.append(task_options)
        with open('hubr_tasks_list.json', 'w', encoding='utf-8') as file:
            json.dump(task_list, file, indent=4, ensure_ascii=False)

        count += 1
        print(f'task loaded... {count}')

        # index += 1
        # if index == limit:
        #     break


if __name__ == '__main__':
    main()
