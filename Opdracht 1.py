def check_extension(s, e):

    if len(e) == 0:
        return True
    elif len(s) == 0:
        return False
    elif s[-1] != e[-1]:
        return False
    else:
        return check_extension(s[:-1], e[:-1])
    
assert check_extension("tentamen.docx", ".exe") == False
assert check_extension("program.exe", ".exe") == True
assert check_extension("wk8ex1.py", ".py") == True