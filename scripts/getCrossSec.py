#read sigma from folder XXXXXX-{p1}-{p2}/Events/run_{p3}/ for a given p3
#it will find all available set of pairs of p1 and p2
#print out a file with p1,p2,sigma
#From command line you can give p3
#written by Giovanna Cottin with input from Gabriel Torrealba

import sys
import os
import numpy as np
import gzip
if len(sys.argv)>1:
    rn=int(sys.argv[1]) # Run number
    lep=sys.argv[2] # Process name
    outfile=sys.argv[3] if len(sys.argv)>3 else 'mg5_grid_'+lep+'_sigma_out.txt' #Outfile **can give full path**
else:
    sys.exit("NOT ENOUGH ARGUMENTS! USAGE: python getCrossSec.py [runNum] [flavor] [outputName]")
path = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid_2j_etacut/HNL_GRID_'+lep+'/'
print(path)
subfolders=[x for x in os.listdir(path) if os.path.isdir(path+x)]
subfolders.sort()
print(subfolders)
out={'p1':[],'p2':[],'sig':[],'gamma':[],'ctau':[]}

if lep == 'e':pid = '9900012'
elif lep=='mu':pid = '9900014'
else: pid = '9900016'
c = 2.99792458e8 #m/s
hbar = 6.5821e-25 #GeV*s


for ss in subfolders:
    #read p1 and p2
    sss=ss.split('-')
    print(sss)
    p1=sss[1]
    i0=3 if ''==sss[2] else 2
    if 'e' in sss[i0] and i0!=len(sss)-1:
        p2=sss[i0]+'-'+sss[i0+1]
    else:
        p2=sss[i0]
    if i0==3:p2='-'+p2
    print(p2)
    #get filename
    fp=path+ss+'/Events/run_{0:0>2}'.format(rn)
    print(fp)
    try:
        filename=[x for x in os.listdir(fp+'/') if 'banner.txt' in x][0] #read from banner
        print(fp+'/'+filename)
        if not os.path.isfile(fp+'/'+filename):continue
        with open(fp+'/'+filename) as ff:
            for l in ff:
                if '#  Integrated weight (pb)  :' in l:
                   sig=l.split()[-1]
                   # print l.split()
                if 'DECAY  '+pid in l:
                    decayWidth=l.split()[-1]
                    print(decayWidth, hbar*c/float(decayWidth)) 
        out['p1'].append(p1)
        out['p2'].append(p2)
        out['sig'].append(sig)
        out['gamma'].append(decayWidth)
        out['ctau'].append(hbar*c/float(decayWidth))
        #out['run'].append(rn)
    except Exception as e:
        print e
        print 'run not found in {0}-{1}'.format(p1,p2)

#idxs=np.argsort(out['p1'])
#print idxs
#print out
#for key in out:
#    out[key]=out[key][idxs]
assert(len(out['p1'])==len(out['p2']) == len(out['sig']) == len(out['gamma']) == len(out['ctau']))
with open(outfile,'w') as ff:
    # ff.write('{0:10}{1:10}{2:25}{3:5}\n'.format('p1','p2','sigma','run'))
    ff.write('mass[GeV] V sig gamma[GeV] ctau[m]\n')
    for i in range(len(out['p1'])):
	ff.write('{0:10}{1:10}{2:25}{3:25}{4:5}\n'.format(out['p1'][i], out['p2'][i], out['sig'][i], out['gamma'][i],out['ctau'][i]))
        ##ff.write('{0:10}{1:10}{2:25}{3:5}\n'.format(out['p1'][i],out['p2'][i],out['sig'][i],out['run'][i]))

'''
to read file easily
import numpy as np
a=np.loadtxt(outfile)
#To separate the columns one can do
p1=a[:,0]
p2=a[:,1]
sig=a[:,2]
run=a[:,3]
'''

