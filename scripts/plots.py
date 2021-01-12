#################################################
# Plotting script for HNL
# Written by Giovanna Cottin (gfcottin@gmail.com)
#################################################
import os,sys
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.random import normal
import matplotlib.font_manager as font_manager
from matplotlib.colors import LogNorm
from matplotlib.ticker import ScalarFormatter 
from pylab import *
import matplotlib.gridspec as gridspec
from numpy import linspace, meshgrid
#from matplotlib.mlab import griddata
#################################################


#### Testing benchmarks for HNL_e ####

elecMixing= True
muonMixing= False
tauMixing = False

if(elecMixing==True): 
	folder="HNL_e"
	title= "Electron Mixing"
if(muonMixing==True): 
	folder="HNL_mu"
	title= "Muon Mixing"

if(tauMixing==True): 
	folder="HNL_tau"
	title= "Tau Mixing"

dat_dir = "/Users/christinawang/programs/pythia8303/examples/HNL_Plots/"


decays_5_1e7  = dat_dir +folder+"/decays_GRID-5-1e-07.dat"
decays_10_1e7 = dat_dir +folder+"/decays_GRID-10-1e-07.dat"

decays_5_1e7_data   = {0:[],1:[],2:[],3:[],4:[],5:[]}
decays_10_1e7_data  = {0:[],1:[],2:[],3:[],4:[],5:[]}

decays_quark_5_1e7  = dat_dir +folder+"/decays_quark_GRID-5-1e-07.dat"
decays_quark_10_1e7 = dat_dir +folder+"/decays_quark_GRID-10-1e-07.dat"
decays_lepton_5_1e7 = dat_dir +folder+"/decays_lepton_GRID-5-1e-07.dat"
decays_lepton_10_1e7 = dat_dir +folder+"/decays_lepton_GRID-10-1e-07.dat"



decays_lepton_5_1e7_data  = {0:[],1:[],2:[],3:[]}
decays_lepton_10_1e7_data = {0:[],1:[],2:[],3:[]}

decays_quark_5_1e7_data   = {0:[],1:[],2:[],3:[]}
decays_quark_10_1e7_data  = {0:[],1:[],2:[],3:[]}


for line in open(decays_lepton_5_1e7,"r"):
  for i,C in enumerate(line.split()): decays_lepton_5_1e7_data[i].append(float(C))
for line in open(decays_quark_10_1e7,"r"):
  for i,C in enumerate(line.split()): decays_quark_10_1e7_data[i].append(float(C))
for line in open(decays_lepton_10_1e7,"r"):
  for i,C in enumerate(line.split()): decays_lepton_10_1e7_data[i].append(float(C))
for line in open(decays_quark_5_1e7,"r"):
  for i,C in enumerate(line.split()): decays_quark_5_1e7_data[i].append(float(C))

Energy_lepton_5_1e7       = np.array(decays_lepton_5_1e7_data[1])
eta_lepton_5_1e7          = np.array(decays_lepton_5_1e7_data[2])
phi_lepton_5_1e7          = np.array(decays_lepton_5_1e7_data[3])

Energy_quark_5_1e7       = np.array(decays_quark_5_1e7_data[1])
eta_quark_5_1e7          = np.array(decays_quark_5_1e7_data[2])
phi_quark_5_1e7          = np.array(decays_quark_5_1e7_data[3])

Energy_lepton_10_1e7       = np.array(decays_lepton_10_1e7_data[1])
eta_lepton_10_1e7          = np.array(decays_lepton_10_1e7_data[2])
phi_lepton_10_1e7          = np.array(decays_lepton_10_1e7_data[3])

Energy_quark_10_1e7       = np.array(decays_quark_10_1e7_data[1])
eta_quark_10_1e7          = np.array(decays_quark_10_1e7_data[2])
phi_quark_10_1e7          = np.array(decays_quark_10_1e7_data[3])


for line in open(decays_5_1e7,"r"):
  for i,C in enumerate(line.split()): decays_5_1e7_data[i].append(float(C))
for line in open(decays_10_1e7,"r"):
  for i,C in enumerate(line.split()): decays_10_1e7_data[i].append(float(C))
