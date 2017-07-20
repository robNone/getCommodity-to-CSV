# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pymongo import MongoClient
import re
conn =  MongoClient(host='127.0.0.1',port=27017)

client=conn['salesorder']
db = conn['easybiz']
def insertx(x):
	client.sqa.insert(x)
def select(x):
	rexExp = re.compile('^'+x+'.*')
	return db.sqa.find({'asin':{'$regex':x} })
def findone(ASIN):
	return	db.data.find_one({'asin':ASIN})
def insertData(data):
	db.data.insert(data)
def insertPage(page):
	db.page.insert(page)
def findAllPage():
	db.page.find()
def threadIn(pagg):
	client.page.insert(pagg)
def threadFind():
	return	db.page.find({})

def selectx(SKU):
	return client.sqa.find({'Account':SKU})
def insert(x):
	db.sqa.insert(x)
def Del():
	db.sqa.remove()  
	client.sqa.remove()  
	db.page.remove()
if __name__ == '__main__':
	for x in  threadFind():
		print x