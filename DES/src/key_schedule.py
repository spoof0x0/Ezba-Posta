from src.utils import *
from src.tables import *


def generate_subkeys(key):
    key = bin(int(key, 16))[2:].zfill(64)
    permuted_key = permute(key, PC1)
    left_half = permuted_key[:28]
    right_half = permuted_key[28:]

    subkeys = []
    for i in range(16):
        left_half = left_shift(left_half, SHIFTS[i])
        right_half = left_shift(right_half, SHIFTS[i])
        combined_key = left_half + right_half
        subkey = permute(combined_key, PC2)
        subkeys.append(subkey)

    return subkeys

    