tau_5_1e7          = np.array(decays_5_1e7_data[0])/299.792 # in ns
ctau_5_1e7         = np.array(decays_5_1e7_data[0])# in mm
decayLenght_5_1e7  = np.array(decays_5_1e7_data[1])
Gamma_5_1e7        = np.array(decays_5_1e7_data[2])
#betaGamma_5_1e7   = np.array(decays_5_1e7_data/decays_5_1e7_data[0])## L/ctau
Energy_5_1e7       = np.array(decays_5_1e7_data[3])
eta_5_1e7          = np.array(decays_5_1e7_data[4])
phi_5_1e7          = np.array(decays_5_1e7_data[5])


tau_10_1e7          = np.array(decays_10_1e7_data[0])/299.792 # in ns
ctau_10_1e7         = np.array(decays_10_1e7_data[0])# in mm
decayLenght_10_1e7  = np.array(decays_10_1e7_data[1])
Gamma_10_1e7        = np.array(decays_10_1e7_data[2])
#betaGamma_10_1e7    = np.array(decays_10_1e7_data/decays_5_1e7_data[0])## L/ctau
Energy_10_1e7       = np.array(decays_10_1e7_data[3])
eta_10_1e7          = np.array(decays_10_1e7_data[4])
phi_10_1e7          = np.array(decays_10_1e7_data[5])

decays_5_1e8  = dat_dir+folder+"/decays_GRID-5-1e-08.dat"
decays_10_1e8 = dat_dir+folder+"/decays_GRID-10-1e-08.dat"

decays_5_1e8_data   = {0:[],1:[],2:[],3:[],4:[],5:[]}
decays_10_1e8_data  = {0:[],1:[],2:[],3:[],4:[],5:[]}

for line in open(decays_5_1e8,"r"):
  for i,C in enumerate(line.split()): decays_5_1e8_data[i].append(float(C))
for line in open(decays_10_1e8,"r"):
  for i,C in enumerate(line.split()): decays_10_1e8_data[i].append(float(C))
tau_5_1e8          = np.array(decays_5_1e8_data[0])/299.792 # in ns
ctau_5_1e8         = np.array(decays_5_1e8_data[0])# in mm
decayLenght_5_1e8  = np.array(decays_5_1e8_data[1])
Gamma_5_1e8        = np.array(decays_5_1e8_data[2])
#betaGamma_5_1e8   = np.array(decays_5_1e8_data/decays_5_1e8_data[0])## L/ctau
Energy_5_1e8       = np.array(decays_5_1e8_data[3])
eta_5_1e8          = np.array(decays_5_1e8_data[4])
phi_5_1e8          = np.array(decays_5_1e8_data[5])


tau_10_1e8          = np.array(decays_10_1e8_data[0])/299.792 # in ns
ctau_10_1e8         = np.array(decays_10_1e8_data[0])# in mm
decayLenght_10_1e8  = np.array(decays_10_1e8_data[1])
Gamma_10_1e8        = np.array(decays_10_1e8_data[2])
#betaGamma_10_1e8    = np.array(decays_10_1e8_data/decays_5_1e8_data[0])## L/ctau
Energy_10_1e8       = np.array(decays_10_1e8_data[3])
eta_10_1e8          = np.array(decays_10_1e8_data[4])
phi_10_1e8          = np.array(decays_10_1e8_data[5])



decays_lepton_5_1e8  =dat_dir+folder+"/decays_lepton_GRID-5-1e-08.dat"
decays_lepton_10_1e8 =dat_dir+folder+"/decays_lepton_GRID-10-1e-08.dat"

decays_quark_5_1e8  = dat_dir+folder+"/decays_quark_GRID-5-1e-08.dat"
decays_quark_10_1e8 = dat_dir+folder+"/decays_quark_GRID-10-1e-08.dat"


decays_lepton_5_1e8_data  = {0:[],1:[],2:[],3:[]}
decays_lepton_10_1e8_data = {0:[],1:[],2:[],3:[]}

decays_quark_5_1e8_data   = {0:[],1:[],2:[],3:[]}
decays_quark_10_1e8_data  = {0:[],1:[],2:[],3:[]}


for line in open(decays_lepton_5_1e8,"r"):
  for i,C in enumerate(line.split()): decays_lepton_5_1e8_data[i].append(float(C))
for line in open(decays_quark_10_1e8,"r"):
  for i,C in enumerate(line.split()): decays_quark_10_1e8_data[i].append(float(C))
