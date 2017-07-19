# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class getParmeter(object):
	"""docstring for postParmeter"""
	def __init__(self, arg,url,headers,TimeOut):
		super(postParmeter, self).__init__()
		self.arg = arg
		self.url = url
		self.headers=headers
		self.TimeOut=TimeOut
class postParmeter(object):
	"""docstring for postParmeter"""
	def __init__(self, arg,url,Data,headers,TimeOut):
		super(postParmeter, self).__init__()
		self.arg = arg
		self.url = url
		self.Data= Data
		self.headers=headers
		self.TimeOut=TimeOut