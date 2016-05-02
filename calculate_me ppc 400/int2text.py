import sys, calc

_nums = (
    '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
    'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
    'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

_tens = (
    'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty',
    'Ninety')

def int2text(number):
    """Converts an integer to the English language name of that integer.
    
    E.g. converts 1 to "One". Supports numbers 0 to 999999.
    This can be used in LilyPond identifiers (that do not support digits).
    
    """
    result = []
    if number >= 10**9:
        billions, number = divmod(number, 10**9)
        if number:
            result.append(int2text(billions) + " " + "Billion" + " ")
        else:
            result.append(int2text(billions) + " " + "Billion")
    
    if number >= 10**6:
        millions, number = divmod(number, 10**6)
        if number:
            result.append(int2text(millions) + " " + "Million" + " ")
        else:
            result.append(int2text(millions) + " " + "Million")
    
    if number >= 10**3:
        hundreds, number = divmod(number, 10**3)
        if number:
            result.append(int2text(hundreds) + " " + "Thousand" + " ")
        else:
            result.append(int2text(hundreds) + " " + "Thousand")
    
    if number >= 100:
        tens, number = divmod(number, 100)
        if number:
            result.append(_nums[tens] + " " + "Hundred" + " ")
        else:
            result.append(_nums[tens] + " " + "Hundred")
    if number < 20:
        result.append(_nums[number])
    else:
        tens, number = divmod(number, 10)
        if _nums[number]:
            result.append(_tens[tens-2] + " " + _nums[number])
        else:
            result.append(_tens[tens-2])
    text = "".join(result)
    return text or 'Zero'

if __name__ == "__main__":
    number = int(sys.argv[1])
    strnumber = int2text(number)
    print strnumber
    print calc.text2int(strnumber)