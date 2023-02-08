def binary_to_dec(bin_val):

    try:
        value = str(bin_val)
        power = int(0)
        dec_val = int(0)
        for i in reversed(value):
            if i == '1':
                dec_val += 2**power
            power += 1
        return dec_val
    except ValueError:
        print("value error")
