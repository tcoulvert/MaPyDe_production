#!/bin/sh

hostname
echo "Job started"
date
start_time=`date +%s`
inputFile=$1
outputDirectory=$2
mg5=$3
python=$4
nEvents=$5
ProcID=$6
homeDir=$7
currentDir=`pwd`
runDir=${currentDir}/madgraph/
outputFile=ttbar_hadronic_${ProcID}.lhe.gz

rm -rf ${runDir}
mkdir -p ${runDir}

if [ -f ${mg5} ] && [ -f ${inputFile} ]
then
	cd ${runDir}
	echo "entering directory: ${runDir}"


	echo "------------------------"

	input=${inputFile}
	cp ${input} input.dat
	echo "set run_card iseed ${ProcID}" >> input.dat
	echo "set run_card nevents ${nEvents}" >> input.dat
	echo "###############"
	echo "input.dat"
	echo "###############"
	cat input.dat
	echo "###############"
	echo "###############"
	
	echo "python ${mg5} input.dat"
	${python} ${mg5} input.dat

	echo "------------------------"

	##^_^##
	echo "madgraph finished"
	date

	echo "------------------------"

	sleep 2
	echo "I slept for 2 seconds"

	echo "------------------------"

	##job finished, copy file to T2
	echo "copying output file to ${outputDirectory}"
	mkdir -p ${outputDirectory}
	cp ${runDir}/ttbar_hadronic/Events/run_01/unweighted_events.lhe.gz ${outputDirectory}/${outputFile}

	if [ -f ${outputDirectory}/${outputFile} ]
	then
		echo ${outputFile} "copied"
	else
		echo ${outputFile} "not copied"
	fi
	
	echo "------------------------"
else
	echo echo "WWWWYYYY ============= failed to access mg5, job anandoned"
fi

cd ${currentDir}
#rm -rf ${runDir}
echo "Job finished"
date
end_time=`date +%s`
runtime=$((end_time-start_time))
echo ${runtime}
