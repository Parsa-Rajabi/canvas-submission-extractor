# Canvas Submission Extractor 

## About
This script looks up student Canvas IDs from a file and copy submission files with names having each ID as a substring. Useful for CMPT 120 TAs to extract submissions for the group they are marking.

## Steps:
1. download it to a directory (best if there is nothing else in it)
2. download the group assignment (Refer to below on how to do so), rename it to `CMPT 120 - Group Export.csv`
3. download the submissions, unzip them, put them in a directory called `submissions` (note all lowercase) next to the script
4. open the script with IDLE, update line 15 to match with the group you are marking
5. run the script, a directory with the group name will be created and all the files that needed to be marked will be copied there

## How to Download Group CSV + Submissions
### Submissions
1. Canvas Course
2. Grade
3. Find exercise that needs to be marked
4. Select the triple dots beside it (screen below)
5. Select Download Submission
6. Rename to `submissions`

![image](https://user-images.githubusercontent.com/34695166/133945658-82f96a13-7103-4fc3-8032-ca6e9124dd48.png)

### Group CSV
1. Canvas Course side bar
2. People
3. Select the group tab "For Marking Purposes Only" 
4. Select "+ Import" 
5. Download Course Roster CVS from the bottom
6. Rename it to `CMPT 120 - Group Export.csv`

![image](https://user-images.githubusercontent.com/34695166/133945597-a07e2d3a-4c5f-4bcf-be6b-10cbf671f08d.png)


## Constants 
Name of the group the TA needs to mark format is "Marking Group X", replace X with a number
```
groupNeedtoBeMarked = "Marking Group 2"
```

## Credits
- Author: Dr. Victor Cheung
- Documenattion + Updates: Parsa Rajabi 

