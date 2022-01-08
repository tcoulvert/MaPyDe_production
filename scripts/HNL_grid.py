# Written by Giovanna Cottin (gfcottin@gmail.com)
import os,sys
import numpy as np
import math

mN    = np.array([0.1, 0.5,1,2,3, 4,5, 6,8,5,10,15,20])
Vlnu2 = np.array([1e-09,1e-08,6e-07,4e-07,2e-07,1e-07,8e-06,6e-06,4e-06,2e-06,1e-06,8e-05,6e-05,4e-05,2e-05,1e-05,1e-04, 1e-03, 1e-02,0.1,0.5,0.8])
### for Christina's macbook pro
#madgraph_path = '/Users/christinawang/programs/MG5_aMC_v2_8_1'
#card_dir = '/Users/christinawang/Desktop/Caltech/Research/LLP/HNL/cards/'
#output_dir = '/Users/christinawang/Desktop/Caltech/Research/LLP/HNL/mg5_grid_1j/'

### for login node
madgraph_path = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/MG5_aMC_v2_9_3/'
card_dir = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/cards/'
output_dir='/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid/'
if not os.path.isdir(output_dir+'HNL_mg5_GRID_e'):os.makedirs(output_dir+'HNL_mg5_GRID_e')
if not os.path.isdir(output_dir+'HNL_mg5_GRID_mu'):os.makedirs(output_dir+'HNL_mg5_GRID_mu')
if not os.path.isdir(output_dir+'HNL_mg5_GRID_tau'):os.makedirs(output_dir+'HNL_mg5_GRID_tau')

#Mixing in electron sector
for mass in mN:
    for mix2 in Vlnu2:
        sqmix2 = np.sqrt(float(mix2))
	if mass >= 1: mass = int(mass)
        f = open(output_dir+"HNL_mg5_GRID_e/HNL_mg5_GRID_e-"+str(mass)+"-"+str(mix2),'w')
        f.write("import model SM_HeavyN_Gen3Mass_NLO\n")
        f.write("define w= w+ w-\n")
        f.write("define e= e+ e-\n")
        #f.write("generate p p > w, (w > e n1)\n") #on shell
        #f.write("generate p p > w+ > e n1\n") #off shell
        #f.write("add process p p > w- > e n1\n")
	f.write("define j = g u c d s u~ c~ d~ s~\n")
	f.write("generate p p > w, (w > e n1)\n")
	f.write("add process p p > w j, (w > e n1)\n")
	f.write("output "+output_dir+"HNL_GRID_e/HNL_GRID_e-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("launch -i "+output_dir+"HNL_GRID_e/HNL_GRID_e-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("generate_events\n")
        f.write(card_dir+"/param_card_HNL.dat\n")
        f.write(card_dir+"/run_card_HNL.dat\n")
        ##f.write("set time_of_flight 1e-25\n") ## get displaced neutrinos/set in run_card
        f.write("set numixing 1 "+str(sqmix2)+"\n")
        f.write("set numixing 5 0\n")
        f.write("set numixing 9 0\n")
        f.write("set MASS 9900012 "+str(mass)+"\n")
        f.write("set MASS 9900014 1.000000e+03\n") #decouple other N
        f.write("set MASS 9900016 1.000000e+03\n")
        f.write("set DECAY 9900012 Auto\n")
        f.close()
#Mixing in muon sector
for mass in mN:
    for mix2 in Vlnu2:
        sqmix2 = np.sqrt(mix2)
        f = open(output_dir+"HNL_mg5_GRID_mu/HNL_mg5_GRID_mu-"+str(mass)+"-"+str(mix2),'w')
        f.write("import model SM_HeavyN_Gen3Mass_NLO\n")
        f.write("define w= w+ w-\n")
        f.write("define mu= mu+ mu-\n")
        f.write("generate p p > w, (w > mu n2)\n")
        f.write("add process p p > w j, (w > mu n2)\n")
	f.write("output "+output_dir+"HNL_GRID_mu/HNL_GRID_mu-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("launch -i "+output_dir+"HNL_GRID_mu/HNL_GRID_mu-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("generate_events\n")
        f.write(card_dir+"/param_card_HNL.dat\n")
        f.write(card_dir+"/run_card_HNL.dat\n")
        f.write("set numixing 1 0\n")
        f.write("set numixing 5 "+str(sqmix2)+"\n")
        f.write("set numixing 9 0\n")
        f.write("set MASS 9900012 1.000000e+03\n")
        f.write("set MASS 9900014 "+str(mass)+"\n") 
        f.write("set MASS 9900016 1.000000e+03\n")
        f.write("set DECAY 9900014 Auto\n")
        f.close()
#Mixing in tau sector
for mass in mN:
    for mix2 in Vlnu2:
        sqmix2 = np.sqrt(mix2)
        if mass >= 1: mass = int(mass)
        f = open(output_dir+"HNL_mg5_GRID_tau/HNL_mg5_GRID_tau-"+str(mass)+"-"+str(mix2),'w')
        f.write("import model SM_HeavyN_Gen3Mass_NLO\n")
        f.write("define w= w+ w-\n")
        f.write("define tau= ta+ ta-\n")
        f.write("define j = g u c d s u~ c~ d~ s~\n")
        f.write("generate p p > w, (w > tau n3)\n")
        f.write("add process p p > w j, (w > tau n3)\n")
        f.write("output "+output_dir+"HNL_GRID_tau/HNL_GRID_tau-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("launch -i "+output_dir+"HNL_GRID_tau/HNL_GRID_tau-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("generate_events\n")
        f.write(card_dir+"/param_card_HNL.dat\n")
        f.write(card_dir+"/run_card_HNL.dat\n")
        f.write("set numixing 1 0\n")
        f.write("set numixing 5 0\n")
        f.write("set numixing 9 "+str(sqmix2)+"\n")
        f.write("set MASS 9900012 1.000000e+03\n")
        f.write("set MASS 9900014 1.000000e+03\n") 
        f.write("set MASS 9900016 "+str(mass)+"\n")
        f.write("set DECAY 9900016 Auto\n")
        f.close()

