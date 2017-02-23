from bs4 import BeautifulSoup
import urllib
import requests
import sys
import time
import urllib
from tqdm import tqdm
import re

def my_hook(t):

  last_b = [0]

  def inner(b=1, bsize=1, tsize=None):
 
    if tsize is not None:
        t.total = tsize
    t.update((b - last_b[0]) * bsize)
    last_b[0] = b
  return inner
loading=0
webpage="http://164.100.47.194/Loksabha/Members/AlphabeticalList.aspx"
page=requests.get(webpage)




soup=BeautifulSoup(page.content,"html.parser")
Mplist=[]
Mplist2=[]
Mplist=soup.findAll("a")
for i in Mplist:
	l=i.find("img")
	if l and i.has_attr("title"):
		Mplist2.append(l["src"]+"=>"+i["title"].encode("UTF-8"))

Mplist=[]	
for i in Mplist2:
  	if re.match(re.compile("^http"),i):
    		Mplist.append(i)
print("The total number records found is "+str(len(Mplist)))

for i in Mplist:
	comp=i.split("=>")
	names=comp[1].split(",")
        print("photo of Loksabha MP "+names[1]+" "+names[0]+" is downloading")
    	with tqdm(unit='B', unit_scale=True, miniters=2,
          desc="[download]") as t:  # all optional kwargs
    		urllib.urlretrieve(comp[0], filename="MpImages/"+names[1]+" "+names[0]+".jpg",
                       reporthook=my_hook(t), data=None)
     





