'''
    Author: Christina Wang
    Date last modified: 4/30/2022
    Script to submit DelphesPythia8 on condor for HNL signal
'''

import os
import numpy as np
coupling = {}


pythia_card = '/storage/af/user/tsievert/topNet/SPAtop/simulation/MaPyDe_production/LHE_condor.cmnd'
delphes_card = '/storage/af/user/tsievert/topNet/SPAtop/simulation/MaPyDe_production/cards/delphes_card_CMS_vfj.dat'
lhe_dirpath = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit/madgraph/ttbar_hadronic"
outputDir = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit/pythiadelphes/ttbar_hadronic"


# nEventsPerJobMadgraph = 100_000
# totalEvents = 2_000_000
# nMadgraphJobs = totalEvents // nEventsPerJobMadgraph  # number of madgraph jobs
# maxNEvents = 10_000
# nJobs = totalEvents // maxNEvents
nEventsPerJobMadgraph = 1_000
totalEvents = 2_000
nMadgraphJobs = totalEvents // nEventsPerJobMadgraph  # number of madgraph jobs
maxNEvents = 500
nJobs = totalEvents // maxNEvents  # number of pythia/delphes jobs
nJobsPerMadgraphJob = nJobs // nMadgraphJobs

file_name = 'submit_pythia_delphes.jdl'
f = open(file_name, "w")
f.write("Universe = vanilla \n")
f.write("Executable = ../MaPyDe_production/scripts_condor/runDelphesPythia8.sh \n")

print(outputDir)
f.write("Arguments = {} $(ProcId) {} {} {} {} {} {}/ \n".format(
    lhe_dirpath, maxNEvents, nJobsPerMadgraphJob, pythia_card, delphes_card, outputDir, os.getenv('HOME')), 
)

f.write("Log = log/pythiadelphes.log \n")
f.write("Output = log/pythiadelphes.$(ProcId).out \n")
f.write("Error = log/pythiadelphes.$(ProcId).err \n")


f.write("RequestMemory = 2000 \n")
f.write("RequestCpus = 1 \n")
f.write("RequestDisk = 4 \n")
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
