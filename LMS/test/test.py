#! /usr/bin/env python
# -*- coding: utf-8 -*-

def ts(func):
    def test():
        print "this is ts"
        func()
    return test

@ts
def mytest():
    print "this is my test"
    return "ok"

mytest()

def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func

def myfunc():
    print(" myfunc() called.")

myfunc = deco(myfunc)

@deco
def myfunc():
    print(" myfunc() called.")

myfunc()

print "_______________________________-"

def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    return _deco

@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b

myfunc(1, 2)
myfunc(3, 4)

def deco(arg):
    def _deco(func):
        def _deco(a, b):
            print("before myfunc() called."),arg
            ret = func(a, b)
            print("  after myfunc() called. result: %s" % ret)
            return ret
        return _deco
    return _deco

@deco("hehe")
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b

myfunc(1, 2)

print "#" * 20

def hh(arg1):
    print "this is hh",arg1

hh(1)

def yefei(aa,bb="BB",*arg):
    print aa
    print bb
    for each in arg:
        print each

yefei("AA")
yefei("AA","BBB")
yefei('AA','BBB','CCC','DDD','EEE')

mytuple=('ff','hh')
yefei('AA',*mytuple)

print "?" * 30
def zhangliu(aa,**arg):
    print aa
    for each in arg.keys():
        print each,arg[each]
zhangliu('AA',bb='BBB',cc='CCC',dd='DDD',ee='EEE')
mydic={'bb':'BBB','cc':'CCC'}
zhangliu('aaa',**mydic)

