import os

fh = open('objectdetected.txt', 'w')
fh.write(str(0))
fh.close

fh = open('graspfeed.txt', 'w')
fh.write(str(90))
fh.close

fh=open('outputfile.txt','w')
fh.write(str(0.4) + "\n")
fh.write(str(1000))
fh.close

