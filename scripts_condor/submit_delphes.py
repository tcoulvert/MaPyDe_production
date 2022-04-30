'''
    Author: Christina Wang
    Date last modified: 4/30/2022
    Script to submit DelphesPythia8 on condor for HNL signal
'''

import os
import numpy as np
coupling = {}



coupling[1] = np.array([0.01, 0.005, 0.001,0.0005,0.0001,5e-05, 1e-05])
coupling[1.5] = np.array([5e-4, 7e-4, 1e-3, 3e-3, 0.002, 0.005, 0.008, 0.01, 0.02, 0.05])
coupling[2] = np.array([0.01, 0.005, 0.001, 0.0005,0.0001,5e-05,1e-05])
coupling[2.1] = np.array([  4e-4, 6e-4,1e-3, 0.005,0.01, 0.02, 0.04])
coupling[2.5] = np.array([ 0.005, 0.003,0.001, 0.0005, 0.0001,5e-05,1e-05,1e-6,  ])
coupling[3] = np.array([0.01, 0.005,0.0005, 0.0001,5e-05, 1e-05,5e-6, 1e-6, 1e-3])
coupling[3.5] = np.array([0.01, 0.001, 0.0005, 0.0001,5e-05,1e-05,1e-6])
coupling[4] = np.array([0.01, 0.001, 0.0005,0.0001, 5e-05, 1e-05, 5e-6, 1e-6])
coupling[4.5] = np.array([1e-6, 5e-6,1e-5, 5e-5, 1e-4])
coupling[5] = np.array([1e-6, 5e-6, 1e-5,5e-5, 1e-4])


config_card = 'cards/delphes_card_CMS_CSCCluster_hnl_PileUp.tcl'
input_lhe_path = "/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid_2j/"
output_delphes_path = "/storage/af/user/christiw/delphes_output/v15/hnl/"

#no cut
#coupling[1] = np.array([1e-5, 5e-5, 0.0001, 0.0005, 0.001])
#coupling[1.5]  = np.array([0.0007, 0.001, 0.005,0.01,0.02])
#coupling[2] = np.array([1e-6, 5e-6, 1e-5, 5e-5, 0.0001, 0.0005, 0.001, 0.01, 0.05,])
#coupling[2.5] = np.array([1e-6, 5e-6, 1e-5, 5e-5, 1e-4, 5e-4, 1e-3, ])
#coupling[3] = np.array([0.0001, 0.001, 0.005, 0.01, 1e-5, 1e-6, 5e-5, 5e-6, ])
#coupling[3.5] = np.array([0.0001, 0.0005, 0.001, 0.005, 0.01, 1e-5, 1e-6, 5e-6, 1e-7])
#coupling[4] = np.array([0.0001, 0.0005, 0.001, 1e-5, 1e-6, 1e-7, ])
#coupling[4.5] = np.array([0.0001, 0.0005, 0.001, 1e-5, 1e-6, 1e-7,])
#coupling[5] = np.array([0.0001, 1e-5, 1e-6, 1e-7, 5e-5, 5e-6, 5e-7])
#config_card = 'cards/delphes_card_CMS_CSCCluster_hnl_PileUp.tcl'
#input_lhe_path = "/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid_2j_etacut/"
#output_delphes_path = "/storage/af/user/christiw/delphes_output/v15/hnl_etacut/"
nJobs = 100
maxNEvents = 1000
for decay in ['e', 'mu', 'tau']:
    for m, v in coupling.items():
            for c in v:
                if not decay == 'e': continue
                for i_run in range(1):
			run = 'run'+str(i_run)
			run = 'run_01'
			print(m,c)
			os.system("rm -rf log/HNL-delphes-{}-{}-{}-{}*".format(run, decay, m, c))
			os.system("rm -rf submit/delphes-{}-{}-{}-{}*".format(run, decay, m, c))

			lhe_file = "{}/HNL_GRID_{}/HNL_GRID_{}-{}-{}/Events/{}/".format(input_lhe_path, decay,decay,m, c, run)

                	file_name = 'submit/delphes-'+run+'_m'+str(m)+'v'+str(c)+'.jdl'
                	f = open(file_name, "w")
        		f.write("Universe = vanilla \n")
        		f.write("Executable = runDelphesPythia8.sh \n")
			#outputDir = '/storage/af/user/christiw/delphes_output/v11/hnl/{}/'.format(run)+decay+'/grid-{}-{}-{}/'.format(decay,m,c)
			outputDir = '{}/{}/'.format(output_delphes_path, run)+decay+'/grid-{}-{}-{}/'.format(decay,m,c)

			print(outputDir)
        		f.write("Arguments = {} {} {} {} $(ProcId) {} {} {} {}/ {}/ \n".format(decay, m, c, lhe_file, maxNEvents, config_card, outputDir, os.getenv('CMSSW_BASE'), os.getenv('HOME')))

        		f.write("Log = log/HNL-delphes-{}-{}_{}_{}_$(ProcId)_PC.log \n".format(run, decay, m, c))
        		f.write("Output = log/HNL-delphes-{}-{}_{}_{}_$(ProcId).out \n".format(run, decay, m, c))
        		f.write("Error = log/HNL-delphes-{}-{}_{}_{}_$(ProcId).err \n".format(run, decay, m, c))


        		f.write("RequestMemory = 2000 \n")
        		f.write("RequestCpus = 1 \n")
        		f.write("RequestDisk = 4 \n")
            		f.write("+JobQueue=\"Short\" \n")

        		f.write("+RunAsOwner = True \n")
        		f.write("+InteractiveUser = true \n")
        		f.write("+SingularityImage = \"/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7\" \n")
        		f.write('+SingularityBindCVMFS = True \n')
        		f.write("run_as_owner = True \n")
        		f.write("x509userproxy = {}/x509_proxy \n".format(os.getenv('HOME')))
        		f.write("should_transfer_files = YES \n")
        		f.write("when_to_transfer_output = ON_EXIT \n")
        		f.write("Queue {} \n".format(nJobs))
        		print("condor_submit {} \n".format(file_name))
                	f.close()
        		os.system("condor_submit {} --batch-name HNL-delphes-{}-{}-{}".format(file_name, decay, m, c))
