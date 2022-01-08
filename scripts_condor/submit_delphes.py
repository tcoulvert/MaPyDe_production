import os
coupling = {}
coupling[1] = [0.01, 0.001, 0.0001, 1e-05]
coupling[2] = [0.01, 0.001, 0.0001, 1e-05]
coupling[3] = [0.01, 0.001, 0.0001, 1e-05]
coupling[4] = [0.01, 0.001, 0.0001, 1e-05]

config_card = 'cards/delphes_card_CMS_CSCCluster_hnl_PileUp.tcl' #path relative to Delphes directory
outputDir = "/storage/af/user/christiw/delphes_output/v1/hnl/"
nJobs = 20
for decay in ['e', 'mu', 'tau']:
    for m, v in coupling.items():
            for c in v:
                if not decay == 'e': continue
                print(m,c)

		os.system("rm -rf log/HNL-delphes*")
		os.system("rm -rf submit/HNL-delphes*")

		# lhe_file = "/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid/HNL_GRID_{}/HNL_GRID_{}-{}-{}/Events/run_01/unweighted_events.lhe.gz".format(decay,decay,m, c)
		lhe_file = "/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid/HNL_GRID_{}/HNL_GRID_{}-{}-{}/Events/run_01/".format(decay,decay,m, c)
                file_name = 'submit/delphesPythia_m'+str(m)+'v'+str(c)+'.jdl'
                f = open(file_name, "w")
        	f.write("Universe = vanilla \n")
        	f.write("Executable = runDelphesPythia8.sh \n")
        	f.write("Arguments = {} {} {} {} \$(ProcId) {} {} {}/ {}/ \n".format(decay, m, c, lhe_file, config_card, outputDir, os.getenv('CMSSW_BASE'), os.getenv('HOME')))


        	f.write("Log = log/HNL-delphes-{}_{}_{}_PC.log \n".format(decay, m, c))
        	f.write("Output = log/HNL-delphes-{}_{}_{}.out \n".format(decay, m, c))
        	f.write("Error = log/HNL-delphes-{}_{}_{}.err \n".format(decay, m, c))

        	#f.write("Requirements=TARGET.OpSysAndVer==\"CentOS7\"")
        	f.write("Requirements=(TARGET.OpSysAndVer==\"CentOS7\" && regexp(\"blade.*\", TARGET.Machine)) \n")

        	f.write("RequestMemory = 2000 \n")
        	f.write("RequestCpus = 1 \n")
        	f.write("RequestDisk = 4 \n")
            	f.write("+JobQueue=\"Short\" \n")

        	f.write("+RunAsOwner = True \n")
        	f.write("+InteractiveUser = true \n")
        	#f.write("+SingularityImage = \"/cvmfs/singularity.opensciencegrid.org/bbockelm/cms:rhel7\"")
        	f.write("+SingularityImage = \"/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7\" \n")
        	f.write('+SingularityBindCVMFS = True \n')
        	f.write("run_as_owner = True \n")
        	f.write("x509userproxy = {}/x509_proxy \n".format(os.getenv('HOME')))
        	f.write("should_transfer_files = YES \n")
        	f.write("when_to_transfer_output = ON_EXIT \n")
        	f.write("Queue {} \n".format(nJobs))
        	print("condor_submit {} \n".format(file_name))
                f.close()

        	os.system("condor_submit {} --batch-name HNL-{}-{}-{}".format(file_name, decay, m, c))
