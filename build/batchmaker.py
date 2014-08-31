#!/usr/bin/python3.4
# rainy_day_hackers
# August 30, 2014

import sys

filename='thebatch'
token='token123'
name1='emp'
name2='guest'
j=3
count=int(sys.argv[1])
print("-T 0 -K {1} -E {2} -A {3}".format(j,token,name1,filename))
print("-T 1 -K {1} -E {2} -A {3}".format(j,token,name2,filename))
while j < count:
    print("-T {0} -K {1} -E {2} -A -R {4} {3}".format(j,token,name1,filename,j))
    j+=1
    print("-T {0} -K {1} -E {2} -L -R {4} {3}".format(j,token,name1,filename,(j-1) ))
    j+=1
    print("-T {0} -K {1} -E {2} -A -R {4} {3}".format(j,token,name2,filename,j))
    j+=1
    print("-T {0} -K {1} -E {2} -L -R {4} {3}".format(j,token,name2,filename,(j-1)))
    j+=1

