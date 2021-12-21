from json import encoder
import lxml
import requests
from bs4 import BeautifulSoup
import json

url = 'https://freelance.habr.com/tasks?q=python'
headers = {
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, 'lxml')
task_list = soup.find_all(class_='task__title')

all_tasks_dict = {}

for task in task_list:
    tasks = task.find_next('a')
    task_name = tasks.text
    task_href = 'https://freelance.habr.com/' + tasks.get('href')

    all_tasks_dict[task_name] = task_href
    # print(f'{task_name} : {task_href}')

with open('all_tasks_dict.json', 'w', encoding='utf-8') as file:
    json.dump(all_tasks_dict, file, indent=4, ensure_ascii=False)

with open('all_tasks_dict.json', encoding='utf-8') as file:
    all_tasks = json.load(file)

print(all_tasks)
