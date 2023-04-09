import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=%C4%B0znik+Cd.+No%3A36B%2C+16900+Bursa%2C+Turkey"

response = requests.get(url)
html = response.text
#print(html)
soup = BeautifulSoup(html, 'html.parser')
myLinks = soup.find_all("a", {"class":"css-1m051bw"})

counter = 0
for link in myLinks:
  if counter > 1:
    print(link.text)
    print(f"""https://www.yelp.com{link["href"]}""")
  counter +=1