from src.utils import *
from src.tables import *
from src.key_schedule import *
from src.feistel import *


def des_encrypt(plaintext, key):
    plaintext_binary = bin(int(plaintext, 16))[2:].zfill(64)
    permuted_plaintext = permute(plaintext_binary, IP)
    left = permuted_plaintext[:32]
    right = permuted_plaintext[32:64]

    subkeys = generate_subkeys(key)

    for i in range(16):
        left, right = feistel_round(left, right, subkeys[i])

    combined = right + left    
    ciphertext_binary = permute(combined, FP)
    ciphertext = hex(int(ciphertext_binary, 2))[2:].upper().zfill(16)
    return ciphertext



def des_decrypt(ciphertext, key):
    ciphertext_binary = bin(int(ciphertext, 16))[2:].zfill(64)
    permuted_ciphertext = permute(ciphertext_binary, IP)
    left = permuted_ciphertext[:32]
    right = permuted_ciphertext[32:64]

    subkeys = generate_subkeys(key)

    for i in range(15, -1, -1):
        left, right = feistel_round(left, right, subkeys[i])

    combined = right + left    
    plaintext_binary = permute(combined, FP)
    plaintext = hex(int(plaintext_binary, 2))[2:].upper().zfill(16)
    return plaintext
