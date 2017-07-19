# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def webGet(url):
 	try:
		de = requests.get(url=url,
                      headers=headers)
		print de.status_code
		return de.text
	except Exception as e:
		return ''

def requests(url ):
	Result=''
	while Result=="":
		Result=webGet(url )
		if Result!='':
			break
		print 'Network Error Retry----- '
	print url+' go......Success'
	return Result