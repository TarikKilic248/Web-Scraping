# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.co.uk/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA%2C+United+States"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("h", {"class":"css-1m051bw"})

print(len(myLinks))

counter = 0
for link in myLinks:
  if counter > 1:
    print(link.text)
    print(f"""https://www.yelp.com{link["href"]}""")
  counter +=1
```
<details> <summary> 👀 Answer </summary>

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.co.uk/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA%2C+United+States"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("a", {"class":"css-1m051bw"}) # Wrong tag

print(len(myLinks))

counter = 0
for link in myLinks:
  if counter > 1:
    print(link.text)
    print(f"""https://www.yelp.com{link["href"]}""")
  counter +=1
```
</details>