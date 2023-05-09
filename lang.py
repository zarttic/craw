# 导入依赖库
import re

import requests
from bs4 import BeautifulSoup
import time
import random

from wordcloud import WordCloud

import filter
from user_list import GithubFollower
filename = "words.txt"
file = open(filename, "a+")
# 定义类
def str2int(text):
    return int(text)


def rex_lang(text):
    pattern = r'(?<=itemprop="programmingLanguage">)[\w\s]+(?=<)'
    match = re.findall(pattern, text)
    if match:
        return match
    else:
        return []


class GithubLang:
    def __init__(self, target_username, headers):
        self.target_username = target_username
        self.headers = headers

    # 定义实例方法
    def get_repo_lang(self, username):
        langs = []
        # print('[INFO]: 正在获取%s的仓库信息...' % username)
        page = 0
        headers = self.headers.copy()

        while True:
            print(page)
            page += 1
            followers_url = f'https://github.com/{username}?page={page}&tab=repositories'
            try:
                response = requests.get(followers_url, headers=headers, timeout=15)
                print(response)
                html = response.text
                return rex_lang(html)
                # langs.append(self.rex1(html))
                # print(self.rex1(html))
            except:
                pass
            # time.sleep(random.random() + random.randrange(0, 2))


github_follower = GithubFollower('gaoyf', {'Content-Type': 'application/json'})
followers = github_follower.get_follower_names()
r = GithubLang('zarttic', {'Content-Type': 'application/json'})
# new_text = ""
word_frequencies = {}
for x in followers:
    cur = r.get_repo_lang(x)
    file.write(','.join(cur))
    for word in cur:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

wordcloud = WordCloud(width=1000, height=700, background_color='white', font_path="lang.ttf").generate_from_frequencies(word_frequencies)

wordcloud.to_file('static.jpg')
