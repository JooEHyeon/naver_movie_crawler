import requests
from bs4 import BeautifulSoup
import csv

# soup_objects = []

# search_input = input()

URL = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(URL)

soup = BeautifulSoup(response.text,'html.parser')

movie_section = soup.select('div[id = container] > div[id = content] > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 >li')

for movie in movie_section:
    a_tag = movie.select_one('dl.lst_dsc > dt > a')
    movie_name = a_tag.text
    movie_code = a_tag['href'].split('=')[-1]
    # print(movie_name, movie_code)

    movie_data = {'name' : movie_name, 'code' : movie_code}

    with open('movie_rank.csv','a',newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ['name', 'code'])
        writer.writerow(movie_data)

             # print(news_link)
             # print(news_title,'\n')