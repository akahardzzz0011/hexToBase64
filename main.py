from hexToBinary import hex_to_binary
from binaryToDec import binary_to_dec
from decToBase64 import dec_to_base64


while True:
    hexadecimal = input("Enter hexadecimal value to be converted to base64:\n\n")
    if len(hexadecimal) % 2 == 0:
        break
    else:
        print("Input must be hexadecimal string")
binary_val = str()
for i in hexadecimal:
    binary_val += str(hex_to_binary(i))

binary_mod = len(binary_val) % 6
if binary_mod != 0:
    pas = str()
    zeros_to_add = 6 - binary_mod
    if zeros_to_add == 4:
        pas = '=='
    if zeros_to_add == 2:
        pas = '='
    for i in range(zeros_to_add):
        binary_val += '0'
i = 0
hex_val = str()
while i < (len(binary_val)):
    dec_val = binary_to_dec(binary_val[i:i+6])
    hex_val += dec_to_base64(dec_val)
    i += 6
if binary_mod != 0:
    hex_val += pas
print(hex_val)
