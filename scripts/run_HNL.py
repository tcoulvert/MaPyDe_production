import os

#text_dir="/Users/christinawang/Desktop/Caltech/Research/LLP/HNL/mg5_grid_1j/"
#mg5_dir = "/Users/christinawang/programs/MG5_aMC_v2_8_1/bin/mg5_aMC"
text_dir="/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid/"
mg5_dir="/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/MG5_aMC_v2_9_3/bin/mg5_aMC"
decay="e"
coupling = {}
#coupling[0.1] = [0.1, 0.01,0.001,0.0001,8e-05,6e-05,4e-05,2e-05,0.5,0.8]
#coupling[0.5] = [0.1, 0.01,0.001,0.0001,8e-05,6e-05,4e-05,2e-05]
coupling[1] = [0.1, 0.01,0.001,0.0001,8e-05,6e-05,4e-05,2e-05]
coupling[2] = [8e-05,6e-05,4e-05,2e-05,1e-06,1e-07]
coupling[4] = [1e-06,8e-06,6e-06,4e-06,2e-06,1e-05,1e-07,8e-07,6e-07,4e-07,2e-07]
coupling[5] =[1.00E-05,8.00E-06,6.00E-06,4.00E-06,2.00E-06,1.00E-06,1.00E-07,1.00E-08, 1.00E-09]
for m, v in coupling.items():
	for c in v:
		print(m,c)
		output = text_dir + "HNL_mg5_GRID_" + decay+"/HNL_mg5_GRID_"+decay+"-"+str(m)+"-"+str(c)
		print(mg5_dir + " " + output)
		#os.system(mg5_dir + " " + output)
