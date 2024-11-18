def funkce_1(width):
    if width < 3 or width > 19 or width % 2 == 0:
        return 1
    
    print('$' + '-' * (width - 2) + '$')
    
    for i in range(width-1):
        if i <= width // 2:
            blank = i + 1
            x = width - 2 * i - 2
        else:
            blank = width - i - 1
            x = 2 * i - width + 2
        
        if x > 0:
            print(" " * blank + "x" * x + " " * blank)

    print("$" + "-" * (width - 2) + "$")
    return 0


def olovnicething(width, step):
    if step == 1:
        rangearg = (0, width // 2, step)
    else:
        rangearg = (width // 2 - 1, -1, step)

    for i in range(*rangearg):
        blank = width // 2 - 1 - i
        at_symbol = width // 3 + 2 * i
        print(" " * blank + "@" * at_symbol + " " * blank)

def funkce_2(width, height):
    if width < 3 or width > 19 or width % 2 == 0:
        return 1
    
    if height >= width:
        return 2

    print(" " * ((width - 1) // 2) + "o" + " " * (width -2))
    
    olovnicething(width, 1)

    for bambam in range(height):
        print("@" + (width - 2) * "x" + "@")

    olovnicething(width, -1)
    print(" " * ((width - 1) // 2) + "o" + " " * (width -2))

    return 0


def funkce_3(width, height, fillchar):
    if width < 3 or width > 19 or width % 2 == 0:
        return 1

    if height >= width:
        return 2

    if not (ord("a") <= ord(fillchar) <= ord("z")):
        return 3

    for i in range(width // 2 + 1):
        blank = " " * (width // 2 - i)
        kawaii = "^" * (2 * i + 1)
        print(blank + kawaii)

    for nyoooom in range(height):
        print("|" + fillchar * (width - 2) + "|")

    return 0
