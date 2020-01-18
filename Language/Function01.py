#!/usr/bin/python

def greet_me(*args):
    if args is not None:
        for arg in args:
            print("arg = ", arg)

def greet_me_1(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("{} = {}".format(key, value))



greet_me('yasoob', 'python', 'egg', 'test')

greet_me_1(name = 'yay')