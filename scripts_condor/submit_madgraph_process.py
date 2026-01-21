'''
generate madgraph lhe files, include both generating the process and launching the process and generate events
'''
import os
coupling = {}


madgraphCard = '/storage/af/user/tsievert/topNet/SPAtop/simulation/MaPyDe_production/cards/ttbar_hadronic.txt'
mg5 = '/usr/MG5_aMC_v3_5_7/bin/mg5_aMC'
python = '/usr/bin/python3.10'
outputDir = '/storage/af/user/tsievert/topNet/SPAtop/simulation/submit/madgraph/ttbar_hadronic'
nEventsPerJob = 100_000
nJobs = 200_000_000 // nEventsPerJob


file_name = 'submit_madgraph.jdl'
f = open(file_name, "w")
f.write("Universe = vanilla \n")
f.write("Executable = ../MaPyDe_production/scripts_condor/runMadgraph_process.sh \n")
f.write("Arguments = {} {} {} {} {} $(ProcID) {}/ \n".format(madgraphCard, outputDir, mg5, python, nEventsPerJob, os.getenv('HOME')))

f.write("Log = log/madgraph.log \n")
f.write("Output = log/madgraph.$(ProcID).out \n")
f.write("Error = log/madgraph.$(ProcID).err \n")

f.write("RequestMemory = 4GB \n")
f.write("RequestCpus = 1 \n")
f.write("RequestDisk = 4GB \n")
f.write("+JobQueue=\"Short\" \n")
# f.write("+JobQueue=\"Long\" \n")

f.write("+RunAsOwner = True \n")
f.write("+InteractiveUser = true \n")
f.write("+SingularityImage = \"{}/public/heptools-compiled.simg\" \n".format(os.getenv('HOME')))
f.write('+SingularityBindCVMFS = False \n')
f.write("run_as_owner = True \n")
f.write("x509userproxy = {}/x509_proxy \n".format(os.getenv('HOME')))
f.write("should_transfer_files = YES \n")
f.write("when_to_transfer_output = ON_EXIT_OR_EVICT \n")
f.write("Queue {} \n".format(nJobs))
print("condor_submit {} \n".format(file_name))
f.close()

os.system("condor_submit {}".format(file_name))
