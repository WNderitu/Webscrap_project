import requests
from bs4 import BeautifulSoup

# error handling for HTTP requests in case the website is not accessible when using get. checks request errors. 
response = requests.get('https://www.bbc.com/')
if response.status_code == 200:
    src = response.content
    print(src)
else:
    print('Error accessing the website', response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

# news headlines in h2 tags class - sc-4fedabc7-3 zTZri
h2_tags = soup.find_all('h2',class_='sc-4fedabc7-3 zTZri')
for h2 in h2_tags:
    print(h2.text)

# summary of news headlines in p  class sc-e5949eb5-0 gpCoKv
p_tags= soup.find_all('p', class_= 'sc-e5949eb5-0 gpCoKv')
for p in p_tags:
    print(p.text)

# summary of news headlines in p - class sc-b8778340-4 kYtujW
p_tags= soup.find_all('p', class_= 'sc-b8778340-4 kYtujW')
for p in p_tags:
    print(p.text)
    





