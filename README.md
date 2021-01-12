# hnl_standalone_production

## Software Installation
MadGraph 2.8.1   
Pythia 8.235 (8.303 didn't work for me when I tried linking Pythia with Delphes, but if you are running them separately, then it doesn't matter)  
Delphes3.4.2  
ROOT 6.13/02. 
* Note: For MadGraph, Delphes, and ROOT, these are the only versions that I tried, other versions might or might not work. Only for Pythia, I checked with both Pythia2 and Pythia3, and only Pythia2 was linking to Delphes.
* For mac user: for some reason, ROOT6.22/04 installed from brew are not compatible with Delphes3.4.2. (Most likely it has to do with brew, not the ROOT version)

## MadGraph
* After installing MadGraph, copy and unzip the HNL model ```model/SM_HeavyN_Gen3Mass_NLO.tgz``` in the MadGraph model directory:```MG5_aMC_v2_8_1/models```
* run: ```scripts/HNL_grid.py```  to create the textfiles that set the mass/coupling of HNL, using the param and run card in the ```cards``` directory
  * will create 3 directories: HNL_mg5_GRID_e, HNL_mg5_GRID_mu, HNL_mg5_GRID_tau with one text file for each mass/coupling point in the dir ```mg5_grid```
* run ```run_HNL.py``` to launch madgraph and create LHE files using the text files in the previous step as inputs
  * 3 directories created in dir ```mg5_grid```: HNL_GRID_e, HNL_GRID_mu, HNL_GRID_tau
* ```getCrossSec.py``` uses the MadGraph output directories to obtain/validate the LO cross sections for each MadGraph simulation.
  * usage: python getCrossSec.py [runNum] [lep] [outfileName]

## Delphes
* After installing Delphes and pythia, compile Delphes with Pythia linked:
 ```bash  
  export PYTHIA8=/Users/christinawang/programs/pythia8235/
  make HAS_PYTHIA8=true
 ```
* Run the executable DelphesPythia8(takes LHE file and pythia parameters as input in .cmnd file and outputs ROOT file):
```bash
./DelphesPythia8 cards/delphes_card_CMS.tcl examples/Pythia8/configLHE.cmnd delphes_nolhe.root
```
