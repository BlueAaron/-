import urllib2
import json
import string
url ='http://m.weather.com.cn/data/101090502.html'
re = urllib2.urlopen(url).read()
we = json.loads(re)['weatherinfo']
print we['city'] , we['date_y'].center(30) ,   we['week']
print we['temp1'], we['weather1'].center(30),  we['wind1']
print we['temp2'], we['weather2'].center(30),  we['wind2']
print we['temp3'], we['weather3'].center(30),  we['wind3']
print we['temp4'], we['weather4'].center(30),  we['wind4']
print we['temp5'], we['weather5'].center(30),  we['wind5']
print we['temp6'], we['weather6'].center(30),  we['wind6']
print we['index48_d']
raw_input('plese input Enter to esc')