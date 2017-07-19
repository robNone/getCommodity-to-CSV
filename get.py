# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import salesorder
from DB import db
from models import paramete
import json
import ast
import xlwt
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')
import time
headers     ={ "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip , 'deflate','br'",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            "Cookie":"optimizelySegments=%7B%221260783744%22%3A%22false%22%2C%221275403343%22%3A%22referral%22%2C%221345201691%22%3A%22gc%22%2C%227652343073%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; optimizelyEndUserId=oeu1499415578985r0.3355847316223117; __storejs__=%22__storejs__%22; _bizo_bzid=a780f31c-05fb-4344-94c6-aa27ed284688; _bizo_cksm=6A59C76D4B543E25; _bizo_np_stats=155%3D2541%2C; XSLE=ee25ad7c92816be6472857a7cfbe77aa; _ga=GA1.2.1066313304.1499415463; _gid=GA1.2.1439516595.1499415463; _uetsid=_uet80dca3be; _xt=1499415507; _xe=https%3A%2F%2Fwww.xsellco.com%2F; _xr=https%3A%2F%2Fwww.xsellco.com%2F; XSESSID=7lgadaf2db0p2juhh3gsckdo66; XSC=1; mobile=false"
            }


def webGet(url):
 	try:
		de = requests.get(url=url,
                      headers=headers)
		print de.status_code
		return de.text
	except Exception as e:
		return ''

def doerro(url ):
	Result=''
	while Result=="":
		Result=webGet(url )
		if Result!='':
			break
		print 'Network Error Retry----- '
	print url+' go......Success'
	return Result

def Geteasybiz():
	url='''https://rocksmith.easybiz.me/mgmt/inventory/products.json?order=asc'''
	header={ "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip , 'deflate','br'",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "content-type":"application/json",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            "Cookie":"__cfduid=d2facef24d4af40a601c6362c6a4a60c21499654923; __utmt=1; _session_id=02411f0d72bff7141e967922e58d4062; __utma=155848495.597294401.1499654877.1499654877.1499654877.1; __utmb=155848495.4.10.1499654877; __utmc=155848495; __utmz=155848495.1499654877.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=168714914.369701341.1499654922.1499654922.1499654922.1; __utmb=168714914.4.10.1499654922; __utmc=168714914; __utmz=168714914.1499654922.1.1.utmcsr=easybiz.me|utmccn=(referral)|utmcmd=referral|utmcct=/"
            }
	re=requests.get(url=url,headers=header)
	print str(re.text)
	easybizJson=json.loads(str(re.text)) 
	db.Del()
	for jso in easybizJson:
		db.insert(jso)
	for x in xrange(100):
		url='https://dashboard.xsellco.com/salesorder?page='+str(x+1)
		salesorder.PageAnalysis(salesorder.doerro(url))
		
if __name__ == '__main__':
	Geteasybiz()


