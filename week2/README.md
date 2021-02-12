# Exec Summary
Create a small GEDCOM file to use in testing your program. You may reuse the file you submitted for assignment Project 01 or create a new one. Make sure that it includes a NOTE record at the beginning with your name.

# Requirements
- Write a short program that:
    - Reads each line of a GEDCOM file
    - Prints "--> <input line>"
    - Prints "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
        - <level> is the level of the input line, e.g. 0, 1, 2
        - <tag> is the tag associated with the line, e.g. 'INDI', 'FAM', 'DATE', ...
        - <valid?> has the value 'Y' if the tag is one of the supported tags or 'N' otherwise.  The set of all valid tags for our project is specified in the Project Overview document.
        - <arguments> is the rest of the line beyond the level and tag.

# Sample Input
0 NOTE dates after now__
1 SOUR Family Echo__
2 WWW http://www.familyecho.com  (Links to an external site.)__
0 bi00 INDI__
1 NAME Jimmy /Conners/

# Sample Output
--> 0 NOTE dates after now__
<-- 0|NOTE|Y|dates after now__
--> 1 SOUR Family Echo__
<-- 1|SOUR|N|Family Echo__
--> 2 WWW http://www.familyecho.com (Links to an external site.) (Links to an external site.)__
<-- 2|WWW|N|http://www.familyecho.com (Links to an external site.)__
--> 0 bi00 INDI__
<-- 0|INDI|Y|bi00__
--> 1 NAME Jimmy /Conners/__
<-- 1|NAME|Y|Jimmy /Conners/