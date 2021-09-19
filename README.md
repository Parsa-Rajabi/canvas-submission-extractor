# Canvas Submission Extractor 

## About
This script looks up student Canvas IDs from a file and copy submission files with names having each ID as a substring. Useful for CMPT 120 TAs to extract submissions for the group they are marking.

## Set up
Name of the group the TA needs to mark format is "Marking Group X", replace X with a number

```
groupNeedtoBeMarked = "Marking Group 2"
```

Name of the file storing the group info download this at:
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

