Python code to parse log files of OrarHSHOIF

1) Get information of the abstraction:
Step 1: Prepare input: 
	1.1 You need to have the log files of all ontologies. 
    1.2 Put all (paths of) those log files into one file, e.g. allLogFiles.txt
Step 2: run the following command 
	python3 readAbstractionInfoForAllOntologies.py  allLogFiles   latexResultFile.tex

This will generate a latex file    latexResultFile.tex.
You can use latexpdf latexResultFile.tex to compile 
