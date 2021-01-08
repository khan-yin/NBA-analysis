import requests
import random
from lxml import etree

url = 'https://sports.qq.com/nba/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 '
                  'Safari/537.36 '
}

def crawl_news():
    pageText = requests.get(url=url, headers=headers).text
    tree = etree.HTML(pageText)
    liList = tree.xpath('//*[@id="ct-screen1"]/div[3]/div[1]/ul/li')  # 动态新闻li标签列表
    length = len(liList) - 1
    rand = []
    for i in range(0, 7):  # 获取七个随机数
        temp = random.randint(0, length)
        while temp in rand:
            temp = random.randint(0, length)
        rand.append(temp)
    info = []  # 动态新闻数据列表
    for i in rand:
        newData = {}  # 新增的动态新闻标题和链接
        newData['href'] = liList[i].xpath('./a/@href')[0]  # 新闻链接
        newData['title'] = liList[i].xpath('./a/text()')[0]  # 新闻标题
        info.append(newData)

    # print(info)
    res = {
        'news': info
    }
    return res


if __name__ == '__main__':
    crawl_news()