#-*- coding:utf-8 -*-

import urllib
import urllib2

#传入值和保存路径
def search(word,filepath):
	url="http://www.baidu.com/s?"

	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers={'User-Agent':user_agent}

	values={'wd':word}
	urlf=url+urllib.urlencode(values)

	response=urllib2.urlopen(urlf)
	html=response.read()

	open(filepath,'w').write(html)

	return 1