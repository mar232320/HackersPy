import time
import json
import os
import math
import threading

class TimeCalMT (threading.Thread):
   def __init__(self, threadID, progDamage, progInstallTime, progHitInterval, progProjectileTime, progAmount, isProgMulti, nodeFirewall, nodeRegeneration, nodeAmount):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.progDamage = progDamage
      self.progInstallTime = progInstallTime
      self.progHitInterval = progHitInterval
      self.progProjectileTime = progProjectileTime
      self.progAmount = progAmount
      self.isProgMulti = isProgMulti
      self.nodeFirewall = nodeFirewall
      self.nodeRegeneration = nodeRegeneration
      self.nodeAmount = nodeAmount

   def run(self):
       firewall = nodeFirewall
       regen = nodeRegeneration
       time = progInstallTime
       i = 0
       if int(progAmount) <= 0:
           return None
       if isProgMulti == 0:
           for x in range(1,int(nodeAmount)+1):
               while True:
                   if firewall <= 0:
                       break
                   i += 0.1
                   if i == max(progHitInterval - progProjectileTime, 0.1):
                       if (progDamage * int(progAmount)) / 10 > (firewall / 100 * regen) / 10:
                           firewall -= progDamage * int(progAmount) / 10
                       else:
                           return None
                       i = 0
                   firewall += (firewall / 100 * regen) / 10
                   time += 0.1
                   if time > 10000:
                       return time
                   firewall = nodeFirewall
       else:
           while True:
               if firewall <= 0:
                   break
               i += 0.1
               if i == max(progHitInterval - progProjectileTime, 0.1):
                   if (progDamage * int(progAmount)) / 10 > (firewall / 100 * regen) / 10:
                       firewall -= progDamage * int(progAmount) / 10
                   else:
                       return None
                   i = 0
               firewall += (firewall / 100 * regen) / 10
               time += 0.1
               if time > 10000:
                   return time
       return time
      
class stealthCalMT (threading.Thread):
   def __init__(self, threadID, visibility, stealthProgVisibility, stealthProgInstallTime):
      threading.Thread.__init__(self)
      self.visibility = visibility
      self.stealthProgVisibility = stealthProgVisibility
      self.stealthProgInstallTime = stealthProgInstallTime
   def run(self):
       self.fvis = stealthCal(self.visibility, self.stealthProgVisibility, self.stealthProgInstallTime)
       return self.fvis
     

def stealthCal(visibility, stealthProgVisibility, stealthProgInstallTime):
    time = 0
    i = 0
    while True:
        time += 20
        time += (stealthProgInstallTime * (stealthProgVisibility / 100 * visibility))
        i += 1
        if i == stealthProgInstallTime:
            break
        if time >= 3600:
            break
    return round(time,0)     
