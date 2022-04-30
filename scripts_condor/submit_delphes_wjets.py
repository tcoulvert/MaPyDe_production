# script to submit DelphesPythia for wjets
import os



config_card = 'cards/delphes_card_CMS_CSCCluster_hnl_PileUp.tcl'
input_lhe_path = "/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/w_production/"
output_delphes_path = "/storage/af/user/christiw/delphes_output/v11/wjets/"
nJobs = 100
maxNEvents = 10000
run = 'run_01'

os.system("rm -rf log/HNL-delphes-{}-wjets*".format(run))
os.system("rm -rf submit/delphes-{}-wjets*".format(run))

lhe_file = "{}/Events/{}/".format(input_lhe_path, run)

file_name = 'submit/delphes-'+run+'_wjets.jdl'
f = open(file_name, "w")
f.write("Universe = vanilla \n")
f.write("Executable = runDelphesPythia8.sh \n")
outputDir = '{}/{}/'.format(output_delphes_path, run)

print(outputDir)
f.write("Arguments = {} {} {} {} $(ProcId) {} {} {} {}/ {}/ \n".format('wjets', 'wjets', 'wjets', lhe_file, maxNEvents, config_card, outputDir, os.getenv('CMSSW_BASE'), os.getenv('HOME')))

f.write("Log = log/HNL-delphes-{}_$(ProcId)_PC.log \n".format(run))
f.write("Output = log/HNL-delphes-{}_$(ProcId).out \n".format(run))
f.write("Error = log/HNL-delphes-{}_$(ProcId).err \n".format(run))


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
os.system("condor_submit {} --batch-name HNL-delphes-wjets".format(file_name))
