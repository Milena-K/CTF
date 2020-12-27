import requests
from bs4 import BeautifulSoup

url = "http://timesink.be/speedy/index.php"
s = requests.Session()
r = s.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
rndString = soup.find_all(id="rndstring")[0].get_text()
post = s.post(url, data={'inputfield': rndString})
print(post.text)
