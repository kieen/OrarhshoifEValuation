def printLatexHeaderAbstractionInfo(fileName):
  
    with open(fileName, mode='w', encoding='utf-8') as aFile:
        
        aFile.write(r'\documentclass{llncs}' + "\n")
        aFile.write(r'\begin{document}       ' + "\n")
        aFile.write(r'\begin{center}       ' + "\n")
        aFile.write(r' \begin{table*}[tb]      ' + "\n")
        aFile.write(r'\centering       ' + "\n")
        aFile.write(r'\caption{Number of refinement steps, size of the abstract ABoxes, and size of the abstract ABoxes in comparison with the original ABoxes for the first and the last abstraction}       ' + "\n")
        aFile.write(r' \label{tab:evalontologyresults}       ' + "\n")
        aFile.write(r'\begin{tabular}{|l || c || *{4}{r|r|r|r||} | *{4}{r|r|r|r|} }       ' + "\n")
        aFile.write(r'\hline       ' + "\n")
        aFile.write(r' &\#\,of       ' + "\n")
        aFile.write(r' % & \multicolumn{6}{c||}{Abstract ABox size (\%)}       ' + "\n")
        aFile.write(r'  &\multicolumn{4}{c||}{First Abstraction}      ' + "\n")
        aFile.write(r'  &\multicolumn{4}{c|}{Last Abstraction}\\     ' + "\n")            
        aFile.write(r' Ontology & steps     ' + "\n")
        aFile.write(r' &\#\,types &\#\,indiv.&\#\,assert.&\%\,assert.      ' + "\n")
        aFile.write(r' &\#\,types &\#\,indiv.&\#\,assert.&\%\,assert.\\      ' + "\n")
        aFile.write(r' \hline    ' + "\n")           


  

        
# prinLatexHeader(3,"test.tex")
