import os
text_dir="/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid/"
mg5_dir="/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/MG5_aMC_v2_9_3/bin/mg5_aMC"
decay="e"
coupling = {}
coupling[1] = [1e-02, 1e-03, 1e-04, 1e-05]
coupling[2] = [1e-02, 1e-03, 1e-04, 1e-05]
coupling[3] = [1e-02, 1e-03, 1e-04, 1e-05]
coupling[4] = [1e-02, 1e-03, 1e-04, 1e-05]
text_dir = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid/'
mg5 = '/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/MG5_aMC_v2_9_3/bin/mg5_aMC'
for decay in ['e', 'mu', 'tau']:
    for m, v in coupling.items():
            for c in v:
                if not decay == 'e': continue
                print(m,c)
                output = text_dir + "HNL_mg5_GRID_" + decay+"/HNL_mg5_GRID_"+decay+"-"+str(m)+"-"+str(c)
                print(mg5_dir + " " + output)
                file_name = 'submit/madgraph_production_m'+str(m)+'v'+str(c)+'.jdl'
                f = open(file_name, "w")
        	f.write("Universe = vanilla \n")
        	f.write("Executable = runMadgraph.sh \n")
        	f.write("Arguments = {} {} {} {} {} {}/ {}/ \n".format(decay, m, c, text_dir, mg5, os.getenv('CMSSW_BASE'), os.getenv('HOME')))


        	f.write("Log = log/HNL-{}_{}_{}_PC.log \n".format(decay, m, c))
        	f.write("Output = log/HNL-{}_{}_{}.out \n".format(decay, m, c))
        	f.write("Error = log/HNL-{}_{}_{}.err \n".format(decay, m, c))

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
        	f.write("Queue 1 \n")
        	print("condor_submit {} \n".format(file_name))
                f.close()

        	os.system("condor_submit {} --batch-name HNL-{}-{}-{}".format(file_name, decay, m, c))
