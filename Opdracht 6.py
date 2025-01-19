def complexity_score(text):
    """
    Het is jouw taak om een functie complexity_score(text) te schrijven die een string text als parameter accepteert en als 
    resultaat een score (float) teruggeeft. De string text kan meerdere zinnen bevatten.
    """
    
    complex_elements = 0
    total_elements = 0
    zin = 0
    woord_counter = 0

    sentences = text.split(".")[:-1]

    for x in sentences:
        woorden = sentences[zin].split()
        if len(woorden) >= 15:
            complex_elements += 1    
        zin += 1  
        for woord in woorden:
            total_elements += 1
            if len(woord) >= 10:
                complex_elements += 1
    
    if len(woorden) >= 15:
        complex_elements += 1
    
    score = complex_elements / total_elements * 100
    print(round(score, 1))
    
complexity_score("ik ben Demianarrias een superleukee jongen uit stadskanaal bla bla bla bla bla bla bla. en jij bent een chigganigga.") 











    
    