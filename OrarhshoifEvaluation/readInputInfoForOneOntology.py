#!/usr/bin/env python3
'''Vocabulary: copied from StatisticVocabulary.java '''
import os
from readAbstractionInfoForOneOntology import NUMBER_OF_INPUT_INDIVIDUALS
''' input ontology'''
NUMBER_OF_TBOX_AXIOMS = "Statistic: Number_of_TBox_Axioms = "
NUMBER_OF_INPUT_CONCEPTASSERTIONS = "Statistic: Number_of_input_concept_assertions = "
NUMBER_OF_INPUT_ROLEASSERTIONS = "Statistic: Number_of_input_role_assertions = "
NUMBER_OF_INPUT_ASSERTIONS = "Statistic: Number_of_input_concept_and_role_assertions = "

'''signature'''
NUMBER_OF_INPUT_INDIVIDUALS = "Statistic: Number_of_input_individuals = "
NUMBER_OF_INPUT_CONCEPTNAMES = "Statistic: Number_of_input_concept_names = "
NUMBER_OF_INPUT_ROLENAMES = "Statistic: Number_of_input_role_names = "

# '''materialization'''
# NUMBER_OF_MATERIALIZED_CONCEPTASSERTIONS = "Statistic: Number_of_materialized_concept_assertions = "
# NUMBER_OF_MATERIALIZED_ROLEASSERTIONS = "Statistic: Number_of_materialized_role_assertions = "
NUMBER_OF_MATERIALIZED_ASSERTIONS = "Statistic: Number_of_materialized_concept_and_role_assertions = "


''' given a log file, e.g. imdb.result.txt, this function will return a string of the following format:
nameOfTheFile   &number_of_refinement_steps 
& #types_in_1st_abstraction  &#individual_1st_abstraction & #assertions_1st_abstraction & %size_1st_abstraction_wrt_originalAbox
& #types_in_last_abstraction  &#individual_last_abstraction & #assertions_last_abstraction & %size_last_abstraction_wrt_originalAbox
\\
'''
def readInputOntologyInfo(logFilePath):
    
    fileName = os.path.basename(logFilePath)
    splittedExentsion = os.path.splitext(fileName)
    fileNameWoExtension = splittedExentsion[0]
    
    resultingString = ""
    with open(logFilePath, encoding='utf-8') as logFile:
        for aline in logFile:
            aline = str(aline.strip())
            '''print TBox information'''
            if "Ontology file:" in aline:
                print(aline)
            
            value, success = getInputOntologyInformation(aline, NUMBER_OF_INPUT_CONCEPTNAMES)
            if success:
                numberOfConceptNames = value
                
            value, success = getInputOntologyInformation(aline, NUMBER_OF_INPUT_ROLENAMES)
            if success:
                numberOfRoleNames = value
            
            value, success = getInputOntologyInformation(aline, NUMBER_OF_TBOX_AXIOMS)
            if success:
                numberOfTBoxAxioms = value
                
            value, success = getInputOntologyInformation(aline, NUMBER_OF_INPUT_INDIVIDUALS) 
            if success:
                numberOfInputIndividuals = value  
                
            value, success = getInputOntologyInformation(aline, NUMBER_OF_INPUT_ASSERTIONS) 
            if success:
                numberOfInputAssertions = value  
            
           
            '''print ABox information'''
            if "ABoxList file" in aline:
                print("\n" + aline + "\n")
            '''override number of input individuals in case the aboxes are separated from the tbox'''
            value, success = getInputOntologyInformation(aline, NUMBER_OF_INPUT_INDIVIDUALS) 
            if success:
                numberOfInputIndividuals = value  
            '''override number of input individuals in case the aboxes are separated from the tbox'''
            value, success = getInputOntologyInformation(aline, NUMBER_OF_INPUT_ASSERTIONS) 
            if success:
                numberOfInputAssertions = value  
              
            value, success = getInputOntologyInformation(aline, NUMBER_OF_MATERIALIZED_ASSERTIONS)
            if success:
                numberOfMaterializedAssertions = value
                
    resultingString += str(fileNameWoExtension) + " & DL language  &$" + str(numberOfTBoxAxioms) + "$  &$" +  str(numberOfConceptNames) + \
      "$  &$" + str(numberOfRoleNames) + "$  &$" + str(numberOfInputIndividuals) + "$  &$" + str(numberOfInputAssertions) + "$  &$" + str(numberOfMaterializedAssertions) + "$   \\\\ \n"
    print(resultingString)        
    return resultingString
            



def getInputOntologyInformation(aString, informationToGet):
    listOfStrings = str(aString).split(informationToGet)
    sizeOfResultingList = len(listOfStrings)
    if sizeOfResultingList > 1:
        return (listOfStrings[1], True)
    return (None, False)

# '''test'''
readInputOntologyInfo("logFiles/imdb.result.txt")
