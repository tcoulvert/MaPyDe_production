'''
    Author: Christina Wang
    Date last modified: 4/30/2022
    Script to submit DelphesPythia8 on condor for HNL signal
'''

import os
import re
import numpy as np
coupling = {}


pythia_card = '/storage/af/user/tsievert/topNet/SPAtop/simulation/MaPyDe_production/cards/LHE_condor.cmnd'
delphes_card = '/storage/af/user/tsievert/topNet/SPAtop/simulation/MaPyDe_production/cards/delphes_card_CMS_vfj.tcl'
# lhe_dirpath = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit/madgraph/ttbar_hadronic"
# lhe_dirpath = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_Wm2j/madgraph/ttbar_semileptonicWm"
# lhe_dirpath = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_Wp2j/madgraph/ttbar_semileptonicWp"
# lhe_dirpath = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_semi/madgraph/ttbar_semileptonic"
# lhe_dirpath = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_4t/madgraph/4t_hadronic"
lhe_dirpath = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_qcd4j/madgraph/qcd4j"
# outputDir = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit/pythiadelphes/ttbar_hadronic"
# outputDir = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_Wm2j/pythiadelphes/ttbar_semileptonicWm"
# outputDir = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_Wp2j/pythiadelphes/ttbar_semileptonicWp"
# outputDir = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_semi/pythiadelphes/ttbar_semileptonic"
# outputDir = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_4t/pythiadelphes/4t_hadronic"
outputDir = "/storage/af/user/tsievert/topNet/SPAtop/simulation/submit_qcd4j/pythiadelphes/qcd4j"
os.makedirs(outputDir, exist_ok=False)


nEventsPerJobMadgraph = 10_000
totalEvents = 1_000_000
nMadgraphJobs = totalEvents // nEventsPerJobMadgraph  # number of madgraph jobs
maxNEvents = 10_000
nJobs = totalEvents // maxNEvents  # number of pythia/delphes jobs
nJobsPerMadgraphJob = nJobs // nMadgraphJobs

file_name = 'submit_pythia_delphes.jdl'
f = open(file_name, "w")
f.write("Universe = vanilla \n")
f.write("Executable = ../MaPyDe_production/scripts_condor/runDelphesPythia8.sh \n")

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