for line in open(decays_lepton_10_1e8,"r"):
  for i,C in enumerate(line.split()): decays_lepton_10_1e8_data[i].append(float(C))
for line in open(decays_quark_5_1e8,"r"):
  for i,C in enumerate(line.split()): decays_quark_5_1e8_data[i].append(float(C))

Energy_lepton_5_1e8       = np.array(decays_lepton_5_1e8_data[1])
eta_lepton_5_1e8          = np.array(decays_lepton_5_1e8_data[2])
phi_lepton_5_1e8          = np.array(decays_lepton_5_1e8_data[3])

Energy_quark_5_1e8       = np.array(decays_quark_5_1e8_data[1])
eta_quark_5_1e8          = np.array(decays_quark_5_1e8_data[2])
phi_quark_5_1e8          = np.array(decays_quark_5_1e8_data[3])

Energy_lepton_10_1e8       = np.array(decays_lepton_10_1e8_data[1])
eta_lepton_10_1e8          = np.array(decays_lepton_10_1e8_data[2])
phi_lepton_10_1e8          = np.array(decays_lepton_10_1e8_data[3])

Energy_quark_10_1e8       = np.array(decays_quark_10_1e8_data[1])
eta_quark_10_1e8          = np.array(decays_quark_10_1e8_data[2])
phi_quark_10_1e8          = np.array(decays_quark_10_1e8_data[3])



decays_5_1e9  = dat_dir+folder+"/decays_GRID-5-1e-09.dat"
decays_10_1e9 = dat_dir+folder+"/decays_GRID-10-1e-09.dat"

decays_5_1e9_data   = {0:[],1:[],2:[],3:[],4:[],5:[]}
decays_10_1e9_data  = {0:[],1:[],2:[],3:[],4:[],5:[]}

for line in open(decays_5_1e9,"r"):
  for i,C in enumerate(line.split()): decays_5_1e9_data[i].append(float(C))
for line in open(decays_10_1e9,"r"):
  for i,C in enumerate(line.split()): decays_10_1e9_data[i].append(float(C))
tau_5_1e9          = np.array(decays_5_1e9_data[0])/299.792 # in ns
ctau_5_1e9         = np.array(decays_5_1e9_data[0])# in mm
decayLenght_5_1e9  = np.array(decays_5_1e9_data[1])
Gamma_5_1e9        = np.array(decays_5_1e9_data[2])
#betaGamma_5_1e9   = np.array(decays_5_1e9_data/decays_5_1e9_data[0])## L/ctau
Energy_5_1e9       = np.array(decays_5_1e9_data[3])
eta_5_1e9          = np.array(decays_5_1e9_data[4])
phi_5_1e9          = np.array(decays_5_1e9_data[5])


tau_10_1e9          = np.array(decays_10_1e9_data[0])/299.792 # in ns
ctau_10_1e9         = np.array(decays_10_1e9_data[0])# in mm
decayLenght_10_1e9  = np.array(decays_10_1e9_data[1])
Gamma_10_1e9        = np.array(decays_10_1e9_data[2])
#betaGamma_10_1e9    = np.array(decays_10_1e9_data/decays_5_1e9_data[0])## L/ctau
Energy_10_1e9       = np.array(decays_10_1e9_data[3])
eta_10_1e9          = np.array(decays_10_1e9_data[4])
phi_10_1e9          = np.array(decays_10_1e9_data[5])


decays_lepton_5_1e9  = dat_dir+folder+"/decays_lepton_GRID-5-1e-09.dat"
decays_lepton_10_1e9 = dat_dir+folder+"/decays_lepton_GRID-10-1e-09.dat"

decays_quark_5_1e9  = dat_dir+folder+"/decays_quark_GRID-5-1e-09.dat"
decays_quark_10_1e9 = dat_dir+folder+"/decays_quark_GRID-10-1e-09.dat"


decays_lepton_5_1e9_data  = {0:[],1:[],2:[],3:[]}
decays_lepton_10_1e9_data = {0:[],1:[],2:[],3:[]}

decays_quark_5_1e9_data   = {0:[],1:[],2:[],3:[]}
decays_quark_10_1e9_data  = {0:[],1:[],2:[],3:[]}


