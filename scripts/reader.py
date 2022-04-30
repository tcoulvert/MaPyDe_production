#check the efficiency of gen-level cuts on HNL

import sys
import os
import numpy as np
import gzip
import math

if len(sys.argv) < 2:
    print("Three parameters are required: python splitLHE.py [input filename]")
    exit()

inputfilename = sys.argv[1]

inputfile = gzip.open(inputfilename, "r")

pdgId = '9900016'
event_start_flag = False
total = 0
pass_cut = 1
for line in inputfile:
    if not event_start_flag:
        if   '<event>' in line: event_start_flag = True
        continue
    if pdgId in line and pdgId == line.split()[0]:
        
        px = float(line.split()[6])
        py = float(line.split()[7])
        pz = float(line.split()[8])
        # print(line.split())
        # print(px,py,pz)
        pt = (px**2+py**2)**0.5
        theta =  math.atan(pt/abs(pz))
        if theta > 0.0:
            eta = -1*math.log(math.tan(theta/2.))
            if pt >= 100 and abs(eta) < 3 and abs(eta)>0.5: pass_cut +=1
        total+=1
print(total, pass_cut, pass_cut*1.0/total)
