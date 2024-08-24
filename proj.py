import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.bbc.com/')
print(result.status_code)

src = result.content
print(src)

soup = BeautifulSoup(result.content, 'html.parser')
# new headlines in h2 tags.
h2_tags = soup.find_all('h2')
for h2 in h2_tags:

    print(h2.text)

# summary of headlines in p
p_tags= soup.find_all('p')
for p in p_tags:

    print(p.text)

    





