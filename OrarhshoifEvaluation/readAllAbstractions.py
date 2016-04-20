''' given a file contains all result/log files. This function will extract information about abstraction and put it in a latex format'''

from readAbstractionInfoForOneOntology import readAbstractionInfoForOneOntology

import sys
from printLatexHeaderAbstractionInfo import printLatexHeaderAbstractionInfo
from printLatexFooterAbstractionInfo import printLatexFooterAbstractionInfo
def readAbstractionInfoForAllOntologies(fileContainingAllResultFiles, latexResultFileName):
    printLatexHeaderAbstractionInfo(latexResultFileName)
    
    with open(fileContainingAllResultFiles, encoding='utf-8') as ontListFile:
        for aLine in ontListFile:
            aLine = str(aLine.strip())
            if not aLine == "" and not aLine.startswith("%") and not aLine.startswith("#"):
                print(aLine)
                resultString = readAbstractionInfoForOneOntology(aLine)    
                with open(latexResultFileName, mode='a', encoding='utf-8') as resultFile:
                    resultFile.write(resultString + "\n")
            
    
    
    printLatexFooterAbstractionInfo(latexResultFileName)
# test
# readAbstractionInfoForAllOntologies("allResultFile.txt", "latexResultFileName.tex")
if __name__ == '__main__':
    if len(sys.argv) == 3:
        readAbstractionInfoForAllOntologies(sys.argv[1], sys.argv[2]) 
         
    else:
        print("Please use only 2 arguments: aFileContainAListOfLogFile,  resultFile.tex")
        print("Example Run: readAbstractionInfoForAllOntologies  aFileContainAListOfLogFiles  resultFile.tex")

# Test
readAbstractionInfoForAllOntologies("logFiles/allLogFiles.txt", "latexInputOntology.tex")
    
             
