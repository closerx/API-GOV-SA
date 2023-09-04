
import requests,re
from bs4 import BeautifulSoup

url="https://www.my.gov.sa/wps/portal/snp/content/appslist/"

res=requests.get(url)

soop=BeautifulSoup(res.content,"lxml")
imgapp=[]
for i in soop.findAll("img"):
	if (i["src"].startswith("/wps")):
		imgapp.append("https://www.my.gov.sa"+i["src"])
		


all=[]
for  i in soop.findAll("td"):
	txt1=i.text.strip()
	txt2=re.sub(r"\s"," ",txt1)
	all.append(txt2.splitlines())
	
apps=[]
info=[]
myall = [ele for ele in all if ele != []]
for i in range(len(myall)):
	if (i % 2) ==0:
		apps.append(myall[i][0])
	else:
		info.append(myall[i][0])

print(apps)
