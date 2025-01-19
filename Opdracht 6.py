def complexity_score(text):
    """
    Het is jouw taak om een functie complexity_score(text) te schrijven die een string text als parameter accepteert en als 
    resultaat een score (float) teruggeeft. De string text kan meerdere zinnen bevatten.
    """
    
    complex_elements = 0
    zin = 0
    total_elements = 0
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
    total_elements += zin 
    
    score = complex_elements / total_elements * 100
    return score
    
assert round(complexity_score("Dit is een korte zin."), 1) == 0.0
assert round(complexity_score("Dit is een gecompliceerde zin met veel verschillende woorden erin verstopt."),1,) == 16.7
assert round(complexity_score("De intelligentie van computerprogramma's neemt toe."), 1) == 28.6
assert round(complexity_score("Programmeren is leuk. Dit is een zeer lange zin die meer dan vijftien woorden bevat en daarom als complex wordt beschouwd bij deze analyse. Nog een zin."),1,)== 6.7










    
    