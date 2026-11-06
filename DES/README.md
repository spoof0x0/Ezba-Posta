# Data Encryption Standard (DES)

A Python implementation of the Data Encryption Standard (DES) algorithm from scratch, as part of the Ezba-Posta project.

## Overview

DES is a symmetric-key block cipher based on a 16-round Feistel network.

- **Block Size:** 64 bits
- **Key Input Size:** 64 bits
- **Effective Key Size:** 56 bits
- **Number of Rounds:** 16
- **Structure:** Feistel Network

The implementation supports both encryption and decryption using hexadecimal inputs.

## Implementation

The implementation is divided into modules:

| File | Description |
|---|---|
| `src/des.py` | Main DES encryption and decryption functions. |
| `src/feistel.py` | Expansion, S-Box substitution, P permutation, and Feistel round. |
| `src/key_schedule.py` | Generates the 16 round subkeys. |
| `src/tables.py` | Standard DES permutation tables, S-Boxes, and shift schedule. |
| `src/utils.py` | Binary permutation, XOR, and circular left-shift utilities. |

## Project Structure

```text
DES/
├── src/
│   ├── des.py
│   ├── feistel.py
│   ├── key_schedule.py
│   ├── tables.py
│   └── utils.py
│
└── tests/
    ├── nbs_vectors.txt
    ├── test_des.py
    ├── test_feistel.py
    ├── test_key_schedule.py
    ├── test_nbs_vectors.py
    ├── test_tables.py
    └── test_utils.py
```

## Usage

Run commands from the `DES` directory.

### Encryption

```python
from src.des import des_encrypt

plaintext = "0123456789ABCDEF"
key = "133457799BBCDFF1"

ciphertext = des_encrypt(plaintext, key)

print(ciphertext)
# 85E813540F0AB405
```

### Decryption

```python
from src.des import des_decrypt

plaintext = des_decrypt(
    "85E813540F0AB405",
    "133457799BBCDFF1"
)

print(plaintext)
# 0123456789ABCDEF
```

## Testing & Validation

The implementation was validated using test vectors from:

**NBS Special Publication 500-20 (1980)**  
*Validating the Correctness of Hardware Implementations of the NBS Data Encryption Standard.*

### Test Results

All 291 test cases passed successfully.

| Test Category | Passed |
|---|---:|
| Initial Permutation & Expansion | 64/64 |
| Inverse Permutation & Expansion | 64/64 |
| Key Permutation | 56/56 |
| Decryption Right Shifts | 56/56 |
| Data Permutation | 32/32 |
| S-Box Tests | 19/19 |
| **Total** | **291/291** |

### Run the NBS Tests

```bash
python -m tests.test_nbs_vectors
```

Run the complete test modules:

```bash
python -m tests.test_tables
python -m tests.test_utils
python -m tests.test_key_schedule
python -m tests.test_feistel
python -m tests.test_des
python -m tests.test_nbs_vectors
```

## Security Disclaimer

DES is obsolete and vulnerable to brute-force attacks due to its small 56-bit effective key size.

This implementation is intended strictly for educational purposes and should not be used for real-world security.

## References

- *Understanding Cryptography*, Christof Paar, Jan Pelzl, and Tim Güneysu.
- NBS Special Publication 500-20 (1980).