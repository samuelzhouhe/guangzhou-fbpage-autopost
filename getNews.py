import requests


def retrieveNews():
	res = requests.get('http://news.dayoo.com/guangdong/139996.shtml', auth=('user', 'pass'))

	wholePage = res.text
	allNews = ''
	newsCount = 0
	for i in range(len(wholePage)):
		if wholePage[i:i+22] == '.htm" target="_blank">' and wholePage[i+22]!='[' and wholePage[i+22]!='<' and newsCount < 10:
			newsCount += 1
			endPoint = i
			while endPoint< len(wholePage) and wholePage[endPoint:endPoint+2]!='</':
				endPoint += 1
			allNews += str(newsCount) + '. '
			allNews += wholePage[i+22:endPoint]
			allNews += '\n'
			
	allNews += "Credit: news are from http://news.dayoo.com/guangdong/139996.shtml"
	return allNews

