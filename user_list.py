# 导入依赖库
import re

import requests
from bs4 import BeautifulSoup
import time
import random

import filter


# 定义类
def str2int(text):
    return int(text)


class GithubFollower:
    def __init__(self, target_username, headers):
        self.target_username = target_username
        self.headers = headers

    def analyse(self, follower_names):
        for idx, name in enumerate(follower_names):
            print('[INFO]: 正在爬取用户%s的详细信息...' % name)
            user_url = f'https://github.com/{name}'
            try:
                response = requests.get(user_url, headers=self.headers, timeout=15)
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                # --获取用户名
                username = soup.find_all('span', class_='p-nickname vcard-username d-block')
                if username:
                    username = [name, filter.rex(username[0].text)]
                    print(username)
                else:
                    username = [name, '']
                # --所在地
                position = soup.find_all('span', class_='p-label')
                if position:
                    # print(position)
                    position = position[0].text
                else:
                    position = ''
                # --仓库数, stars数, followers, following
                overview = soup.find_all('span', class_='Counter')
                num_repos = str2int(overview[0].text)
                num_stars = str2int(overview[3].text)
                # --贡献数(最近一年)
                num_contributions = soup.find_all('h2', class_='f4 text-normal mb-2')
                # print(num_contributions)
                num_contributions = str2int(num_contributions[0].text.replace('\n', '').replace(' ', ''). \
                    replace('contributioninthelastyear', '').replace(
                    'contributionsinthelastyear', ''))
                print(num_contributions)
                # --保存数据
                info = [username[0], position, num_repos, num_stars, num_contributions]
                print(info)
                # follower_infos[str(idx)] = info
            except:
                pass
            print("end")
            # time.sleep(random.random() + random.randrange(0, 2))

    # 定义实例方法
    def get_follower_names(self):
        print('[INFO]: 正在获取%s的所有followers用户名...' % self.target_username)
        page = 0
        follower_names = []
        headers = self.headers.copy()
        while True:
            print(page)
            page += 1
            followers_url = f'https://github.com/{self.target_username}?page={page}&tab=followers'
            try:
                response = requests.get(followers_url, headers=headers, timeout=15)
                html = response.text
                # print(html)
                if 've reached the end' in html:
                    break
                soup = BeautifulSoup(html, 'lxml')
                pattern = r'(?<=>)[a-zA-Z0-9]+(?=<)'
                for name in soup.find_all('span', class_='Link--secondary'):

                    # print(name)
                    match = re.search(pattern, str(name))
                    # print(match)
                    if match:
                        # print(match.group())
                        follower_names.append(match.group())

            except:
                pass
            # time.sleep(random.random() + random.randrange(0, 2))
            headers.update({'Referer': followers_url})
        # print('[INFO]: 成功获取%s的%s个followers用户名...' % (self.target_username, len(follower_names)))
        return follower_names


# 创建类的实例对象并调用 getfollowernames 方法获取目标用户的 followers 名称列表
# # github_follower = GithubFollower('YunaiV', {'Content-Type': 'application/json'})
# github_follower = GithubFollower('iwnfy', {'Content-Type': 'application/json'})
# followers = github_follower.getfollowernames()
# # print(followers)
# github_follower.analyse(followers)
