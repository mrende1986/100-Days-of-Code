from bs4 import BeautifulSoup

with open("Day 45/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find_all(name='h1')
print(heading)

specific_heading = soup.find_all(name='h1', id='name')
print(specific_heading)

company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name)

headings = soup.select(".heading")
print(headings)