def fooget(url):
	strl=str( doerro(url))
	s=re.split("1 - 100 of ",strl)[1].split('<')[0]
	li=[]
	sc= int(s.replace(',','').replace('  ',''))//100
	for x in range(sc+1):
		lista= re.split('<tr',strl)
		del lista[0:2]
		for z in lista:
			zhanghao= z[z.find('title'):].split('"')[1]
			SKU=z[z.find('fs_sku='):].split('=')[1].split('"')[0]
			ASIN=z[z.find('offer-listing'):].split('/')[1].split('"')[0]
			name=z[z.find('offer-listing'):].split('>')[1].split('<')[0]
			hasUMber=z[z.find('FBA'):].split('"')[1].replace('In stock:','').replace('New','')
			sellers=z[z.find('text-muted text-muted js-twipsy'):].split('"')[4] 
			BuyBoxPrice=z[z.find('Buy Box price'):].split('>')[1].split('<')[0] 
			LowestPrice= re.split('Shipping',z)[2].split('>')[1].split('<')[0]
			MyPrice=re.split('Shipping',z)[3].split('>')[1].split('<')[0]
			MyLowestPrice=re.split('text-lg input-group-prepend',z)[1].split('=')[7].split('"')[1] 
			MyHighestPrice=re.split('text-lg input-group-prepend',z)[2].split('value')[1].split('"')[1] 
			if z.find('icon-line-chart')>0:
				Rank=z[z.find('icon-line-chart'):].split('>')[2].split('<')[0] 
			else:
				Rank=''
			if z.find('selected')>0:
				selected=z[z.find('selected'):].split('>')[1].split('<')[0] 
			else:
				selected=''
			value=0
			cz=0.0
			for x in db.select(ASIN):
				if x['price']!=None:
					if x['price']!=1.0:
						value+=float(x['price'])
						cz+=1.0
			if value!=0:
				value= value/cz
			sales=0
			for key in db.selectx(SKU):
				  
				if zhanghao.replace('acct ','')==key['Acct']:
					sales+= int(key['Umber'])

			matchbuybox=0
			Umatchbuybox=0
			try:
				if (BuyBoxPrice!='' )and (MyLowestPrice!=''):
					matchbuybox= float(MyLowestPrice.replace(',','').replace('$',''))-float(BuyBoxPrice.replace(',','').replace('$','').replace('C','').replace('$',''))
				if matchbuybox<=0:
					Umatchbuybox=True
				else :
					Umatchbuybox=False

			except Exception as e:
				print e
				print 'erro:matchbuybox'
			Laptop=0
			Desktop=0
			try:
				if value!=0:
					Laptop=(float(MyPrice.replace('$','').replace('C','').replace(',',''))*0.94-value-10)	/float(MyPrice.replace(',','').replace('C','').replace('$','')	)
					Desktop=(float(MyPrice.replace(',','').replace('C','').replace('$',''))*0.94-value-20)	/float(MyPrice.replace(',','').replace('C','').replace('$','')	)
			
			except Exception as e:
				print e
			zoheader={ "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip , 'deflate','br'",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "content-type":"application/json",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            "Cookie":'AWSELB=C3D9FDF90A2BD82AE2851173282959FE68EF057263227BD1F17315BF6F30C6947A3990B930A1D0F3F7F9549AB29A1725A1DB32C5D9223E6F3F1E909D6C9CBF48B3E2010B4B; SHAREJSESSIONID=32286a46-e40f-427a-a1ce-668e546b1eae; rememberMe=jnSJ4htAGHHBVKKSVE71H5MqifGE5w7TvkUob+u6p9rVJcOX6ZPTpUyHtCUtJEatJDjc8Eg64fG34MQj/NutX0izsRxwF+Vhh1qrKNOiOecnblRfaV4AzZKzb6VCu+OZpK/is/U0Ozwwd0JIy8+lkNn6+e/FNh0sX4s/eZg0AHt+Ay0qI6nJRWRvp+uTMJRJ0aixzK4IJVU/x69vSJwwuM3vGvF8Iwn5pvLKiu+2C1mYYu63UwKlbz1LHjON43x+cT4tibOSUUm9w+AafYZ/kcJW+kGuKgwIjDQ9TZe+tWDoH15CP3jiFyRGzysudbMG9im/LL1CsxXddaMb1kjqUmHVWtSbsd8Pf9/rP0NeZEDGKrAPInOoLfaWCoqrVR9M8VgTc6AMW7RCRSQp6JkrJ/lUOgoyVBMKJxsT9Q6mzqgZLSl956xxIl0BAT+2puI07OTAwwQNraa/2f2yUC43fiV7GO3ugsJIh75viuWynEoe0UdSroVsXPL7VhpqlTgCFl7ajfayp91Ssde7cvmb7uR6s7ZPpU1Gl1xzuIWaKO/wULbjADoNcT9hOKBb3DYpRELbltBvh8eVov//Y17Plab8UDJJuFvGP2zLmJyAjtqYr714z1NEUoCg8RDpB7An8TNkMYyzYwUflZmaKpkbCMenJ/S71dtVeBhcT0yD/kKOwSoJfD1e29KcvNwbUj5vDVKLas4Xm4HPV8dIFBTiUA==; id=6add5714f634642c; username=1634475170%40qq.com; type=0; Hm_lvt_d3128fb229f35448f6a7c9860be9f14d=1498550925; Hm_lpvt_d3128fb229f35448f6a7c9860be9f14d=1500015603'
            }
			# data={}
			# if ASIN!='':
			# 	if db.findone(ASIN)==None:
			# 		data['rank']=0
			# 		print data
			# 		while  data['rank']==0:
			# 			try:
			# 				req=requests.get(url='http://api.ziniao.com//sp?asin='+ASIN,headers=zoheader)
			# 				print req.text
			# 				jsona=json.loads(req.text)

			# 				data=jsona['data']['content']
			# 				print data
			# 				print data['rank']
			# 			except Exception as e:
			# 				data['rank']==0
			# 				print 'json erro'
			# 			print data
			# 		db.insertData(data)
			# 	else :
			# 		data =db.findone(ASIN)
			# print data
			# print ASIN,data['rank'],data['reviews']
			# rank =data['rank']
			# reviews=['reviews']
			# star=['star']

			az=(zhanghao,SKU,ASIN,name,hasUMber,sellers,Rank,BuyBoxPrice,LowestPrice,MyPrice,MyLowestPrice,MyHighestPrice,Umatchbuybox,selected,Laptop,Desktop,value,sales)
			li.append(az)
		try:

			strl=doerro('https://dashboard.xsellco.com'+strl[strl.find('Next'):].split('"')[2])
 			
 		except Exception as e:
 			print e
 	return li
