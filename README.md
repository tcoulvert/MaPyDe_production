# HEP Event Production
This repo contains the necassary tools to produce ttbar events with Madgraph, Pythia, and Delphes *without* using CMSSW. It does, however, assume you have access to a HPC cluster with HTCondor installed (i.e. this repo is tailored towards independent event production for CMS scientists and affiliates). If you need to change the process from ttbar to something else, its simple enough to change the madgraph card and the output directory and file names. If, however, you want to change to a different job manager, that would be more complicated, but the condor scripts can serve as a guide.

If you are a CMS person and you want to use CMSSW, the general form would stay the same, but you would need to change the singularity image to an el8 (or whatever is currently recommended by CMS for condor) image and install + build the packages inside the bash runscripts. But otherwise, the process would be the same.

This README assumes you have Apptainer (Singularity) installed.

## Software Installation

### Clone the repo
'''bash
git clone https://github.com/tcoulvert/MaPyDe_production/tree/main
'''

### Build the singularity image
'''bash
apptainer build heptools.simg docker://tcoulvert/heptools:madgraph-compiled
'''

## Editing the code
You likely need to edit the paths to the singularity image in the `submit_*.py` files under the `scripts_condor` directory. In those files is also where you specify the total number of events you'd like to generate, and the number of events-per-job (determined by how much RAM per job you have access to). I found that for LO ttbar, 100,000 events per madgraph job and 10,000 events per pythia-delphes job worked well within my 4GB RAM per CPU requirements. Both stages took ~10min to complete on the Caltech tier2 cluster.

***NOTE***: If you choose to change the number of events per madgraph job, remember to change it in both the `sumbit_madgraph_process.py` file and the `submit_delphes.py` file!! This is because the `submit_delphes.py` file needs to know the number of pythia-delphes jobs per madgraph job in order to find the correct madgraph LHE files. Also, make sure the number of madgraph events per job is integer divisable by the number of pythia-delphes events per job, or else you will not run some event through pythia-delphes.


## Madgraph
To change the process and parameters of Madgraph, edit the `cards/ttbar_hadronic.txt` file. Details on how to write a madgraph input file and an overview of madgraph itself are [here](https://indico.cern.ch/event/555228/sessions/203428/attachments/1315471/1970459/tutorial-CMSandATLAS-2016.pdf). For an overview of MC production as a whole check out the [2011 KIAS Madgraph school](http://workshop.kias.re.kr/MGLP/?Program) and the talks by [Frank Krauss from the 2007 HCP Summer School](https://indico.cern.ch/event/6238/contributions/speakers).

### Random seed
Currently, the random seed used by madgraph to generate its events (which **must** be different for every individual job) is updated manually in the `runMadgraph_process.sh` script using the Condor job ProcID. There is a way to tell madgraph you are running multiple runs (sets of events) and have it update the seed automatically, but I wasn't able to figure out how.

### Other ways of running Madgraph
According to the internet, you should be able to tell madgraph to run – across multiple cores, or runs, or on a cluster – and then run pythia and delphes automatically using the `<madgraph-output-directory>/bin/generate_events.sh` script. For example, [this article by Adarsh Pyarelal](https://adarsh.cc/posts/2016-04-15-madgraph-on-a-cluster.html). However, I was never able to get this to work as anytime I attempted to do so, madgraph would complain I needed to install the `pythia-pgs` package, which hasn;t been supported by its developers for more than 10 years – which madgraph knows, and will tell you as such if you try to install it. If you do choose to install `pythia-pgs` anyways, the installation will likely fail as the package is written in very old Fortran, which doesn't play nicely with the (likely) modern C/C++ you almost certainly have on your machine. If you do manage to get madgraph working this way, please let me know, I tried for many, many hours.


## Pythia
To change the processes and parameters of Pythia, edit the `cards/LHE_condor.cmnd` file. Details on how to write a command file as well as the various capabilities of pythia are given in [this pythia tutorial](http://home.thep.lu.se/~leifg/tutorials/) and in [pythia's documentation](https://pythia.org//latest-manual/Welcome.html). Refreshingly, the pythia documentation is extremely detailed, and describes the methodologies upon which their code is written, and links directly to the papers their taken from.


## Delphes
To change the processes and parameters of Delphes, edit the `cards/delphes_card_CMS_vfj.tcl` file. Details on how to write or modify the param file are given in the [delphes documentation](https://cp3.irmp.ucl.ac.be/projects/delphes/wiki/WorkBook). This is not as robust as pythia's, but in my experience you also don't need to change much in the delphes file for most "standard" analysis configurations.

### Very Fat Jets
For my use here, I wanted ak15 jets in addition to the CMS standard ak4 and ak8, so I added a function for ak15. Likely you do not want this, and should remove it.
