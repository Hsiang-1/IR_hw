from pprint import pprint
from baiduspider import BaiduSpider

result = BaiduSpider().search_web('Python')
print(result.baike.plain)  # print
print('\n\n')
pprint(result.baike.title)  # pprint

