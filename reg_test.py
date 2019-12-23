import urllib
import re

# 读取HTML源代码
sock = urllib.parse('http://yahoo.org/')
htmlSource = sock.read()
sock.close()
# 匹配，输出结果（[0:3]表示提取3个）
print('open tags:')
print(re.findall(r"<[^>][^>]*[^/>]>", htmlSource)[0:3])
print('close tags:')
# print re.findall
