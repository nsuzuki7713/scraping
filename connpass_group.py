# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv
from time import sleep

f = open('group-list-20180206.csv', 'a')
writer = csv.writer(f, lineterminator='\n')
writer.writerow(["公開日","グループ名","URL","人数"])

count = 0
for i in range(201):
    url = "https://connpass.com/recent_group/?page=" + str(i+1)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    list = soup.find_all("div", class_="series_list")

    for val in list:
        csv_list = []
        csv_list.append(val.select(".date")[0].string.replace('公開日: ', ''))
        csv_list.append(val.select(".title")[0].string)
        csv_list.append(val.select(".title > a")[0].get('href'))
        csv_list.append(val.select(".amount")[0].string)
        writer.writerow(csv_list)
        count = count + 1

    sleep(1)
print("グループ数:" + str(count))
f.close()