for line in open(decays_lepton_5_1e9,"r"):
  for i,C in enumerate(line.split()): decays_lepton_5_1e9_data[i].append(float(C))
for line in open(decays_quark_10_1e9,"r"):
  for i,C in enumerate(line.split()): decays_quark_10_1e9_data[i].append(float(C))
for line in open(decays_lepton_10_1e9,"r"):
  for i,C in enumerate(line.split()): decays_lepton_10_1e9_data[i].append(float(C))
for line in open(decays_quark_5_1e9,"r"):
  for i,C in enumerate(line.split()): decays_quark_5_1e9_data[i].append(float(C))

Energy_lepton_5_1e9       = np.array(decays_lepton_5_1e9_data[1])
eta_lepton_5_1e9          = np.array(decays_lepton_5_1e9_data[2])
phi_lepton_5_1e9          = np.array(decays_lepton_5_1e9_data[3])

Energy_quark_5_1e9       = np.array(decays_quark_5_1e9_data[1])
eta_quark_5_1e9          = np.array(decays_quark_5_1e9_data[2])
phi_quark_5_1e9          = np.array(decays_quark_5_1e9_data[3])

Energy_lepton_10_1e9       = np.array(decays_lepton_10_1e9_data[1])
eta_lepton_10_1e9          = np.array(decays_lepton_10_1e9_data[2])
phi_lepton_10_1e9          = np.array(decays_lepton_10_1e9_data[3])

Energy_quark_10_1e9       = np.array(decays_quark_10_1e9_data[1])
eta_quark_10_1e9          = np.array(decays_quark_10_1e9_data[2])
phi_quark_10_1e9          = np.array(decays_quark_10_1e9_data[3])


#################
## Plotting Style
#################
rcParams['legend.loc'] = 'best'
#Direct input 
plt.rcParams['text.latex.preamble']=[r"\usepackage{lmodern}"]
#Options
params = {'text.usetex' : True,
          'font.size' : 10,
          'font.family' : 'lmodern',
          'legend.fontsize': 5
          }
plt.rcParams.update(params) 
####################################
# Color pallete
#import cmocean
#cm1=cmocean.cm.amp
#cm2=cmocean.cm.deep
####################################
#https://stackoverflow.com/questions/18764814/make-contour-of-scatter


ctau51e7=round(ctau_5_1e7[0]/1000.,3)
ctau101e7=round(ctau_10_1e7[0]/1000.,3)
ctau51e8=round(ctau_5_1e8[0]/1000.,3)
ctau101e8=round(ctau_10_1e8[0]/1000.,3)
ctau51e9=round(ctau_5_1e9[0]/1000.,3)
ctau101e9=round(ctau_10_1e9[0]/1000.,3)

fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(12, 8))

