from src.key_schedule import *


key = "133457799BBCDFF1"

subkeys = generate_subkeys(key)

assert len(subkeys) == 16
assert all(len(k) == 48 for k in subkeys)

assert hex(int(subkeys[0], 2))[2:].upper().zfill(12) == "1B02EFFC7072"
assert hex(int(subkeys[-1], 2))[2:].upper().zfill(12) == "CB3D8B0E17F5"

print("All 16 DES Subkeys passed validation!")