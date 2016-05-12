import sys, calc

_roman_numerals = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5),
("IV", 4), ("I", 1))

def int2roman(n):
    """Convert an integer value to a roman number string.
    
    E.g. 1 -> "I", 12 -> "XII", 2015 -> "MMXV"
    
    n has to be > 1.
    
    """
    if n < 1:
        raise ValueError('Roman numerals must be positive integers, got %s' % n)
    roman = []
    for ltr, num in _roman_numerals:
        k, n = divmod(n, num)
        roman.append(ltr * k)
    return "".join(roman)

if __name__ == "__main__":
    number = int(sys.argv[1])
    romannumber = int2roman(number)
    print romannumber
    print calc.roman2int(romannumber)