def hex_to_binary(value):

    try:
        value = int(value)
        if value == 0:
            return '0000'
        elif value == 1:
            return '0001'
        elif value == 2:
            return '0010'
        elif value == 3:
            return '0011'
        elif value == 4:
            return '0100'
        elif value == 5:
            return '0101'
        elif value == 6:
            return '0110'
        elif value == 7:
            return '0111'
        elif value == 8:
            return '1000'
        elif value == 9:
            return '1001'
        else:
            raise ValueError
    except ValueError:
        value = value.lower()
        if value == 'a':
            return '1010'
        elif value == 'b':
            return '1011'
        elif value == 'c':
            return '1100'
        elif value == 'd':
            return '1101'
        elif value == 'e':
            return '1110'
        elif value == 'f':
            return '1111'
        else:
            raise ValueError("Input must be in hexadecimal form")
