# -*- codeing = utf-8 -*-
import requests
from lxml import etree
import csv

url = 'https://nba.hupu.com/stats/teams'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
trList=tree.xpath('//*[@id="data_js_sort"]/tbody/tr')
i = 1
print(len(trList))

newFile = open('team_detail_info.csv', 'w')
newWriter = csv.writer(newFile, lineterminator='\n')
newWriter.writerow(['排名','球队','投篮命中率','投篮命中','投篮出手','三分命中率','三分命中','三分出手','罚球命中率','罚球命中','罚球出手','总篮板','进攻篮板','防守篮板','助攻','失误','抢断','盖帽','犯规','得分'])

for tr in trList:
    if i ==1 or i == 2:
        i = i + 1
        continue
    i = i + 1
    paiming=tr.xpath('./td[1]/text()')[0];
    qiudui=tr.xpath('./td[2]/a/text()')[0];
    tou1=tr.xpath('./td[3]/text()')[0];
    tou2=tr.xpath('./td[4]/text()')[0];
    tou3=tr.xpath('./td[5]/text()')[0];
    san1=tr.xpath('./td[6]/text()')[0];
    san2=tr.xpath('./td[7]/text()')[0];
    san3=tr.xpath('./td[8]/text()')[0];
    fa1=tr.xpath('./td[9]/text()')[0];
    fa2=tr.xpath('./td[10]/text()')[0];
    fa3=tr.xpath('./td[11]/text()')[0];
    lan1=tr.xpath('./td[12]/text()')[0];
    lan2=tr.xpath('./td[13]/text()')[0];
    lan3=tr.xpath('./td[14]/text()')[0];
    zhu=tr.xpath('./td[15]/text()')[0];
    shi=tr.xpath('./td[16]/text()')[0];
    qiang=tr.xpath('./td[17]/text()')[0];
    gai=tr.xpath('./td[18]/text()')[0];
    fan=tr.xpath('./td[19]/text()')[0];
    de=tr.xpath('./td[20]/text()')[0];
    info=[paiming,qiudui,tou1,tou2,tou3,san1,san2,san3,fa1,fa2,fa3,lan1,lan2,lan3,zhu,shi,qiang,gai,fan,de]
    newWriter.writerow(info)
newFile.close()



