import os
import subprocess
from subprocess import call

decay="tau"
text_dir="/Users/christinawang/Desktop/Caltech/Research/LLP/HNL/mg5_grid_1j/pythia_cmd_grid_"+decay+"/"
output_dir="/Users/christinawang/Desktop/Caltech/Research/LLP/HNL/mg5_grid_1j/Delphes_output_"+decay+"/"
delphes_dir="/Users/christinawang/programs/Delphes-3.4.2/"
if not os.path.isdir(output_dir):os.makedirs(output_dir)
coupling = {}
#coupling[0.1] = [0.1, 0.01,0.001,0.0001,8e-05,6e-05,4e-05,2e-05]
#coupling[0.5] = [0.1, 0.01,0.001,0.0001,8e-05,6e-05,4e-05,2e-05]
coupling[1] = [0.1, 0.01,0.001,0.0001,8e-05,6e-05,4e-05,2e-05]
#coupling[2] = [8e-05,6e-05,4e-05,2e-05,1e-06,1e-07]
#coupling[4] = [1e-06,8e-06,6e-06,4e-06,2e-06,1e-05,1e-07,8e-07,6e-07,4e-07,2e-07]
#coupling[5] =[1.00E-05,8.00E-06,6.00E-06,4.00E-06,2.00E-06,1.00E-06,1.00E-07,1.00E-08, 1.00E-09]

f = open('delphes_cmd','w')
for m, v in coupling.items():
	for c in v:
		executable = delphes_dir + "DelphesPythia8"
		card = delphes_dir+"/cards/delphes_card_CMS_CSCCluster.tcl"
		pythia_cmd = text_dir + "/configLHE_" + decay + "-" + str(m) + "-" + str(c) + ".cmnd"
		output = output_dir + "/delphes_" + decay + "-" + str(m) + "-" + str(c) + ".root"
		# if os.path.isfile(output): os.system("rm " + output)
		f.write("echo "+ str(m) + " " + str(c)+"\n")
		f.write('rm -rf '+output + '\n')
		f.write(executable + " " + card + " " + pythia_cmd + " " + output+'\n')
		# os.system(executable + " " + card + " " + pythia_cmd + " " + output)
		# print os.getenv("DYLD_LIBRARY_PATH")
f.close()
