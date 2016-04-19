#!/usr/bin/env python3
'''Vocabulary: copied from StatisticVocabulary.java '''
''' input ontology'''
NUMBER_OF_TBOX_AXIOMS = "Statistic: Number_of_TBox_Axioms = "
NUMBER_OF_INPUT_CONCEPTASSERTIONS = "Statistic: Number_of_input_concept_assertions = "
NUMBER_OF_INPUT_ROLEASSERTIONS = "Statistic: Number_of_input_role_assertions = "
NUMBER_OF_INPUT_ASSERTIONS = "Statistic: Number_of_input_concept_and_role_assertions = "

'''signature'''
NUMBER_OF_INPUT_INDIVIDUALS = "Statistic: Number_of_input_individuals = "
NUMBER_OF_INPUT_CONCEPTNAMES = "Statistic: Number_of_input_concept_names = "
NUMBER_OF_INPUT_ROLENAMES = "Statistic: Number_of_input_role_names = "

'''materialization'''
NUMBER_OF_MATERIALIZED_CONCEPTASSERTIONS = "Statistic: Number_of_materialized_concept_assertions = "
NUMBER_OF_MATERIALIZED_ROLEASSERTIONS = "Statistic: Number_of_materialized_role_assertions = "
NUMBER_OF_MATERIALIZED_ASSERTIONS = "Statistic: Number_of_materialized_concept_and_role_assertions = "
'''abstraction'''
NUMBER_OF_TYPES = "Statistic: Number_of_types = "
NUMBER_OF_X = "Statistic: Number_of_x = "
NUMBER_OF_U = "Statistic: Number_of_u = "
NUMBER_OF_YZ = "Statistic: Number_of_yz = "
NUMBER_OF_ABSTRACT_INDIVIDUALS = "Statistic: Number_of_abstract_individuals_xuyz = "
CURRENT_LOOP = "Statistic: Current_loop = "
NUMBER_OF_ABSTRACT_CONCEPTASSERTIONS = "Statistic: Number_of_abstract_concept_assertions = "
NUMBER_OF_ABSTRACT_ROLEASSERTIONS = "Statistic: Number_of_abstract_role_assertions = "
NUMBER_OF_ABSTRACT_ASSERTIONS = "Statistic: Number_of_abstract_concept_and_role_assertions = "

''' global abstractionDict, will store a dictioinary of the form:
 <LoopNumber, dict{<#Type, n1>, <#AbstractIndividuals,n2>, <#AbstractAssertions,n3>}}>'''
abstractionDict = {}
# global numberOfInputAssertions
numberOfInputAssertions = 1
globalLogFileName = ""
''' given a log file, e.g. imdb.result.txt, this function will return a string of the following format:
nameOfTheFile   &number_of_refinement_steps 
& #types_in_1st_abstraction  &#individual_1st_abstraction & #assertions_1st_abstraction & %size_1st_abstraction_wrt_originalAbox
& #types_in_last_abstraction  &#individual_last_abstraction & #assertions_last_abstraction & %size_last_abstraction_wrt_originalAbox
\\
'''
def readAbstractionInfoForOneOntology(logFileName):
    global globalLogFileName
    globalLogFileName = logFileName
    startAbox = False
    # a dictionary for abstraction which map the first(1), second (2),... abstraction to its info,e.g. type, size,..., stored in a list

    with open(logFileName, encoding='utf-8') as logFile:
        for aline in logFile:
            aline = str(aline.strip())
            '''print TBox information'''
            if "Ontology file:" in aline:
                print(aline)
             
            printInputInformation(aline, NUMBER_OF_INPUT_CONCEPTNAMES)
            printInputInformation(aline, NUMBER_OF_INPUT_ROLENAMES)
            printInputInformation(aline, NUMBER_OF_TBOX_AXIOMS)
            
            '''print ABox information'''
            if "ABoxList file" in aline:
                print("\n" + aline + "\n")
                startAbox = True
            if startAbox:
                printInputInformation(aline, NUMBER_OF_INPUT_INDIVIDUALS)
                printInputInformation(aline, NUMBER_OF_INPUT_CONCEPTASSERTIONS)
                printInputInformation(aline, NUMBER_OF_INPUT_ROLEASSERTIONS)
                printInputInformation(aline, NUMBER_OF_INPUT_ASSERTIONS)
                numberOfInputAssertionsReadFromThisLine = getInformation(aline, NUMBER_OF_INPUT_ASSERTIONS) 
               
                if not (numberOfInputAssertionsReadFromThisLine is None):
                    global numberOfInputAssertions
                    numberOfInputAssertions = numberOfInputAssertionsReadFromThisLine
                  
            getAbstractionInfoForOneLoop(aline, NUMBER_OF_TYPES)
            getAbstractionInfoForOneLoop(aline, NUMBER_OF_ABSTRACT_INDIVIDUALS)
            getAbstractionInfoForOneLoop(aline, NUMBER_OF_ABSTRACT_ASSERTIONS)
            
    return getAbstractionInfoForAllLoops()
            
