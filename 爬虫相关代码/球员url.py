import requests
import csv
from lxml import etree
import os
from selenium import webdriver
from time import sleep

if not os.path.exists('./team'):
    os.mkdir('./team')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
bro = webdriver.Edge(executable_path='./msedgedriver')
for i in range(1,31):
    url = 'https://nba.stats.qq.com/player/list.htm#teamId='+str(i)
    bro.get(url)
    page_text = bro.page_source
    tree = etree.HTML(page_text)
    name=tree.xpath('//a[@class="current"]/span/text()')[0]
    path='./team/'+name+'.txt'
    newFile = open(path, 'w')
    trList = tree.xpath('/html/body/div[2]/div[2]/table/tbody/tr')
    for tr in trList:
        playerUrl=tr.xpath('./td[1]/a/@href')[0]
        newFile.write('https:'+playerUrl+'\n')






