import os,sys
import numpy as np
import math

coupling = {}
coupling[1] = [0.1, 0.01,0.001,0.0001,8e-05,6e-05,4e-05,2e-05]
coupling[2] = [8e-05,6e-05,4e-05,2e-05,1e-06,1e-07]
coupling[4] = [1e-06,8e-06,6e-06,4e-06,2e-06,1e-05,1e-07,8e-07,6e-07,4e-07,2e-07]
coupling[5] =[1.00E-05,8.00E-06,6.00E-06,4.00E-06,2.00E-06,1.00E-06,1.00E-07,1.00E-08, 1.00E-09]

runNum = "01"
decay_mode = ['e', 'mu', 'tau']
lhe_file_dir = '/Users/christinawang/Desktop/Caltech/Research/LLP/HNL/mg5_grid_1j/'
output_dir = lhe_file_dir+'pythia_cmd_grid_' #pythia command output dir
if not os.path.isdir(output_dir+'e'):os.makedirs(output_dir+'e/')
if not os.path.isdir(output_dir+'mu'):os.makedirs(output_dir+'mu/')
if not os.path.isdir(output_dir+'tau'):os.makedirs(output_dir+'tau/')

for lep in decay_mode:
    for mass, v in coupling.items():
        for mix2 in v:
			f = open(output_dir+lep+"/configLHE_"+lep+"-"+str(mass)+"-"+str(mix2)+".cmnd",'w')
			f.write("Main:numberOfEvents = 20000\n")  
			f.write("Main:timesAllowErrors = 50\n")       
			f.write("Init:showChangedSettings = on\n")    
			f.write("Init:showChangedParticleData = off\n") 
			f.write("Next:numberCount = 1000\n")        
			f.write("Next:numberShowInfo = 1\n")           
			f.write("Next:numberShowProcess = 1\n")   
			f.write("Next:numberShowEvent = 0\n")      
			f.write("Beams:frameType = 4\n")
			f.write("Beams:LHEF = "+lhe_file_dir+"HNL_GRID_"+lep+"/HNL_GRID_"+lep+"-"+str(mass)+"-"+str(mix2)+"/Events/run_"+runNum+"/unweighted_events.lhe.gz\n")
			f.write("Beams:idA = 2212\n")              
			f.write("Beams:idB = 2212\n")            
			f.write("Beams:eCM = 13000.\n")          
                        f.write("JetMatching:setMad = off\n")
                        f.write("JetMatching:scheme = 1\n")
                        f.write("JetMatching:merge = on\n")
                        f.write("JetMatching:jetAlgorithm = 2\n")
                        f.write("JetMatching:etaJetMax = 5.\n")
                        f.write("JetMatching:coneRadius = 1.\n")
                        f.write("JetMatching:slowJetPower = 1\n")
                        f.write("JetMatching:qCut = 19.\n") #this is the actual merging scale
                        f.write("JetMatching:nQmatch = 5\n") #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
                        f.write("JetMatching:nJetMax = 4\n") #number of partons in born matrix element for highest multiplicity
                        f.write("JetMatching:doShowerKt = off\n") #off for MLM matching, turn on for shower-kT matching
