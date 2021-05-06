# 获取单词库
# 新东方 url = "https://www.koolearn.com/dict/zimu_a_1.html"
# 词根库 url = "http://www.etymon.cn/yingyucizhui/list_2_1.html"
import requests
from bs4 import BeautifulSoup
from lxml import etree

# url = "https://www.koolearn.com/dict/zimu_a_1.html"
url = "http://www.etymon.cn/yingyucizhui/list_2_1.html"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
re = requests.get(url,headers=head)
re.encoding = 'utf-8'
html = re.text
# print(html)

bs = BeautifulSoup(html,features="html.parser")
dl = bs.find("div",id='dictionary').find("dl")

for dt in dl.find_all('dt'):
    print(dt.text)
# print(dl.text)
# tree = etree.HTML(html)

