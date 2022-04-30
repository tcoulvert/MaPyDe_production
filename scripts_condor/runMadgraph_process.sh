#!/bin/sh

hostname
echo "Job started"
date
start_time=`date +%s`
decay=$1
mass=$2
coupling=$3
inputDirectory=$4
mg5=$5
runNum=$6
nEvents=$7
CMSSW_BASE=$8
homeDir=$9
currentDir=`pwd`
runDir=${currentDir}/christiw/

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

	#get grid proxy
	export X509_USER_PROXY=${homeDir}x509_proxy
	echo "${homeDir}x509_proxy"
	voms-proxy-info

	cd ${runDir}
	echo "entering directory: ${runDir}"
	echo "${CMSSW_BASE}/src/MG5_aMC_v2_9_3.tar.gz"
	if [ -f ${CMSSW_BASE}/src/MG5_aMC_v2_9_3.tar.gz ]
	then
		cp $CMSSW_BASE/src/MG5_aMC_v2_9_3.tar.gz .

		tar -zxvf MG5_aMC_v2_9_3.tar.gz
		mg5=MG5_aMC_v2_9_3/bin/mg5_aMC
		input=${inputDirectory}/HNL_mg5_GRID_${decay}/HNL_mg5_GRID_${decay}-${mass}-${coupling}
		ls ${input}
		cp ${input} input.dat
		echo "copied madgraph dat file"
		date


		echo "###############"
		echo "input.dat"
		echo "###############"
		cat input.dat
		
		echo "python ${mg5} input.dat"
		python ${mg5} input.dat

		##^_^##
		echo "madgraph finished"
		date


		sleep 2
		echo "I slept for 2 second"

		if [ -d ${inputDirectory}/HNL_GRID_${decay}/HNL_GRID_${decay}-${mass}-${coupling} ]
		then
			echo "job finished"
		else
			echo "job failed not copied"
		fi
	else
		echo echo "WWWWYYYY ============= failed to access file mg5, job anandoned"
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
