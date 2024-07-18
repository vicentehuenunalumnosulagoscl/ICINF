def solo_numeros(var):
    if not var:
      return False

    for char in var:
        if char < '0' or char > '9':
            return False 
    return True 

print(solo_numeros("12345"))
print(solo_numeros("123c5"))
print(solo_numeros(""))
