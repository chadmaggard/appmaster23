import requests
from bs4 import BeautifulSoup

#url = 'http://download2.inin.com/Service%20Updates/Interaction_Center/2019r2/P06/CIC_release_readme.html?token=exp=1564165138~acl=/*~hmac=e5732ec55d65bfe8705b0fd61aa3b97b8fafbbd524a37760e05a187a4ac7136b'
#url = 'http://download2.inin.com/Service%20Updates/Interaction_Center/2019r2/P06/CIC_release_summary.html?token=exp=1564170984~acl=/*~hmac=a1e08161032b3f839495669daf6fb9f237e901b07786f3d5b87d1e22140966f3'
url = 'http://download2.inin.com/Service%20Updates/Interaction_Center/2019r2/P06/CIC_release_readme.html?token=exp=1564258020~acl=/*~hmac=cc818eadfa1e0b4e130c11eaf8f5aabfc1c5b232ef491d5457e6a4167c355ed1'
r = requests.get(url)

html_box = r.text

soup = BeautifulSoup(html_box)

pretty_soup = soup.prettify()

#print(pretty_soup)

#a_tags = soup.find_all('div class="handlers')

mydivs = soup.find_all(class_=["serviceupdateheader", "componentheader", "scrnumber", "scrdesc" ])
#mydivs2 = soup.find_all(class_="scrdesc")
#mydivs = soup.find_all(id="scrnumber")

#print(mydivs2)

print(type(mydivs))


#for class_ in mydivs:
 #   print(class_)

#for class_ in mydivs2:
 #   print(class_)
