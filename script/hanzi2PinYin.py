#!/usr/bin/env python
# -*- coding: utf-8 -*-
##  算法有毛病。。。这个太慢了。。。
## 应该把姓氏和名字直接拆分开，然后按照同音来生成，快百倍吧。。不写了
from pinyin import PinYin

def getPinYin(hanzi):
    test = PinYin()
    test.load_word()
    return test.hanzi2pinyin(string=hanzi)

def headDaXie(hanzi_list):
    result = []
    for hanzi in hanzi_list:
        result.append(chr(ord(hanzi[0])-32)+hanzi[1:])
    return result

if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    wf = open(sys.argv[2],'w')
    s = ""
    for l in f:
        s += '-'.join(headDaXie(getPinYin(l.strip())))+"\n"
        #print s
    wf.write(s)
    f.close()
    wf.close()



