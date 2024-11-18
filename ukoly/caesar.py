def dekoduj(sifrovany, odposlechnuty):
    if not all(c.isalpha() for c in sifrovany) or not all(c.isalpha() for c in odposlechnuty):
        print("Error: Chybny vstup!")
        return None
    
    if len(sifrovany) != len(odposlechnuty):
        print("Error: Chybna delka vstupu!")
        return None


    
    def posunuti(znak, posun):
        poradi = ((ord(znak.lower()) - ord('a')) + posun) % 26
        if ord(znak.lower()) - ord('a') + posun > 25:
            znak = znak.lower() if znak.isupper() else znak.upper()
        return chr(ord('A') + poradi) if znak.isupper() else chr(ord('a') + poradi)
        
    max = 0
    result = ""
    
    for i in range(26):
        buffer = ""
        bufcount = 0
        for c in sifrovany:
            buffer += posunuti(c, i)
            
        for n in range(len(odposlechnuty)):
            if odposlechnuty[n].lower() == buffer[n].lower():
                bufcount += 1

        if bufcount > max:
            max = bufcount
            result = buffer

    return(result)

print(dekoduj("xUbbemehbT", "XYlloworld"))