'''  '''
def getAbstractionInfoForAllLoops():
    resultingString = ""
    keys = list(abstractionDict.keys())
    keys.sort()
    for key in keys:
        print(key + "&    " + "\t", end="")
    print()
    
    '''print the ontology name'''
    print(globalLogFileName + "  ", end="")
    resultingString += globalLogFileName + "  "
    
    '''print number of refinements steps'''
    print("&$%d$ " % (len(keys)-1), end="")
    resultingString += "&$" + str(len(keys)-1) + "$ "
    
    '''print the first and the last abstracion information'''
    firstAndLastKeys = []
    firstAndLastKeys.append(keys[0])
    firstAndLastKeys.append(keys[-1])
    for key in firstAndLastKeys:
        value = abstractionDict[key]
#         print("&$" + value[NUMBER_OF_TYPES] + "$  ", end="")
        resultingString += "&$" + value[NUMBER_OF_TYPES] + "$  "
        
#         print("&$" + value[NUMBER_OF_ABSTRACT_INDIVIDUALS] + "$  ", end="")
        resultingString += "&$" + value[NUMBER_OF_ABSTRACT_INDIVIDUALS] + "$  "
        
#         print("&$" + value[NUMBER_OF_ABSTRACT_ASSERTIONS] + "$  ", end="")
        resultingString += "&$" + value[NUMBER_OF_ABSTRACT_ASSERTIONS] + "$  "
        
        abstractionSizeCompression = float(value[NUMBER_OF_ABSTRACT_ASSERTIONS]) / float(numberOfInputAssertions) * 100
        abstractionSizeCompressionString = "{0:.3f}".format(abstractionSizeCompression)
        resultingString += "&$" + abstractionSizeCompressionString + "$ "
#         print("&$%.3f$ " % (abstractionSizeCompression), end="")
           
#     print("\\\\")
    resultingString += "\\\\"
    print(resultingString)
    return  resultingString

def printInputInformation(aString, informationToBePrinted):
    listOfStrings = str(aString).split(informationToBePrinted)
    sizeOfResultingList = len(listOfStrings)
    if sizeOfResultingList > 1:
        print(informationToBePrinted + listOfStrings[1])
        return listOfStrings[1]

def getInformation(aString, informationToGet):
    listOfStrings = str(aString).split(informationToGet)
    sizeOfResultingList = len(listOfStrings)
    if sizeOfResultingList > 1:
        return listOfStrings[1]

'''get a specific number in one loop, e.g. NUMBER_OF_ABSRTACT_INDIVIDUALS, and put it to the global dictionary'''
def getAbstractionInfoForOneLoop(aLine, informationToGet):
    aString = str(aLine)
    if CURRENT_LOOP in aString and informationToGet in aString:
        twoSplittedParts = aString.split(";")
#         print(aString)
        abstractionLoop = getInformation(twoSplittedParts[0], CURRENT_LOOP)
#         print(abstractionLoop)
        informationValue = getInformation(aString, informationToGet)
#         print(informationValue)
        ''' put them to the dictionary'''
        updateDictionary(abstractionLoop, informationToGet, informationValue)
        return (abstractionLoop, informationToGet, informationValue)
    
        
''' add a new value to the dictionary for abstraction'''        
def updateDictionary(key, typeOfTheValue, addedValue):
    existingValues = abstractionDict.get(key)
    if existingValues == None:
        existingValues = {}
         
    existingValues[typeOfTheValue] = addedValue
    abstractionDict[key] = existingValues
# '''test'''
# readAbstractionInfoForOneOntology("imdb.result.txt")
