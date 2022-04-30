# generate events with eta cut for event generation, not process generation

import os,sys
import numpy as np
import math




mN = np.arange(0,6,0.1)
Vlnu2 = np.array([1e-7, 2e-7,3e-7,4e-7,5e-7,6e-7,7e-7,8e-7,9e-7,\
1e-6, 2e-6,3e-6,4e-6,5e-6,6e-6,7e-6,8e-6,9e-6,\
1e-5, 2e-7,3e-5,4e-5,5e-5,6e-5,7e-5,8e-5,9e-5,\
1e-4, 2e-7,3e-4,4e-4,5e-4,6e-4,7e-4,8e-4,9e-4,\
1e-3, 2e-7,3e-3,4e-3,5e-3,6e-3,7e-3,8e-3,9e-3,\
1e-2, 2e-7,3e-2,4e-2,5e-2,6e-2,7e-2,8e-2,9e-2,\
1e-1, 2e-7,3e-1,4e-1,5e-1,6e-1,7e-1,8e-1,9e-1, 1.638e-06])
### for Christina's macbook pro
#madgraph_path = '/Users/christinawang/programs/MG5_aMC_v2_8_1'
#card_dir = '/Users/christinawang/Desktop/Caltech/Research/LLP/HNL/cards/'
#output_dir = '/Users/christinawang/Desktop/Caltech/Research/LLP/HNL/mg5_grid_1j/'

### for login node
madgraph_path = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/MG5_aMC_v2_9_3/'
card_dir = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/cards/'
output_dir='/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid_2j_etacut/'
if not os.path.isdir(output_dir):os.makedirs(output_dir)
if not os.path.isdir(output_dir+'HNL_mg5_GRID_e_generate'):os.makedirs(output_dir+'HNL_mg5_GRID_e_generate')
if not os.path.isdir(output_dir+'HNL_mg5_GRID_mu_generate'):os.makedirs(output_dir+'HNL_mg5_GRID_mu_generate')
if not os.path.isdir(output_dir+'HNL_mg5_GRID_tau_generate'):os.makedirs(output_dir+'HNL_mg5_GRID_tau_generate')
run_card = 'run_card_HNL.dat'
#Mixing in electron sector
for mass in mN:
    for mix2 in Vlnu2:
        sqmix2 = np.sqrt(float(mix2))
        if mass >= 1 and int(mass)==mass:mass = int(mass)	
        f = open(output_dir+"HNL_mg5_GRID_e_generate/HNL_mg5_GRID_e-"+str(mass)+"-"+str(mix2),'w')
        #f.write("launch -i "+output_dir+"HNL_GRID_e/HNL_GRID_e-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("launch -i\n")
        f.write("generate_events\n")
        f.write(card_dir+"/param_card_HNL.dat\n")
        f.write(card_dir+run_card+"\n")
        f.write("set numixing 1 "+str(sqmix2)+"\n")
        f.write("set numixing 5 0\n")
        f.write("set numixing 9 0\n")
	f.write("set nevents 100000 \n")
        f.write("set MASS 9900012 "+str(mass)+"\n")
        f.write("set MASS 9900014 1.000000e+03\n") #decouple other N
        f.write("set MASS 9900016 1.000000e+03\n")
        f.write("set DECAY 9900012 Auto\n")
        f.write("set cut_decays True \n")
        f.write("set eta_min_pdg 9900012 0.5 \n")
        f.write("set eta_max_pdg 9900012 3 \n")
	f.close()
#Mixing in muon sector
for mass in mN:
    for mix2 in Vlnu2:
        sqmix2 = np.sqrt(mix2)
        if mass >= 1 and int(mass)==mass:mass = int(mass)
	f = open(output_dir+"HNL_mg5_GRID_mu_generate/HNL_mg5_GRID_mu-"+str(mass)+"-"+str(mix2),'w')
        #f.write("launch -i "+output_dir+"HNL_GRID_mu/HNL_GRID_mu-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("launch -i\n")
        f.write("generate_events\n")
        f.write(card_dir+"/param_card_HNL.dat\n")
        f.write(card_dir+run_card+"\n")
        f.write("set numixing 1 0\n")
        f.write("set numixing 5 "+str(sqmix2)+"\n")
        f.write("set numixing 9 0\n")
	f.write("set nevents 100000 \n")
        f.write("set MASS 9900012 1.000000e+03\n")
        f.write("set MASS 9900014 "+str(mass)+"\n") 
        f.write("set MASS 9900016 1.000000e+03\n")
        f.write("set DECAY 9900014 Auto\n")
        f.write("set cut_decays True \n")
        f.write("set eta_min_pdg 9900014 0.5 \n")
        f.write("set eta_max_pdg 9900014 3 \n")
	f.close()
#Mixing in tau sector
for mass in mN:
    for mix2 in Vlnu2:
        sqmix2 = np.sqrt(mix2)
        if mass >= 1 and int(mass)==mass:mass = int(mass)
	f = open(output_dir+"HNL_mg5_GRID_tau_generate/HNL_mg5_GRID_tau-"+str(mass)+"-"+str(mix2),'w')
        #f.write("launch -i "+output_dir+"HNL_GRID_tau/HNL_GRID_tau-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("launch -i\n")
        f.write("generate_events\n")
        f.write(card_dir+"/param_card_HNL.dat\n")
        f.write(card_dir+run_card+"\n")
        f.write("set numixing 1 0\n")
        f.write("set numixing 5 0\n")
        f.write("set numixing 9 "+str(sqmix2)+"\n")
	f.write("set nevents 100000 \n")
        f.write("set MASS 9900012 1.000000e+03\n")
        f.write("set MASS 9900014 1.000000e+03\n") 
        f.write("set MASS 9900016 "+str(mass)+"\n")
        f.write("set DECAY 9900016 Auto\n")
	f.write("set cut_decays True \n")
        f.write("set eta_min_pdg 9900016 0.5 \n")
        f.write("set eta_max_pdg 9900016 3 \n")
	f.close()

