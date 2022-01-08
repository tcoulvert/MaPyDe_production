#!/bin/sh

hostname
echo "Job started"
date
start_time=`date +%s`
decay=$1
mass=$2
coupling=$3
lhe_file=$4
index=$5
card=$6
outputDirectory=$7
CMSSW_BASE=$8
homeDir=$9
currentDir=`pwd`
#user=${homeDir#*/data/}
user=${homeDir#*/storage/user/}
runDir=${currentDir}/${user}_${analyzerTag}/
outputfile=hnl_${decay}_${mass}_${coupling}.root

rm -rf ${runDir}
mkdir -p ${runDir}

if [ -f /cvmfs/cms.cern.ch/cmsset_default.sh ]
then
	#setup cmssw
	#cd $CMSSW_BASE/src/
	cd ${CMSSW_BASE}/src/
	workDir=`pwd`
	echo "entering directory: ${workDir}"
	ulimit -c 0
	source /cvmfs/cms.cern.ch/cmsset_default.sh
	export SCRAM_ARCH=slc7_amd64_gcc630
	eval `scram runtime -sh`
	echo `which root`

	cd ${runDir}
	echo "entering directory: ${runDir}"
	echo "${CMSSW_BASE}/src/delphes.tar.gz"
	if [ -f ${CMSSW_BASE}/src/delphes.tar.gz ]
	then
		cp $CMSSW_BASE/src/delphes.tar.gz .
		#get grid proxy
		export X509_USER_PROXY=${homeDir}x509_proxy
		echo "${homeDir}x509_proxy"
		voms-proxy-info


		#run the job
		tar -zxvf delphes.tar.gz
		cd Delphes-3.4.2
		ls setup.sh
#		bash setup.sh

		my_pythia8=/storage/af/user/christiw/login-1/christiw/LLP/CMSSW_9_4_20/src/LLP-Reinterpretation/pythia8235
		echo ${my_pythia8}
		export PYTHIA8=${my_pythia8}
		export PATH=${my_pythia8}/bin:${PATH}
		export PYTHIA8DATA=${my_pythia8}/share/Pythia8/xmldoc
		echo $PYTHIA8DATA
		export LD_LIBRARY_PATH=${my_pythia}/lib:${LD_LIBRARY_PATH}

		echo $PYTHIA8
		echo $PYTHIA8DATA
		echo $LD_LIBRARY_PATH

		# cp ${lhe_file} input.lhe.gz
		# echo "copied lhe.gz file"
		# gunzip input.lhe.gz

		# output of run_splitLHE.py
		cp ${lhe_file}/unweighted_events_split_${index}.lhe input.lhe

		### add LHE file path to configLHE.cmnd
		echo "Beams:LHEF=input.lhe" >> examples/Pythia8/configLHE_condor.cmnd
		echo "###################"
		echo "PYTHIA CONFIGURATION"
		echo "###################"

		cat examples/Pythia8/configLHE_condor.cmnd

		echo "./DelphesPythia8 ${card}  examples/Pythia8/configLHE_condor.cmnd ${outputfile}"
		./DelphesPythia8 ${card}  examples/Pythia8/configLHE_condor.cmnd ${outputfile}
		ls ${outputfile}
		echo ${outputfile}
		echo ${outputDirectory}
		##^_^##
		echo "Delphes finished"
		date

		sleep 2
		echo "I slept for 2 second"

		##job finished, copy file to T2
		echo "copying output file to ${outputDirectory}"
		eval `scram unsetenv -sh`
		mkdir -p ${outputDirectory}
		cp ${outputfile} ${outputDirectory}/${outputfile}
		if [ -f ${outputDirectory}/${outputfile} ]
		then
			echo ${outputfile} "copied"
		else
			echo ${outputfile} "not copied"
		fi
	else
		echo echo "WWWWYYYY ============= failed to access file RazorRun_T2, job anandoned"
	fi

else
	echo "VVVVYYYY ============= failed to access file /cvmfs/cms.cern.ch/cmsset_default.sh, job abandoned"
fi

cd ${currentDir}
#rm -rf ${runDir}
echo "Job finished"
date
end_time=`date +%s`
runtime=$((end_time-start_time))
echo ${runtime}
