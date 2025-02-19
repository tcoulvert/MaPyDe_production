#!/bin/sh

hostname
echo "Job started"
date
start_time=`date +%s`
lhe_dir=$1
ProcID=$2
maxNEvents=$3
nJobsPerMadgraphJob=$4
pythiaCard=$5
delphesCard=$6
outputDirectory=$7
pythiaDir=$8
delphesDir=$9
python=${10}
homeDir=${11}
currentDir=`pwd`
user=${homeDir#*/storage/af/user/}
runDir=${currentDir}/pythiadelphes/
lhe_file=${lhe_dir}/ttbar_hadronic_$((${ProcID} / ${nJobsPerMadgraphJob})).lhe.gz
lhe_split_index=$((${ProcID} % ${nJobsPerMadgraphJob}))
outputFile=ttbar_hadronic_${ProcID}.root

rm -rf ${runDir}
mkdir -p ${runDir}

if [ -d ${pythiaDir} ] && [ -d ${delphesDir} ]
then
	cd ${runDir}
	echo "entering directory: ${runDir}"

	echo "${python}"
	echo "------------------------"

	# run splitLHE.py
	cp ${lhe_file} input.lhe.gz
	cp /storage/af/user/tsievert/topNet/SPAtop/simulation/MaPyDe_production/scripts/splitLHE.py .
	${python} splitLHE.py input.lhe.gz split_${ProcID} ${maxNEvents} ${lhe_split_index}
	echo "------------------------"
	ls
	echo "------------------------"

	### add LHE file path to configLHE.cmnd
	cp ${pythiaCard} config_pythia.cmnd
	echo -e "\nBeams:LHEF=split_${ProcID}.lhe" >> config_pythia.cmnd
	# echo "Beams:LHEF=split_${ProcID}.lhe" > config_pythia.cmnd
	# echo "###################"
	# echo "PYTHIA CONFIGURATION"
	# echo "###################"
	# cat config_pythia.cmnd

	### add LHE file path to configLHE.cmnd
	cp ${delphesCard} config_delphes.dat
	# echo "###################"
	# echo "DELPHES CONFIGURATION"
	# echo "###################"
	# cat config_delphes.dat
	
	echo "${delphesDir}/DelphesPythia8 config_delphes.dat config_pythia.cmnd ${outputFile}"
	${delphesDir}/DelphesPythia8 config_delphes.dat config_pythia.cmnd ${outputFile}
	
	echo ${outputFile}
	##^_^##
	echo "Delphes finished"
	date

	sleep 2
	echo "I slept for 2 second"

	##job finished, copy file to T2
	echo "copying output file to ${outputDirectory}"
	mkdir -p ${outputDirectory}
	cp ${outputFile} ${outputDirectory}/${outputFile}
	# if [ -f ${outputDirectory}/${outputfile} ]
	# then
	# 	echo ${outputfile} "copied"
	# else
	# 	echo ${outputfile} "not copied"
	# fi

else
	echo "VVVVYYYY ============= failed to access file Pythia or Delphes, job abandoned"
fi

cd ${currentDir}
#rm -rf ${runDir}
echo "Job finished"
date
end_time=`date +%s`
runtime=$((end_time-start_time))
echo ${runtime}
