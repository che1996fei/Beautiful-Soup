from bs4 import BeautifulSoup

html = '''
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
'''

#子节点
# soup = BeautifulSoup(html, 'lxml')
# # print(soup.p.contents)#用contents获得直接子节点
# # print(soup.p.children)
# # for i, child in enumerate(soup.p.children):
# #     print(i, child)                            #用children属性获取子节点并用for循环输出
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)                             #用descendants属性获得所有子孙节点并用for循环输出


