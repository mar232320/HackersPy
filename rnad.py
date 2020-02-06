import os
import sys
dead= 3
for i in range (dead):
    print ("Hello")

print ("GoodBye")
os.execl(sys.executable, sys.executable, * sys.argv)