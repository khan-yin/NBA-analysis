
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}
url = 'https://nba.hupu.com/'
pageText = requests.get(url=url, headers=headers).text
tree = etree.HTML(pageText)

aList = tree.xpath('/html/body/div[1]/section[1]/div[1]/div/div[1]/div[1]/div/div[1]/a')
info=[]
for a in aList:
    link=a.xpath('./@href')[0]
    img=a.xpath('./div[1]/div[1]/img/@data-src')[0]
    titleTag=a.xpath('./div[2]/span/text()')
    title=''
    if len(titleTag)!=0:
        title=titleTag[0]
    flag=0
    for data in info:
        if data['link']==link:
            flag=1
            break
    if flag==0:
        newData={}
        newData['link']=link
        newData['img']=img
        newData['title']=title
        info.append(newData)
print(info)