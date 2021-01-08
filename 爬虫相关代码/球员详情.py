import requests
import csv
from lxml import etree
import os
from selenium import webdriver
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
bro = webdriver.Edge(executable_path='./msedgedriver')

# -*- codeing = utf-8 -*-
# @Time: 2020-10-11 15:38
# @Author: 戴铭阳
# @File: getRequests.py
# @Software : PyCharm
import requests
from lxml import etree
import os
import time

headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / '
                        '87.0.4270.0Safari / 537.36 '
    }
bro = webdriver.Edge(executable_path='./msedgedriver')

#allteam=['湖人','76人','步行者','独行侠','公牛','国王','黄蜂','灰熊','活塞','火箭','掘金','爵士','开拓者','凯尔特人','快船','篮网','老鹰','雷霆','马刺','猛龙','魔术','尼克斯','奇才','骑士','热火','森林狼','太阳','鹈鹕','雄鹿','勇士']
allteam=['魔术','勇士','森林狼']
for teamname in allteam:
    filename1 = './team/'+teamname+'.txt'
    fp1 = open(filename1, 'r')
    if not os.path.exists('./team/'+teamname):
        os.mkdir('./team/'+teamname)
 
    line = fp1.readline()  # 调用文件的 readline()方法
    i=1

    head=['赛季','球队','时间','得分','命中%','投篮','三分%','三分','罚球%','罚球','篮板','前场','后场','助攻','抢断','盖帽','犯规']

    while line:
        print(line)
        bro.get(line)  

        jiqian = bro.find_elements_by_xpath('//*[@id="main-wrap"]/div[2]/div[3]/div[2]/ul[1]/li[1]/a')[0]
        jiqian.click()
        page_text = bro.page_source
        tree = etree.HTML(page_text)
        name=tree.xpath('//*[@id="inforCard"]/div[1]/h1/text()')[0]
        print('./team/'+teamname+'/'+name+'.csv')
        newFile = open('./team/'+teamname+'/'+name+'.csv', 'w')
        newWriter = csv.writer(newFile, lineterminator='\n')
        newWriter.writerow(['季前赛'])
        newWriter.writerow(head)

        trList = tree.xpath('//*[@id="main-wrap"]/div[2]/div[3]/div[2]/div/table/tbody/tr')

        for tr in trList:
            info=[]
            tdList=tr.xpath('./td')
            for td in tdList:
                info.append(td.xpath('./text()')[0]+'')
            newWriter.writerow(info)

        changgui=bro.find_elements_by_xpath('//*[@id="main-wrap"]/div[2]/div[3]/div[2]/ul[1]/li[2]/a')[0]
        changgui.click()
        page_text = bro.page_source
        tree = etree.HTML(page_text)
        newWriter.writerow(['常规赛'])
        newWriter.writerow(head)

        trList = tree.xpath('//*[@id="main-wrap"]/div[2]/div[3]/div[2]/div/table/tbody/tr')
    
        for tr in trList:
            info=[]
            tdList=tr.xpath('./td')           

            for td in tdList:
                temp = td.xpath('./text()')
                if len(temp)==0:
                    info.append('')
                else:
                    info.append(temp[0])
            newWriter.writerow(info)


        jihou=bro.find_elements_by_xpath('//*[@id="main-wrap"]/div[2]/div[3]/div[2]/ul[1]/li[3]/a')[0]
        jihou.click()
        page_text = bro.page_source
        tree = etree.HTML(page_text)
        newWriter.writerow(['季后赛'])
        newWriter.writerow(head)

        trList = tree.xpath('//*[@id="main-wrap"]/div[2]/div[3]/div[2]/div/table/tbody/tr')
    
        for tr in trList:
            info=[]
            tdList=tr.xpath('./td')
            for td in tdList:
                info.append(td.xpath('./text()')[0])
            newWriter.writerow(info)


        newFile.close()
   
        sleep(7)

        line = fp1.readline()
    fp1.close()


