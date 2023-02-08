def dec_to_base64(dec_val):

    try:
        dec_val = int(dec_val)
        if dec_val == 0:
            return 'A'
        elif dec_val == 1:
            return 'B'
        elif dec_val == 2:
            return 'C'
        elif dec_val == 3:
            return 'D'
        elif dec_val == 4:
            return 'E'
        elif dec_val == 5:
            return 'F'
        elif dec_val == 6:
            return 'G'
        elif dec_val == 7:
            return 'H'
        elif dec_val == 8:
            return 'I'
        elif dec_val == 9:
            return 'J'
        elif dec_val == 10:
            return 'K'
        elif dec_val == 11:
            return 'L'
        elif dec_val == 12:
            return 'M'
        elif dec_val == 13:
            return 'N'
        elif dec_val == 14:
            return 'O'
        elif dec_val == 15:
            return 'P'
        elif dec_val == 16:
            return 'Q'
        elif dec_val == 17:
            return 'R'
        elif dec_val == 18:
            return 'S'
        elif dec_val == 19:
            return 'T'
        elif dec_val == 20:
            return 'U'
        elif dec_val == 21:
            return 'V'
        elif dec_val == 22:
            return 'W'
        elif dec_val == 23:
            return 'X'
        elif dec_val == 24:
            return 'Y'
        elif dec_val == 25:
            return 'Z'
        elif dec_val == 26:
            return 'a'
        elif dec_val == 27:
            return 'b'
        elif dec_val == 28:
            return 'c'
        elif dec_val == 29:
            return 'd'
        elif dec_val == 30:
            return 'e'
        elif dec_val == 31:
            return 'f'
        elif dec_val == 32:
            return 'g'
        elif dec_val == 33:
            return 'h'
        elif dec_val == 34:
            return 'i'
        elif dec_val == 35:
            return 'j'
        elif dec_val == 36:
            return 'k'
        elif dec_val == 37:
            return 'l'
        elif dec_val == 38:
            return 'm'
        elif dec_val == 39:
            return 'n'
        elif dec_val == 40:
            return 'o'
        elif dec_val == 41:
            return 'p'
        elif dec_val == 42:
            return 'q'
        elif dec_val == 43:
            return 'r'
        elif dec_val == 44:
            return 's'
        elif dec_val == 45:
            return 't'
        elif dec_val == 46:
            return 'u'
        elif dec_val == 47:
            return 'v'
        elif dec_val == 48:
            return 'w'
        elif dec_val == 49:
            return 'x'
        elif dec_val == 50:
            return 'y'
        elif dec_val == 51:
            return 'z'
        elif dec_val == 52:
            return '0'
        elif dec_val == 53:
            return '1'
        elif dec_val == 54:
            return '2'
        elif dec_val == 55:
            return '3'
        elif dec_val == 56:
            return '4'
        elif dec_val == 57:
            return '5'
        elif dec_val == 58:
            return '6'
        elif dec_val == 59:
            return '7'
        elif dec_val == 60:
            return '8'
        elif dec_val == 61:
            return '9'
        elif dec_val == 62:
            return '+'
        elif dec_val == 63:
            return '/'
        else:
            raise ValueError
    except ValueError:
        print("Value is not integer")
