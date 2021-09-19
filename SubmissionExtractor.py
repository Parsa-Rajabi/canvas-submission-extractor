# Submission Extractor
# Author: Dr. Victor Cheung
# Date: 15 Sep, 2021

# Description: This script looks up student Canvas IDs from a file
# and copy submission files with names having each ID as a substring.
# Useful for CMPT 120 TAs to extract submissions for the group they are marking.

import os
import shutil

### constants setup ###
# name of the group the TA needs to mark
# format is "Marking Group X", replace X with a number
groupNeedtoBeMarked = "Marking Group 2"

# name of the file storing the group info
# download this at Canvas Course side bar > People >
#   Select the group tab "For Marking Purposes Only" >
#   + Import > Download Course Roster CVS from the bottom
groupInfoFilename = "CMPT 120 - Group Export.csv"

separator = os.path.sep #os specific file separator

# name of the directory storing all the submissions
# must be at the same level of this .py script
sourceDir = "." + separator + "submissions"

# name of the directory storing all the extracted (copied) submissions
# preferrably does not exist so this .py script will create it
destDir = "." + separator + groupNeedtoBeMarked

if os.path.exists(destDir) :
    print("Directory/File " + destDir +" already exists, remove it first.")

else :
    # create the directory to store the extracted files
    os.makedirs(destDir, True)

    ### The actual work ###
    # get the list of all files and directories in the submission directory
    fileList = os.listdir(sourceDir)

    # open the file storing the group info
    groupInfoFile = open(groupInfoFilename)
    for i in range(1) : # remove multiple non-data lines
        groupInfoFile.readline()

    submissionsCopied = 0 #counter for how many submissions are copied in this gourp

    # for each line, get the group number and ID (Canvas ID, not SFU ID)
    for student in groupInfoFile :
        items = student.strip().split(",") #note: each name has a comma too...
        groupNumber = items[6] #retrieve which group the student belongs to
        canvasID = items[2] #retrieve the Canvas ID
        #print("reading student at " + groupNumber + " " + canvasID)

        if groupNumber == groupNeedtoBeMarked :
            # go through the file list and find those with a matching Canvas ID
            for file in fileList:
                canvasIDinFile = file.split("_")[1]
                if canvasIDinFile == canvasID :
                    print("Copying... " + file)
                    shutil.copy(sourceDir+separator+file, destDir+separator+file)

            # display some info
            print("Copied submissions for " + items[0] + ", " + items[1] + "\n")
            submissionsCopied += 1

    # done copying
    print("Extraction done. " + str(submissionsCopied) + " copied.")
    print("Good luck marking!")
