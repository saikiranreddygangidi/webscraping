import requests
from bs4 import BeautifulSoup
data=[]
import pandas as pd
import re
for i in range(1,10):
    da=[]
    k="https://www.filmibeat.com/scripts/popcorn/controllers/celeb-search.php?lang=all&limit={}&start_with=all".format(i)
    da.append(i)
    da.append(1)
    page=requests.get(k)
    soup =BeautifulSoup(page.content,'html.parser')
    title=soup.find('ul',{'class':'event-block'})
    link=title.find('a').get('href')
    s=requests.get(link)
    soup1 =BeautifulSoup(s.content,'html.parser')
    title=soup1.find('div',{'class':'celeb-profile-name'})
    if title!=None:
     title=title.find('h1')
    title1=soup1.find('div',{'class':'celeb-profile-from'})
    title2=soup1.find('div',{'class':'celeb-profile-DOB'})
    title3=soup1.find('div',{'class':'celeb-profile-bio'})
    title4=soup1.find('div',{'class':'celeb-profile-img'})
    da.append(title.get_text())
    da.append('M/F')
    if title2!=None:
     if title2.get_text()!='\n':
      text=title2.get_text().split(':')[1]
      da.append(re.findall('(.*)\n',text)[0])
     else:
      da.append('no-data-dob')
    if title1!=None:
     if title1.get_text()!='\n':
      text=title1.get_text().split(':')[1]
      da.append(re.findall('(.*)\n',text)[0])
    else:
     da.append('no-data-from')
    
    if title4!=None:
     text=title4.find('img')
     if text!='\n':
      da.append(text.get('src'))
    else:
     da.append('no-photo')
    if title3!=None:
     s1=requests.get(title3.find('a').get('href'))
     soup2 =BeautifulSoup(s1.content,'html.parser')
     title5=soup2.find('div',{'class':'bharat-story'})
     if title5!=None:
      text=title5.get_text()
      da.append(re.findall('(.*)\n',text)[1])
    da.append(title.get_text())
    data.append(da)
    print(da)
   
df=pd.DataFrame(data,columns=['id','is_disable','name','gender','Dateofbirth','Birth place','image','bio','orginal_name'])   
import os
#os.remove("data1.csv")
#with open('data1.csv', 'a') as f:
 #   df.to_csv(f)
df.to_csv(r'data1.csv', index = False)
