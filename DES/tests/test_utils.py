from src.utils import *

assert permute("101100", [6, 1, 3]) == "011"


assert xor("1010", "1100") == "0110"
assert xor("101100", "110010") == "011110"
assert xor("0000", "0000") == "0000"
assert xor("1111", "1111") == "0000"



assert left_shift("101100", 1) == "011001"
assert left_shift("101100", 2) == "110010"
assert left_shift("101100", 0) == "101100"

print("All utils functions passed validation!")