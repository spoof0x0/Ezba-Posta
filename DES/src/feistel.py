from src.utils import *
from src.tables import *





def expansion(right_half):
    expanded_half = permute(right_half, E)
    return expanded_half




def feistel_function(right_half, round_key):
    expanded_half = expansion(right_half)
    xored_half = xor(expanded_half, round_key)
    substituted_half = ""
    for i in range(8):
        row = int(xored_half[i * 6] + xored_half[i * 6 + 5], 2)
        col = int(xored_half[i * 6 + 1:i * 6 + 5], 2)
        sbox_value = S_BOXES[i][row][col]
        substituted_half += bin(sbox_value)[2:].zfill(4)

    permuted_half = permute(substituted_half, P)
    return permuted_half


def feistel_round(left, right, round_key):
    new_left = right
    new_right = xor(left, feistel_function(right, round_key))
    return new_left, new_right

