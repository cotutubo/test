# -*- coding: utf-8 -*-
import re
import sys

import random , time, commands
from threading import Thread

start_time = time.time()

def main():

    def aho(a,b):
        if b == 0: return a
        return aho(b, a % b)

    print aho(167,100)

    def kuso(a,b):
        while b > 0:
            a,b = b, a % b
        return a
    print kuso(155,100)

    #print "start_time :" + str(start_time)
    #print "end_time   :" + str(time.time())
    #print "error      :" + str(errors)
    #print list(set(res)) #配列の重複を消去


if __name__ == "__main__":
    main()
