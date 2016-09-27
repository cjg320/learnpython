import requests
from bs4 import BeautifulSoup

s = requests.session()
login_url = "http://socialclub.rockstargames.com/profile/signin"

#get the token needed to log in
tmp=s.get("http://socialclub.rockstargames.com")

findtoken = BeautifulSoup(tmp.content, "lxml")
token=findtoken.find("__RequestVerificationToken")
#__________________________________

username = 'smittyofwar@mail.com'
passwrd='Harambe1'

data = dict(login=username, password=passwrd,__RequestVerificationToken=token, next='/')

s.post(login_url, data=data,headers=dict(Referer="http://socialclub.rockstargames.com"))



r = s.get("http://socialclub.rockstargames.com")
#r = s.get("https://socialclub.rockstargames.com/member/cjg320/games/gtav/career/overview/gtaonline")

soup = BeautifulSoup(r.content, "lxml")
soup = soup.prettify()


with open('thesauce.txt', 'w', encoding='utf-8') as f:
    for line in soup:
        f.write(str(line))


