'''
generate madgraph lhe files, include both generating the process and launching the process and generate events
'''
import os, shutil
coupling = {}


# madgraph_string = 'ttbar_hadronic'
# madgraph_string = 'ttbar_semileptonic'
madgraph_string = '4t_hadronic'
# madgraph_string = 'qcd4j'
madgraphCard = f'/storage/af/user/tsievert/topNet/SPAtop/simulation/MaPyDe_production/cards/{madgraph_string}.txt'
mg5 = '/usr/MG5_aMC_v3_5_7/bin/mg5_aMC'
python = '/usr/bin/python3.10'
outputDir = f'/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_{madgraph_string}/madgraph/{madgraph_string}'
if os.path.exists(outputDir): shutil.rmtree(outputDir[:outputDir.find(f'submit_{madgraph_string}')+len(f'submit_{madgraph_string}')])
os.makedirs(outputDir, exist_ok=False)
os.makedirs(os.path.join('/'.join(outputDir.split('/')[:-2]), 'log'), exist_ok=False)
nEventsPerJob = 100_000
nJobs = 10_000_000 // nEventsPerJob


file_name = f'submit_{madgraph_string}/submit_madgraph.jdl'
f = open(file_name, "w")
f.write("Universe = vanilla \n")
f.write("Executable = MaPyDe_production/scripts_condor/runMadgraph_process.sh \n")
f.write("Arguments = {} {} {} {} {} $(ProcID) {}/ \n".format(madgraphCard, os.path.normpath(outputDir), mg5, python, nEventsPerJob, os.getenv('HOME')))

f.write(f"Log = submit_{madgraph_string}/log/madgraph.log \n")
f.write(f"Output = submit_{madgraph_string}/log/madgraph.$(ProcID).out \n")
f.write(f"Error = submit_{madgraph_string}/log/madgraph.$(ProcID).err \n")

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
