# -*- coding: utf-8 -*-
#!/usr/bin/python
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

print "**" * 30

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()


def my(aa):
    print aa
    def mydecorator(func):
        def myfunc(x):
            print "I'm here"
            func(x)
        return myfunc
    return mydecorator

@my('hello')
def yefei(x):
    print x

yefei('hello world')

