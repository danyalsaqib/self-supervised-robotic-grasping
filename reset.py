import os

fh = open('objectstatus.txt', 'w')
fh.write(str(0))
fh.close

fh = open('graspfeedback.txt', 'w')
fh.write(str(90))
fh.close

fh = open('gc_file.txt', 'w')
fh.write(str(0))
fh.close

fh=open('cnnoutput.txt','w')
fh.write(str(0.4) + "\n")
fh.write(str(1000))
fh.close
