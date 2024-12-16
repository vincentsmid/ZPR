from fractions import Fraction

def normalize_polynomial(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    if len(poly) == 1 and poly[0] == 0:
        return [0]
    return poly

def polynomial_division(dividend, divisor):
    dividend = [Fraction(x) for x in dividend]
    divisor = [Fraction(x) for x in divisor]

    # Normalize inputs
    dividend = normalize_polynomial(dividend[:])
    divisor = normalize_polynomial(divisor[:])

    if len(divisor) == 1 and divisor[0] == 0:
        raise ValueError("Division by zero")

    if len(dividend) < len(divisor):
        return [0], dividend

    result = [Fraction(0)] * (len(dividend) - len(divisor) + 1)
    remainder = dividend[:]

    for i in range(len(dividend) - len(divisor), -1, -1):
        if len(remainder) <= i + len(divisor) - 1:
            continue

        coef = remainder[i + len(divisor) - 1] / divisor[-1]
        result[i] = coef

        for j in range(len(divisor)):
            remainder[i + j] -= coef * divisor[j]

    result = [int(x) for x in normalize_polynomial(result)]
    remainder = [int(x) for x in normalize_polynomial(remainder[:len(divisor)-1])]

    if not remainder:
        remainder = [0]

    return result, remainder

def vypocet_python(data):
    prvni = data['prvni']
    druhy = data['druhy']

    vysledek, zbytek = polynomial_division(prvni, druhy)

    return {
        'vysledek': vysledek,
        'zbytek': zbytek
    }

def vypocet_numpy(data):
    import numpy as np
    from fractions import Fraction

    prvni = np.array([Fraction(x) for x in data['prvni']])
    druhy = np.array([Fraction(x) for x in data['druhy']])

    quotient, remainder = np.polydiv(prvni, druhy)

    vysledek = [int(x) for x in quotient]
    zbytek = [int(x) for x in remainder]

    # Normaize results
    vysledek = normalize_polynomial(vysledek)
    zbytek = normalize_polynomial(zbytek)

    if not zbytek:
        zbytek = [0]

    return {
        'vysledek': vysledek,
        'zbytek': zbytek
    }
