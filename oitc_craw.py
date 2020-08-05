from selenium import webdriver
from time import sleep
import requests
import datetime
from bs4 import BeautifulSoup as b4

get = datetime.datetime.now()

mon_dic={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
         7:"July",8:"August",9:"September",10:"October",11:"November",
         12:"December"}

month = mon_dic.get(get.month,"")
month_int = get.month
day = get.day

print(f"2020-{month_int}-{day} 大塚資訊最新活動 ")


get_data = requests.get("https://www.oitc.com.tw/",headers = {})
get_data = b4(get_data.text,"lxml")

#class用class_表示的原因是因為class是Python保留字
result = get_data.find_all('div', class_="item swiper-slide")


a_01 = get_data.find('div', class_="item swiper-slide")

#注意不可寫成.find_all().find(),只能先以find找到單一元素，再用find_all()往下找更細的內容
#以下三行可以爬到官網中最新活動
for i in result:
    result2 = i.find_all("a", class_="figure")
    for j in result2:
        print(j.get("title"))
        print(j.get("href"))



