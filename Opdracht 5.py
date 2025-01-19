def alfabet_words(s):
    """
    Schrijf de functie alfabet_word(s) die een string s accepteert (een woord) en als resultaat True teruggeeft indien de letters in alfabetische volgorde staan en anders False.
    Maak gebruik van recursie. Je mag geen gebruik maken van list comprehension of lusconstructies.
    """

    if len(s) == 1:
        return True
    elif len(s) == 0:
        return False 
    elif s[0] <= s[1]:
        return alfabet_words(s[1:])
    else:
        return False
    
assert alfabet_words("nigga") == False
assert alfabet_words("abcde") == True
assert alfabet_words("baba") == False
assert alfabet_words("") == False