# def timer():  
#     ''''' 
#     每n秒执行一次 
# 	'''
# 	list=['https://shop.bitmain.com/overview.htm?name=antminer_l3_litecoin_asic_scrypt_miner','https://shop.bitmain.com/overview.htm?name=antminer_s9_asic_bitcoin_miner']  
# 	while True:
# 		for x in list:
# 			req=	doerro(x)  
# 		print time.strftime('%Y-%m-%d %X',time.localtime())    
# 		yourTask()  # 此处为要执行的任务    
# 		time.sleep(1)  
if __name__ == '__main__':

	# url=('https://feedback.aliexpress.com/display/productEvaluation.htm#feedback-list/display/productEvaluation.htm#feedback-list')
	header={ "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip , 'deflate','br'",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "content-type":"application/json",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            }
	# data={'data':'ownerMemberId=223330755&memberType=seller&productId=32802110508&companyId=&evaStarFilterValue=all+Stars&evaSortValue=sortdefault%40feedback&page=5&currentPage=4&startValidDate=&i18n=true&withPictures=false&withPersonalInfo=false&withAdditionalFeedback=false&onlyFromMyCountry=false&version=0.0.0&translate=+Y+&jumpToTop=false&_csrf_token=YHIM4VDse0OOxBBFRGi275'}
	# print requests.post(data=data,url=url,headers=headers).text
	while True:
		# Geteasybiz()
		lista= fooget('https://dashboard.xsellco.com/repricer?fai_is_configured%5B%5D=1&fgte_quantity=1')
		lista+=fooget('https://dashboard.xsellco.com/repricer?fai_is_configured%5B%5D=0&fgte_quantity=1')
		import csv
		csvfile = file('csvtest.csv', 'wb')
		writer = csv.writer(csvfile)
		lista.insert(0,('Acct ','SKU','ASIN','Title','Inventory','Sellers','Rank','Buy Box Price','Lowest Price','My Price','My LowestPrice','My HighestPrice','Match Buybox','Repricer','Laptop Profit Rate','Desktop Profit Rate','EB Cost','10 Days sales'))
		writer.writerows(lista)
		csvfile.close()
		time.sleep(86400)
