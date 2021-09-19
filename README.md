# Canvas Submission Extractor 

## About
This script looks up student Canvas IDs from a file and copy submission files with names having each ID as a substring. Useful for CMPT 120 TAs to extract submissions for the group they are marking.

## Steps:
- Step 1: download it to a directory (best if there is nothing else in it)
- Step 2: download the group assignment (Refer to below on how to do so), rename it to `CMPT 120 - Group Export.csv`
- Step 3: download the submissions, unzip them, put them in a directory called `submissions` (note all lowercase) next to the script
- Step 4: open the script with IDLE, update line 15 to match with the group you are marking
- Step 5: run the script, a directory with the group name will be created and all the files that needed to be marked will be copied there

## Constants 
Name of the group the TA needs to mark format is "Marking Group X", replace X with a number

```
groupNeedtoBeMarked = "Marking Group 2"
```

Name of the file storing the group info:
1. Canvas Course side bar
2. People
3. Select the group tab "For Marking Purposes Only" 
4. Select "+ Import" 
5. Download Course Roster CVS from the bottom

Ensure you name the file the same as the following: 

```
groupInfoFilename = "CMPT 120 - Group Export.csv"
```

## Credits
- Author: Dr. Victor Cheung - September 2021
- Edits: Parsa Rajabi - September 2021

