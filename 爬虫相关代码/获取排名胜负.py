# -*- codeing = utf-8 -*-
# @Time: 2020-09-26 13:58
# @Author: 戴铭阳
# @File: 5.xpath解析基础.py
# @Software : PyCharm

import requests
import csv
from lxml import etree
import os

from selenium import webdriver
if not os.path.exists('./pics'):
    os.mkdir('./pics')

bro = webdriver.Edge(executable_path='./实训/msedgedriver')
bro.get('https://nba.stats.qq.com/standings/')
page_text = bro.page_source

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}




tree = etree.HTML(page_text)

trList1 = tree.xpath('//div[@class="area area-tables"]/div/div[1]/div[2]/table/tbody/tr')
trList2 = tree.xpath('//div[@class="area area-tables"]/div/div[1]/div[2]/div/div/table[1]/tbody/tr')


newFile = open('rank.csv', 'w')
newWriter = csv.writer(newFile, lineterminator='\n')
newWriter.writerow(['东部'])
newWriter.writerow(['排名','球队','胜','负','胜场差','胜率','主场','客场','东部',	'得分',	'失分',	'净胜',	'连胜/负'])

for tr1,tr2 in zip(trList1,trList2):
    
    rank = tr1.xpath('./td[1]//text()')[0]
    name = tr1.xpath('./td[2]/a/span/text()')[0]
    win = tr1.xpath('./td[3]/text()')[0]
    lose = tr1.xpath('./td[4]/text()')[0]
    url = tr1.xpath('./td[2]/a/img/@src')[0]

    wl = tr2.xpath('./td[1]/text()')[0]
    percent = tr2.xpath('./td[2]/text()')[0]
    zhu = tr2.xpath('./td[3]/text()')[0]
    ke = tr2.xpath('./td[4]/text()')[0]
    east = tr2.xpath('./td[5]/text()')[0]
    scorce = tr2.xpath('./td[6]/text()')[0]
    shi = tr2.xpath('./td[7]/text()')[0]
    jingsheng = tr2.xpath('./td[8]/text()')[0]
    lian = tr2.xpath('./td[9]/text()')[0]
    lian = lian + tr2.xpath('./td[9]/span/text()')[0]

    img_data = requests.get(url=url).content
    path = './pics/' + name + '.png'

    fp = open(path, 'wb')
    fp.write(img_data)
    row = [rank,name,win,lose,wl,percent,zhu,ke,east,scorce,shi,jingsheng,lian]
    newWriter.writerow(row)
newWriter.writerow(['西部'])
newWriter.writerow(['排名','球队','胜','负','胜场差','胜率','主场','客场','西部',	'得分',	'失分',	'净胜',	'连胜/负'])
trList1 = tree.xpath('//div[@class="area area-tables"]/div/div[2]/div[2]/table/tbody/tr')
trList2 = tree.xpath('//div[@class="area area-tables"]/div/div[2]/div[2]/div/div/table[1]/tbody/tr')
for tr1,tr2 in zip(trList1,trList2):
    rank = tr1.xpath('./td[1]//text()')[0]
    name = tr1.xpath('./td[2]/a/span/text()')[0]
    win = tr1.xpath('./td[3]/text()')[0]
    lose = tr1.xpath('./td[4]/text()')[0]
    url = tr1.xpath('./td[2]/a/img/@src')[0]

    wl = tr2.xpath('./td[1]/text()')[0]
    percent = tr2.xpath('./td[2]/text()')[0]
    zhu = tr2.xpath('./td[3]/text()')[0]
    ke = tr2.xpath('./td[4]/text()')[0]
    east = tr2.xpath('./td[5]/text()')[0]
    scorce = tr2.xpath('./td[6]/text()')[0]
    shi = tr2.xpath('./td[7]/text()')[0]
    jingsheng = tr2.xpath('./td[8]/text()')[0]
    lian = tr2.xpath('./td[9]/text()')[0]
    lian = lian + tr2.xpath('./td[9]/span/text()')[0]

    img_data = requests.get(url=url).content
    path = './pics/' + name + '.png'

    fp = open(path, 'wb')
    fp.write(img_data)
    row = [rank,name,win,lose,wl,percent,zhu,ke,east,scorce,shi,jingsheng,lian]
    newWriter.writerow(row)

newFile.close()  







