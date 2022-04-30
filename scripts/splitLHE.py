import sys
import os
import numpy as np
import gzip
import math

if len(sys.argv) < 4:
    print("Three parameters are required: python splitLHE.py [input filename] [output filename] [max number of events per output file] [index(optional)]")
    exit()

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]
maxNEvents = int(sys.argv[3])
if len(sys.argv)==4:index = -1
else:index = int(sys.argv[4])
print ("Input file: " + inputfilename)
print ("Output files: " + outputfilename)
print ("Max Number of Events in Output: " + str(maxNEvents))

inputfile = gzip.open(inputfilename, "r")

inputEventIndex = -1
currentFileEventIndex = -1;

headerLineIndex = -1
fileEndLine = 0
headerLines = []
fileEndLine = "</LesHouchesEvents>"
event_start_indices = []
event_end_indices = []
lineIndex = 0
fileIndex = 0
event_counter = maxNEvents
for line in inputfile:
    if '<event>' in line: event_start_indices.append(lineIndex)
    if '</event>' in line: event_end_indices.append(lineIndex)
    if len(event_start_indices)== 0: headerLines.append(line)
    else:
        if '<event>' in line and event_counter == maxNEvents: #open a new file and write header +write this line
            # Close previous file
            if fileIndex > 0:
                tempOutputFile.write(fileEndLine)
                tempOutputFile.close()
                if fileIndex % 10 == 0: print("Closing file " + tempOutputFileName)
		if fileIndex == index+1:break
            #Open new file
            tempOutputFileName = outputfilename+"_"+str(fileIndex)+".lhe"
            tempOutputFile = open(tempOutputFileName, "w")
            # Write header
            for l in headerLines:
                tempOutputFile.write(l)
            event_counter = 1
            fileIndex+=1
        elif '<event>' in line: event_counter +=1

        tempOutputFile.write(line)

    lineIndex = lineIndex + 1 #increment line counter


#assert(len(event_start_indices) == len(event_end_indices))
nFiles = int(math.ceil(1.0*len(event_start_indices)/maxNEvents))
print("NEvents: "+str(len(event_start_indices)))
print("nFiles: "+str(nFiles))
