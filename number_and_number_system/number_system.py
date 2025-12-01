# DEX 1024
dec_count = (4 * 10**0) + (2 * 10**1) + (0 * 10**2) + (1 * 10**3)
# 4 + 20 + 0 + 1000 =  1024


# DEC 57 to BIN

first_number, remainder_from_division = divmod(57, 2)  # (28, 1)
second_number, second_remainder_from_division = divmod(first_number, 2)  # (14, 0)
third_number, third_remainder_from_division = divmod(second_number, 2) # (7, 0)
fourth_number, fourth_remainder_from_division = divmod(third_number, 2) # (3, 1)
fifth_number, fifth_remainder_from_division = divmod(fourth_number, 2)  # (1, 1)


bin_number = 111001

# BIN 111001 to DEX

bin_to_dec = (1 * 2**0) + (0 * 2**1) + (0 * 2**2) + (1 * 2**3) + (1 * 2**4) + (1 * 2**5)
print(bin_to_dec)


