#script to run splitLHE for all coupling, mass, decay llp_MuonSystem_delphes

import os

inputDirectory="/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/hnl_standalone_production/mg5_grid/"
maxNEvents = 5000

coupling = {}
coupling[1] = [0.01, 0.001, 0.0001, 1e-05]
#coupling[2] = [0.01, 0.001, 0.0001, 1e-05]
#coupling[3] = [0.01, 0.001, 0.0001, 1e-05]
#coupling[4] = [0.01, 0.001, 0.0001, 1e-05]

for decay in ['e', 'mu', 'tau']:
	if not decay == 'e':continue
	for m, v in coupling.items():
		for c in v:
			print(m,c)
			inputLHE = inputDirectory + "HNL_GRID_{}/HNL_GRID_{}-{}-{}/Events/run_01/unweighted_events.lhe.gz".format(decay, decay, m, c)
			output = inputDirectory + "HNL_GRID_{}/HNL_GRID_{}-{}-{}/Events/run_01/unweighted_events_split".format(decay, decay, m, c)
			os.system("python splitLHE.py {} {} {}".format(inputLHE, output, maxNEvents))
