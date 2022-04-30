# Written by Giovanna Cottin (gfcottin@gmail.com)
import os,sys
import numpy as np
import math



mN    = np.array([0.1, 0.5,1,2,3, 4,4.5, 5, 6,7, 8,5,10,15,20,2.1, 2.2, 2.3, 2.5,3.2,3.5, 3.8, 3.9, 3.6, 3.7, 4.1,4.2,4.5,5.5, 3.55, 4.6, 4.7, 3.3, 3.4, 3.1, 3.05, 2.8, 5.3, 5.4, 5.32, 5.35, 5.38, 1.5, 2.4, 3.3, 3.4])
Vlnu2 = np.array([0.02,0.04, 1e-09,1e-08,6e-07,4e-07,2e-07,1e-07,9e-6, 8e-06,7e-6, 6e-06,5e-6, 4e-06,3e-6,2e-06,1e-06,9e-05,8e-05,7e-5,6e-05,4e-05,3e-05, 2e-05,1e-05,1e-04, 0.0002,0.0003,0.0004,0.0006, 0.0007, 0.0008, 0.0009,1e-03, 0.002,0.003,0.004,1e-02,0.1,0.5,0.8,0.05,0.005,0.0005,5e-5, 1e-4, 5e-5, 1e-5, 5e-6, 1e-6, 5e-7, 1e-7, 8e-7, 6e-7, 7e-7,9e-7,2e-6, 3e-6, 4e-6])



### for login node
madgraph_path = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/MG5_aMC_v2_9_3/'
card_dir = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/cards/'
output_dir='/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid_2j_nocut/'
if not os.path.isdir(output_dir+'HNL_mg5_GRID_e'):os.makedirs(output_dir+'HNL_mg5_GRID_e')
if not os.path.isdir(output_dir+'HNL_mg5_GRID_mu'):os.makedirs(output_dir+'HNL_mg5_GRID_mu')
if not os.path.isdir(output_dir+'HNL_mg5_GRID_tau'):os.makedirs(output_dir+'HNL_mg5_GRID_tau')

#Mixing in electron sector
for mass in mN:
    for mix2 in Vlnu2:
	print(mass, mix2)
        sqmix2 = np.sqrt(float(mix2))
	if mass >= 1 and int(mass)==mass:mass = int(mass)
        print(output_dir+"HNL_mg5_GRID_e/HNL_mg5_GRID_e-"+str(mass)+"-"+str(mix2))
	f = open(output_dir+"HNL_mg5_GRID_e/HNL_mg5_GRID_e-"+str(mass)+"-"+str(mix2),'w')
        f.write("import model SM_HeavyN_Gen3Mass_NLO\n")
        f.write("define w= w+ w-\n")
        f.write("define e= e+ e-\n")
	f.write("define j = g u c d s u~ c~ d~ s~\n")
	f.write("generate p p > w, (w > e n1)\n")
	f.write("add process p p > w j, (w > e n1)\n")
	f.write("add process p p > w j j, (w > e n1)\n")
	f.write("output "+output_dir+"HNL_GRID_e/HNL_GRID_e-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("launch -i "+output_dir+"HNL_GRID_e/HNL_GRID_e-"+str(mass)+"-"+str(mix2)+"\n")
        f.write("generate_events\n")
        f.write(card_dir+"/param_card_HNL.dat\n")
        f.write(card_dir+"/run_card_HNL.dat\n")
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
        if mass >= 1 and int(mass)==mass:mass = int(mass)
	sqmix2 = np.sqrt(mix2)
        f = open(output_dir+"HNL_mg5_GRID_mu/HNL_mg5_GRID_mu-"+str(mass)+"-"+str(mix2),'w')
        f.write("import model SM_HeavyN_Gen3Mass_NLO\n")
        f.write("define w= w+ w-\n")
        f.write("define mu= mu+ mu-\n")
        f.write("generate p p > w, (w > mu n2)\n")
        f.write("add process p p > w j, (w > mu n2)\n")
        f.write("add process p p > w j j, (w > mu n2)\n")
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
        if mass >= 1 and int(mass)==mass:mass = int(mass)
        f = open(output_dir+"HNL_mg5_GRID_tau/HNL_mg5_GRID_tau-"+str(mass)+"-"+str(mix2),'w')
        f.write("import model SM_HeavyN_Gen3Mass_NLO\n")
        f.write("define w= w+ w-\n")
        f.write("define tau= ta+ ta-\n")
        f.write("define j = g u c d s u~ c~ d~ s~\n")
        f.write("generate p p > w, (w > tau n3)\n")
        f.write("add process p p > w j, (w > tau n3)\n")
        f.write("add process p p > w j j, (w > tau n3)\n")
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

