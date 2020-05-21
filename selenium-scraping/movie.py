import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import csv
import os
driver = webdriver.Chrome('chromedriver')
names=[]
link_b=[]
link_img=[]

driver.maximize_window()
driver.get('https://www.filmibeat.com/celebs')
time.sleep(2)
while True:
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    #sliders = soup.find_all("div", {"class": "slider-item"})

    height=0
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    if height == driver.execute_script("return document.body.scrollHeight;"):
        break
    else:
        curheight = driver.execute_script("return document.body.scrollHeight;")
        height = curheight

title=soup.find('div',{'class':'event-cont'})
t=title.find_all('a')
print('end loop')
k=0

for i in t:
    
    if k%2!=0:
        print('done')
        names.append(i.get_text())
        
        link_b.append(i.get('href'))
        
    else:
        k1=i.find('img')
        if k1!= None:
         link_img.append(k1.get('src'))
     
    k+=1
data=[]
import pandas as pd
for i in zip(names,link_b,link_img):
 data.append(list(i))
df=pd.DataFrame(data,columns=['names','link_data','link_img'],index=False)   
import os
os.remove("data1.csv")
with open('data1.csv', 'a') as f:
    df.to_csv(f)
#df.to_csv(r'data.csv', index = False)
print(df.head(1))
