import requests
import random
from lxml import etree
url = 'https://sports.qq.com/nba/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}

pageText = requests.get(url = url, headers = headers).text
tree = etree.HTML(pageText)
liList = tree.xpath('//*[@id="ct-screen1"]/div[3]/div[1]/ul/li')#动态新闻li标签列表
len = len(liList) - 1
rand = []
for i in range(0,8):#获取八个随机数
    temp = random.randint(0,len)
    while temp in rand:
        temp = random.randint(0,len)
    rand.append(temp)
info = [] # 动态新闻数据列表
for i in rand:
    newData={} #新增的动态新闻标题和链接
    newData['href'] = liList[i].xpath('./a/@href')[0]#新闻链接
    newData['title'] = liList[i].xpath('./a/text()')[0]#新闻标题
    info.append(newData)
    