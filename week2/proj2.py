
import sys

validTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
exceptionTags = ["INDI", "FAM"]

def inputCheck(familyTree):
    for line in familyTree.splitlines():

        # Split string into an array of works, breaking string at every space
        lineArray = line.split()

        # Set level of GEDCOM line
        level = lineArray[0]

        # Set tag, check if tag is of exception ("INDI" or "FAM")
        if (lineArray[2] in exceptionTags):
            lineArray[1], lineArray[2] = lineArray[2], lineArray[1]
        tag = lineArray[1]

        # Check if current GEDCOM line is valid entry
        valid = 'Y' if (tag in validTags) else 'N'

        print("--> " + line)
        print("<-- " + level + '|' + tag + '|' + valid + '|' + " ".join(lineArray[2:]))

def main():
    with open(sys.argv[1], 'r') as gedFile:
        inputCheck(gedFile.read())

if __name__ == "__main__":
    main()