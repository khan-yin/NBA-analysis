import requests
import time,datetime
from lxml import etree
from time import sleep
import csv
import os

file_dir = './matches'
date1 = 0
date2 = 0
for root,dirs,files in os.walk(file_dir):
    start=files[len(files)-1].split(" ")[0]
    timeArray1 = time.strptime(start, "%Y年%m月%d日")
    date1 = int(time.mktime(timeArray1))
    date = time.strftime("%Y:%m:%d");
    timeArray2 = time.strptime(date, "%Y:%m:%d")
    date2 = int(time.mktime(timeArray2))
url= 'https://nba.hupu.com/schedule/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
        'Safari/537.36 '
}
gap=604800
fp = open('./matchHtmls.txt', 'w', encoding='utf-8')
            
for i in range(date1,date2,gap):
    timeArray = time.localtime(i)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    detailUrl = url+otherStyleTime
    pageText = requests.get(url=detailUrl,headers=headers).text
    tree = etree.HTML(pageText)
    trList = tree.xpath('//*[@id="allteamNba"]/div[4]/table/tbody/tr[@class="left"]')
    for tr in trList:
        if tr.xpath('./td[3]/a/text()')[0]=='数据统计':
            data=tr.xpath('./td[3]/a/@href')[0]
            fp.write(data+'\n')
    sleep(3)
fp.close()


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
            'Safari/537.36 '
}
fp = open('./matchHtmls.txt', 'r', encoding='utf-8')
line = fp.readline()  # 调用文件的 readline()方法
while line:
    line=line.split('\n')[0]
    pageText = requests.get(url=line,headers=headers).text
    #print(pageText)
    tree = etree.HTML(pageText)
    detailDate=tree.xpath('/html/body/div[3]/div[4]/div[1]/div[1]/div[2]/div[2]/p[1]/text()')[0]
        
    d=detailDate.split('：')[1]
    date=d.split(' ')[0]
    timeArray = time.strptime(d, "%Y年%m月%d日 %H:%M")
    dat = int(time.mktime(timeArray1))
    now=time.time()
    if now<dat:
        continue


    homeTeam=tree.xpath('/html/body/div[3]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/p/a/text()')[0]
    awayTeam=tree.xpath('/html/body/div[3]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p/a/text()')[0]
    path='./matches/'+date+' '+homeTeam+' '+awayTeam+'.csv'
    newFile = open(path, 'w')
    newWriter = csv.writer(newFile, lineterminator='\n')
    newWriter.writerow([homeTeam])
    newWriter.writerow(['球员','位置','时间','投篮','3分','罚球','前场','后场','篮板','助攻','犯规','抢断','失误','封盖','得分','+/-'])
    trList=tree.xpath('//*[@id="J_home_content"]/tbody/tr')
    for tr in trList:
        if len(tr.xpath('./@class'))==1:
            continue
        data=[]
        data.append(tr.xpath('string(./td[1])'))
        data.append(tr.xpath('string(./td[2])'))
        data.append(tr.xpath('string(./td[3])'))
        data.append(tr.xpath('string(./td[4])'))
        data.append(tr.xpath('string(./td[5])'))
        data.append(tr.xpath('string(./td[6])'))
        data.append(tr.xpath('string(./td[7])'))
        data.append(tr.xpath('string(./td[8])'))
        data.append(tr.xpath('string(./td[9])'))
        data.append(tr.xpath('string(./td[10])'))
        data.append(tr.xpath('string(./td[11])'))
        data.append(tr.xpath('string(./td[12])'))
        data.append(tr.xpath('string(./td[13])'))
        data.append(tr.xpath('string(./td[14])'))
        data.append(tr.xpath('string(./td[15])'))
        data.append(tr.xpath('string(./td[16])'))
        
        newWriter.writerow(data)

    newWriter.writerow([awayTeam])
    newWriter.writerow(['球员','位置','时间','投篮','3分','罚球','前场','后场','篮板','助攻','犯规','抢断','失误','封盖','得分','+/-'])
    trList=tree.xpath('//*[@id="J_away_content"]/tbody/tr')
    for tr in trList:
        if len(tr.xpath('./@class'))==1:
            continue
        data=[]
        data.append(tr.xpath('string(./td[1])'))
        data.append(tr.xpath('string(./td[2])'))
        data.append(tr.xpath('string(./td[3])'))
        data.append(tr.xpath('string(./td[4])'))
        data.append(tr.xpath('string(./td[5])'))
        data.append(tr.xpath('string(./td[6])'))
        data.append(tr.xpath('string(./td[7])'))
        data.append(tr.xpath('string(./td[8])'))
        data.append(tr.xpath('string(./td[9])'))
        data.append(tr.xpath('string(./td[10])'))
        data.append(tr.xpath('string(./td[11])'))
        data.append(tr.xpath('string(./td[12])'))
        data.append(tr.xpath('string(./td[13])'))
        data.append(tr.xpath('string(./td[14])'))
        data.append(tr.xpath('string(./td[15])'))
        data.append(tr.xpath('string(./td[16])'))
        newWriter.writerow(data)
        
    line = fp.readline()
    sleep(3)
    newFile.close()


