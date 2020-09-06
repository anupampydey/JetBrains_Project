import os
import argparse
from collections import deque
import requests
from bs4 import BeautifulSoup, SoupStrainer
from colorama import Fore, init

init(autoreset=True)  # auto reset turned on for colorama foreground
parser = argparse.ArgumentParser(description="Text Parsing of Browser Webpage",
                                 epilog="post your feedbacks to Anupam Dey!")
parser.add_argument("dir_name", type=str, help='Name of the directory to be created')
args = parser.parse_args()

dirName = args.dir_name
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory", dirName, "Created")
else:
    print("Directory", dirName, "already exists")

filename = ''
saved_pages = deque()
while True:
    user_url = input("Enter URL > ").strip()
    if '.' in user_url:
        if 'http' not in user_url:
            user_url = "https://" + user_url
        req = requests.get(user_url)
        if req:
            # Success
            tags_list = SoupStrainer(['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
            soup = BeautifulSoup(req.content, 'html.parser', parse_only=tags_list)
            for tag in soup:
                if tag.name == 'a':
                    print(Fore.BLUE + tag.get_text())  # change forecolor of linked text to blue
                else:
                    print(tag.get_text())

            user_url = user_url.lstrip("https://")
            if user_url.count('.') == 2:
                idx1 = user_url.find('.')
                idx2 = user_url.find('.', idx1 + 1)
                filename = user_url[idx1 + 1:idx2]
            else:
                idx1 = user_url.find('.')
                filename = user_url[:idx1]
            filepath = dirName + '/' + filename + '.txt'
            saved_pages.append(filename)
            with open(filepath, 'w', encoding='utf-8') as my_file:
                my_file.write(soup.get_text())
        else:
            # Failure
            print('Error: Incorrect URL')
    elif user_url in saved_pages:
        filepath = dirName + '/' + user_url
        with open(filepath, 'r', encoding='utf-8') as my_file:
            print(my_file.read())
    elif user_url == 'back':
        if len(saved_pages) != 0:
            saved_pages.pop()
        if len(saved_pages) != 0:
            filename = saved_pages.pop()
            filepath = dirName + '/' + filename + '.txt'
            with open(filepath, 'r') as my_file:
                print(my_file.read())
    elif user_url == 'exit':
        break
    else:
        print('Error: Incorrect URL')
