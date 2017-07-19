# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import db
import re

NewHeaders = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
              "Accept-Encoding": "gzip , 'deflate','br'",
              "Accept-Language": "zh-CN,zh;q=0.8",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
              "Cookie": "optimizelySegments=%7B%221260783744%22%3A%22false%22%2C%221275403343%22%3A%22referral%22%2C%221345201691%22%3A%22gc%22%2C%227652343073%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; optimizelyEndUserId=oeu1499415578985r0.3355847316223117; XSLE=ee25ad7c92816be6472857a7cfbe77aa; _ga=GA1.2.1066313304.1499415463; _xt=1499415507; _xe=https%3A%2F%2Fwww.xsellco.com%2F; _xr=https%3A%2F%2Fwww.xsellco.com%2F; XSESSID=7lgadaf2db0p2juhh3gsckdo66; XSC=1; mobile=false"
              }


def webGet(url):
    try:
        de = requests.get(url=url,
                          headers=NewHeaders)
        print de.status_code
        return de.text
    except Exception as e:
        return ''


def doerro(url):
    Result = ''
    while Result == "":
        Result = webGet(url)
        if Result != '':
            break
        print 'Network Error Retry----- '
    print url + ' go......Success'
    return Result


def DelLastChar(str):
    str_list = list(str)
    str_list.pop()
    return "".join(str_list)


def PageAnalysis(page):

    list = re.split("<tr data-target=", page)
    del list[0]
    for salesorder in list:
        try:
            if salesorder.find('text-success text-lg icon-dropbox') > 0:

                Acct = re.split("acct ", salesorder)[
                    1].split('"')[0].replace(' ', '')
                Account = re.split(
                    "star-rating", salesorder)[1].replace(" ", '')

                Umber = re.split(
                    'text-muted', Account)[1].split('>')[1].split('&')[0]
                Account = re.split(
                    'text-muted', Account)[1].split('>')[2].split('<')[0]
                Account = DelLastChar(Account)
                db.insertx({'Acct': Acct, 'Umber': Umber, 'Account': Account})

        except Exception as e:
            print e
if __name__ == '__main__':
    t = getSalesorder('https://dashboard.xsellco.com/salesorder?page=1')
    print (t.webGet())
