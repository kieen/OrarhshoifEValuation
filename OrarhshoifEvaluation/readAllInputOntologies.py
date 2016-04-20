''' given a file contains all result/log files. This function will extract information about abstraction and put it in a latex format'''



import sys
from readInputInfoForOneOntology import readInputOntologyInfo



def readAllOntologies(fileContainingAllResultFiles, latexResultFileName):
        
    appendContent("inputOntologyHeader.txt", latexResultFileName, 'w')
    with open(fileContainingAllResultFiles, encoding='utf-8') as ontListFile:
        for aLine in ontListFile:
            aLine = str(aLine.strip())
            if not aLine == "" and not aLine.startswith("%") and not aLine.startswith("#"):
                print(aLine)
                resultString = readInputOntologyInfo(aLine)    
                with open(latexResultFileName, mode='a', encoding='utf-8') as resultFile:
                    resultFile.write(resultString + "\n")
            
    
    
    appendContent("inputOntologyFooter.txt", latexResultFileName, 'a')

def appendContent(sourceFile, targetFile, modeFlag):
    with open(targetFile, mode=modeFlag, encoding='utf-8') as theTargetFile:
        with open(sourceFile, mode='r', encoding='utf-8') as theSourceFile:
            for aLine in theSourceFile:
                theTargetFile.write(aLine)
# test
readAllOntologies("logFiles/allLogFiles.txt", "latexInputOntology.tex")
if __name__ == '__main__':
    if len(sys.argv) == 3:
        readAllOntologies(sys.argv[1], sys.argv[2]) 
         
    else:
        print("Please use only 2 arguments: aFileContainAListOfLogFile,  resultFile.tex")
        print("Example Run: readAllAbstractions  aFileContainAListOfLogFiles  resultFile.tex")
        
