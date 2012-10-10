#!/usr/bin/env python
import urllib
import re

def grabber():
        '''Grabber method which grabs xkcd.com'''
        print '''Enter the directory where you want to rip xkcd
Example : C:/xkcd , make sure this folder exists !'''

        path = raw_input()

        print 'Ripping xkcd.com! sit back and relax !'

        for i in range(2000):
                try:
                        page = urllib.urlopen('http://xkcd.com/'+str(i))
                        print 'http://xkcd.com/'+str(i)
                        lines = page.readlines()
                        txt = ','.join(lines)
                        gt = '< '.replace(' ','')
                        match_object = re.search(gt+'img src="(.*?)" title=',txt)
                        img = match_object.group(1)
                        urllib.urlretrieve(img,path+'/'+str(i)+'.png')

                except AttributeError:
                        pass

def Main():
        grabber()

if __name__=='__main__':
        Main()