plt.subplot(3,6,1)
plt.title(title,fontsize=15)
#plt.hist(decayLenght_5_1e7/1000.,20,range=[0,10],color="red", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,density=True,label="$c\\tau N 5=$"+str(ctau51e7))
#plt.hist(decayLenght_10_1e7/1000.,20,range=[0,10],color="black", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,density=True,label="$c\\tau N 10=$"+str(ctau101e7))
plt.hist(decayLenght_5_1e7/1000.,20,range=[0,10],color="red", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$c\\tau N 5=$"+str(ctau51e7))
plt.hist(decayLenght_10_1e7/1000.,20,range=[0,10],color="black", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$c\\tau N 10=$"+str(ctau101e7))
plt.legend()
plt.xlabel('decay length [m]',fontsize=8)
plt.subplot(3,6,2)
plt.hist(Gamma_5_1e7,20,range=[0,40],color="red", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Gamma_10_1e7,20,range=[0,40],color="black", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$\\gamma$ ',fontsize=8)
plt.subplot(3,6,3)
plt.hist(eta_5_1e7,20,range=[0,10],color="red", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(eta_10_1e7,20,range=[0,10],color="black", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$|\\eta_{N}|$ ',fontsize=8)
plt.subplot(3,6,4)
plt.title("$|V_{lN}|^{2}=10^{-7}$ GeV",fontsize=10)
plt.hist(Energy_5_1e7,20,range=[0,500],color="red", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_10_1e7,20,range=[0,500],color="black", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$E_{N}$ [GeV] ',fontsize=8)
plt.subplot(3,6,5)
plt.hist(Energy_lepton_5_1e7,20,range=[0,250],color="red", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_lepton_10_1e7,20,range=[0,250],color="black", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('lepton $E$ from $N$ [GeV] ',fontsize=8)
plt.subplot(3,6,6)
plt.hist(Energy_quark_5_1e7,20,range=[0,250],color="red", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_quark_10_1e7,20,range=[0,250],color="black", alpha=0.3, histtype="stepfilled",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('quark $E$ from $N$ [GeV] ',fontsize=8)
plt.subplot(3,6,7)
plt.hist(decayLenght_5_1e8/1000.,20,range=[0,100],color="red", alpha=0.3, histtype="bar",zorder=0.,rasterized=True,label="$c\\tau N 5=$"+str(ctau51e8))
plt.hist(decayLenght_10_1e8/1000.,20,range=[0,100],color="black", alpha=0.3, histtype="bar",zorder=0.,rasterized=True,label="$c\\tau N 10=$"+str(ctau101e8))
plt.legend()
plt.xlabel('decay length [m]',fontsize=8)
plt.subplot(3,6,8)
plt.hist(Gamma_5_1e8,20,range=[0,40],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Gamma_10_1e8,20,range=[0,40],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$\\gamma$ ',fontsize=8)
plt.subplot(3,6,9)
plt.hist(eta_5_1e8,20,range=[0,10],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(eta_10_1e8,20,range=[0,10],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$|\\eta_{N}|$ ',fontsize=8)
plt.subplot(3,6,10)
plt.title("$|V_{lN}|^{2}=10^{-8}$ GeV",fontsize=10 )
plt.hist(Energy_5_1e8,20,range=[0,500],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_10_1e8,20,range=[0,500],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$E_{N}$ [GeV] ',fontsize=8)
plt.subplot(3,6,11)
plt.hist(Energy_lepton_5_1e8,20,range=[0,250],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_lepton_10_1e8,20,range=[0,250],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('lepton $E$ from $N$ [GeV] ',fontsize=8)
plt.subplot(3,6,12)
plt.hist(Energy_quark_5_1e8,20,range=[0,250],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_quark_10_1e8,20,range=[0,250],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('quark $E$ from $N$ [GeV] ',fontsize=8)
plt.subplot(3,6,13)
plt.hist(decayLenght_5_1e9/1000.,20,range=[0,100],color="red", alpha=0.3, histtype="bar",zorder=0.,rasterized=True,label="$c\\tau N 5=$"+str(ctau51e9))
plt.hist(decayLenght_10_1e9/1000.,20,range=[0,100],color="black", alpha=0.3, histtype="bar",zorder=0.,rasterized=True,label="$c\\tau N 10=$"+str(ctau101e9))
plt.legend()
plt.xlabel('decay length [m]',fontsize=8)
plt.subplot(3,6,14)
plt.hist(Gamma_5_1e9,20,range=[0,40],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Gamma_10_1e9,20,range=[0,40],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$\\gamma$ ',fontsize=8)
plt.subplot(3,6,15)
plt.hist(eta_5_1e9,20,range=[0,10],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(eta_10_1e9,20,range=[0,10],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$|\\eta_{N}|$ ',fontsize=8)
plt.subplot(3,6,16)
plt.title("$|V_{lN}|^{2}=10^{-9}$ GeV",fontsize=10 )
plt.hist(Energy_5_1e9,20,range=[0,500],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_10_1e9,20,range=[0,500],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('$E_{N}$ [GeV] ',fontsize=8)
plt.subplot(3,6,17)
plt.hist(Energy_lepton_5_1e9,20,range=[0,250],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_lepton_10_1e9,20,range=[0,250],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('lepton $E$ from $N$ [GeV] ',fontsize=8)
plt.subplot(3,6,18)
plt.hist(Energy_quark_5_1e9,20,range=[0,250],color="red", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=5$ GeV")
plt.hist(Energy_quark_10_1e9,20,range=[0,250],color="black", alpha=0.3, histtype="barstacked",zorder=0.,rasterized=True,label="$m_{N}=10$ GeV")
plt.legend()
plt.xlabel('quark $E$ from $N$ [GeV] ',fontsize=8)
plt.tight_layout()
plt.show()
plt.savefig(folder+'.pdf', bbox_inches='tight')
####################################
###################################
