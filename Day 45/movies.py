from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
movies = response.text
soup = BeautifulSoup(movies, 'html.parser')

print(soup.title)

top_movies = soup.find_all(name='h3')
top_list = []

for m in top_movies:
    top_list.append(m.getText())

top_list[88] = '12) The Godfather Part II'

top_list = top_list[::-1]

with open('movies.txt', mode='w') as file:
    for movie in top_list:
        file.write(f"{movie}\n")
