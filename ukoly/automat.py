def analyzuj(text):
    # Množiny přídavných jmen
    negativni = {'slozity', 'narocny', 'tezky', 'neprijemny', 'otravny', 'nudny'}
    pozitivni = {'jednoduchy', 'lehky', 'zabavny', 'obohacujici', 'trivialni', 'snadny'}

    slova = text.lower().rstrip('.').split()

    if len(slova) < 2:
        return None

    sloveso_index = -1
    for i, slovo in enumerate(slova):
        if slovo in {'je', 'neni'}:
            sloveso_index = i
            break

    if sloveso_index == -1:
        return None

    pridavne_jmeno = slova[-1]

    if pridavne_jmeno not in negativni and pridavne_jmeno not in pozitivni:
        return None

    ma_moc = slova[-2] == 'moc' if len(slova) >= 2 else False

    je_negativni = slova[sloveso_index] == 'neni'
    je_pozitivni = pridavne_jmeno in pozitivni

    if ma_moc:
        if (je_pozitivni and not je_negativni) or (not je_pozitivni and je_negativni):
            return ':-O'

    if (je_pozitivni and not je_negativni) or (not je_pozitivni and je_negativni):
        if 'zpr' in slova[:sloveso_index]:
            return ';-)'
        return ':-)'
    else:
        return ':-('
