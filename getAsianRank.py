# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import sys
import time
import selenium
import  requests
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
reload(sys)
sys.setdefaultencoding('utf8')

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def dSelenium(asin,cookies,porx):
	# dcap = dict(DesiredCapabilities.PHANTOMJS)
	# dcap["phantomjs.page.settings.userAgent"] = (
	# 	"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
	# 	)
	proxy = Proxy(
    {
        'httpProxy': porx
    }
	)
	desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
	proxy.add_to_capabilities(desired_capabilities)
	obj = webdriver.PhantomJS(executable_path='C:/Users/16344/Desktop/getCommodity to CSV/phantomjs-2.1.1-windows/bin/phantomjs.exe'.decode('utf-8').encode('gbk'),  desired_capabilities=desired_capabilities)
	obj.add_cookie(cookies)
	obj.set_page_load_timeout(5)
	print 'aaaaaaaaaaaaaaaaaaaaaa'
	try:
   		obj.get('http://www.ziniao.com/view_details.html?keyword=B01LW98GQM&site=US')
		print obj.text
	except Exception as e:
		print e
	driver.close()
	return obj.text
postheaders ={ "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip , 'deflate','br'",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
           	"Referer":"http://www.ziniao.com/login.html",
            "Origin": "http://www.ziniao.com"
            }
data        ={
		"username":'15558053695@163.com',
		"password":'123456',
		"geetest_challenge":'',
		"geetest_validate":'',
		"geetest_seccode":'',
		"gt_server_status_code":'',
		"userId":'',
		"rememberMe":"on"
        }

if __name__ == '__main__':
	r=''
	while r== '':
		try:
			sr =requests.get(url= 'http://www.66ip.cn/getzh.php?getzh=2017071401688&getnum=1&isp=0&anonymoustype=2&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=https').text.split('<')[0].replace('\r\n','').replace(' ','').replace('\t','')
			print sr
			proxies={
				"http": "http://"+sr,  
				"https": "https://"+sr,  
				}
			headers     ={ "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip , 'deflate','br'",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            "Cookie":"SHAREJSESSIONID=dedf3a1c-37f2-4479-9877-b7fa303a90c1; rememberMe=ORYN7Lrf50XO9RhDT4iwn9VPP1tJimopbjnC0zBHNx8lGqLBsZiSWhbDGCFCi8Rl33VCnxJhpkmVGGi3ibPnfudHl0DqoVxzUE5FS4wqIoEvTRJfQ01xcOGjPWvUhivFhjaNgg+p90Aqmpl+9DrT9J7yyJDftbzWXS52x1AyVMNRfN80pnuZqjRLLO1EyA4DsF4xmDtoh6TdtMkhf4lQHvomCyqkfwV4y2sby1XYud0MmSNE3tq7Qpbzlogm/eTkWiTtU0NXFoQcseSOhHRSL/Xx+SPD/ssDFds+4yLCRwWXGHOwvMXICdcUnHAjbArxxEaRFSuKgUTYqmxzst1TUt9Kefjh3vXpxBcCytn95gaqzmF4cWw77RAFx9XcJUxCYtk5ETTEuooTpolcezBrx64YYANlDDvNKkoCpA6nZOkhWdjnQkubeIKZOSGsdk47KWSGIK6QSAzjt9XU9LxwPJiMCEHNSC2tzQfwN9aI6mjtA6m+o93iaYHR5CelShSMn4ehuP1NgXO59eogLL9n6wakAh8VwogtqiQWix1iFCDcgWtmkKVkjvm8QIA6o8MH3ij0rHbm7RQ0ZT0zLsBSXgmuRz/pfUpIOa6RlEUt+j8N2rADYBxkqgnvyqXjCxHdxQ9QT5Pn3cIOkiHZwNKZGdcROBvpRm/qosgJNyNowvZiy2yxApIu2gaGlGNhFbo9swwK+dwp56QGjVe1OfIMg9h6J5wr2ghHWqsxoqhoHyo=; id=81b9f0c48cb5816e; username=15558053695%40163.com; type=0; AWSELB=C3D9FDF90A2BD82AE2851173282959FE68EF0572634AA60239182F1DB9F36A2416E7D974E64C0301E40DA13E1FEDB5AD836C3A1ACFF0195AEB8BB79C1FD02848F2D059C857; Hm_lvt_d3128fb229f35448f6a7c9860be9f14d=1498550925,1500427787,1500429236; Hm_lpvt_d3128fb229f35448f6a7c9860be9f14d=1500432940"
            
            }
			# r=requests.post(url='http://api.ziniao.com//login?',headers=postheaders,data=data,proxies=proxies ,timeout=10)
			# r= requests.get(url='http://api.ziniao.com//sp?asin=B00CVTZKB2&site=US',headers=headers,proxies=proxies ,timeout=5)
			# time.sleep(5)
			headers     ={ "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip , 'deflate','br'",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
           
            }
			r= requests.get(url='https://www.amazon.com/Za-White-Protector-Sunscreen-Spf26/dp/B00F15V9ZY/ref=sr_1_1_a_it?ie=UTF8&qid=1500443793&sr=8-1&keywords=za',headers=headers,proxies=proxies,timeout=5 ).text
			print r
		except Exception as e:
			print e
 
	 
