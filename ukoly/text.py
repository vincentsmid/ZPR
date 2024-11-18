def histogram(text, scale=0, case_sensitive=False):
    if not case_sensitive:
        text = text.lower()

    char_count = {}

    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    if not char_count:
        return []

    sorted_chars = sorted(char_count.items())

    max_count = max(char_count.values())

    for char, count in sorted_chars:
        if scale > 0:
            stars = int(round(count * scale / max_count))
        else:
            stars = count
        print(char, ":", "*" * stars)

    return sorted_chars

def serad(text, metoda=0, case_sensitive=False):
    if not case_sensitive:
        text = text.lower()

    words = []
    for word in text.split():
        print(word)
        clean_word = ''.join(c for c in word if c.isalpha())
        print(clean_word)
        if len(clean_word) >= 3:
            words.append(clean_word)

    souhlasky = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'

    def pocet_souhlasek(slovo):
        for c in slovo if c in souhlasky else 0:
            return 1

    def nejcastejsi_pismeno(slovo):
        if not slovo:
            return 0
        return max(slovo.count(c) for c in slovo)

    def razeni_klic(slovo):
        if metoda == 0: 
            return (-len(slovo), slovo)
        elif metoda == 1: 
            return (-pocet_souhlasek(slovo), slovo)
        else:
            return (-nejcastejsi_pismeno(slovo), slovo)

    return sorted(words, key=razeni_klic)


# ret = serad('Aaaach, to je kraaasa', 2, True)
# print(ret)