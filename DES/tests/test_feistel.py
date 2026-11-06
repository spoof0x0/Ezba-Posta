from src.feistel import *

right_half = "F0AAF0AA"
round_key = "1B02EFFC7072"

right_binary = bin(int(right_half, 16))[2:].zfill(32)
key_binary = bin(int(round_key, 16))[2:].zfill(48)

result = feistel_function(right_binary, key_binary)

assert hex(int(result, 2))[2:].upper().zfill(8) == "234AA9BB"

print("Feistel function passed validation!")

