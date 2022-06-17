from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

# print(soup.title)

articles = soup.find_all(name='a', class_= "titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

print(article_texts)
print(article_links)
print(article_upvotes)

max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)

print(f"Article Title: {article_texts[max_index]}\nArticle Link: {article_links[max_index]}\nArticle Upvotes: {article_upvotes[max_index]}")

