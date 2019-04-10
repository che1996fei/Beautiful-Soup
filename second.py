from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 选择元素
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title) #打印输出title节点的选择结果
# print(type(soup.title)) #输出title节点的类型
# print(soup.title.string) #获得title节点的文本内容
# print(soup.head) #输出头节点
# print(soup.p) #输出p节点

#提取信息
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title.name)#获取名称
# print(soup.p['name'])#获取属性
# print(soup.p['class'])
# print(soup.p.string)#获取文本

#嵌套选择
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

