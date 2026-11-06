

from src.des import *

plaintext = "0123456789ABCDEF"
key = "133457799BBCDFF1"

ciphertext = des_encrypt(plaintext, key)

assert ciphertext == "85E813540F0AB405"



plaintext = "0123456789ABCDEF"
key = "133457799BBCDFF1"
expected = "85E813540F0AB405"

result = des_encrypt(plaintext, key)

assert result == expected, f"Expected {expected}, got {result}"


print("DES Encryption Test Passed!")





# Test DES decryption
plaintext = "0123456789ABCDEF"
key = "133457799BBCDFF1"
ciphertext = des_encrypt(plaintext, key)
decrypted_text = des_decrypt(ciphertext, key)

assert decrypted_text == plaintext, f"Expected {plaintext}, got {decrypted_text}"



ciphertext = "85E813540F0AB405"
key = "133457799BBCDFF1"

plaintext = des_decrypt(ciphertext, key)

assert plaintext == "0123456789ABCDEF"


key = "133457799BBCDFF1"

plaintexts = [
    "0123456789ABCDEF",
    "0000000000000000",
    "FFFFFFFFFFFFFFFF",
    "1234567890ABCDEF",
    "AABBCCDDEEFF0011"
]

for plaintext in plaintexts:
    ciphertext = des_encrypt(plaintext, key)
    decrypted = des_decrypt(ciphertext, key)

    assert decrypted == plaintext, f"Round-trip failed for plaintext {plaintext}: got {decrypted}"




key = "133457799BBCDFF1"

test_vectors = [
    ("0123456789ABCDEF", "85E813540F0AB405"),
]

for plaintext, expected in test_vectors:
    result = des_encrypt(plaintext, key)

    assert result == expected, (
        f"Failed for {plaintext}: "
        f"expected {expected}, got {result}"
    )



test_vectors = [
        ("7CA110454A1A6E57", "01A1D6D039776742", "690F5B0D9A26939B"),
        ("0131D9619DC1376E", "5CD54CA83DEF57DA", "7A389D10354BD271"),
        ("07A1133E4A0B2686", "0248D43806F67172", "868EBB51CAB4599A"),
        ("3849674C2602319E", "51454B582DDF440A", "7178876E01F19B2A"),
        ("04B915BA43FEB5B6", "42FD443059577FA2", "AF37FB421F8C4095"),
        ("0113B970FD34F2CE", "059B5E0851CF143A", "86A560F10EC6D85B"),
        ("0170F175468FB5E6", "0756D8E0774761D2", "0CD3DA020021DC09"),
        ("43297FAD38E373FE", "762514B829BF486A", "EA676B2CB7DB2B7A"),
        ("07A7137045DA2A16", "3BDD119049372802", "DFD64A815CAF1A0F"),
        ("04689104C2FD3B2F", "26955F6835AF609A", "5C513C9C4886C088"),
        ("37D06BB516CB7546", "164D5E404F275232", "0A2AEEAE3FF4AB77"),
        ("1F08260D1AC2465E", "6B056E18759F5CCA", "EF1BF03E5DFA575A"),
        ("584023641ABA6176", "004BD6EF09176062", "88BF0DB6D70DEE56"),
        ("025816164629B007", "480D39006EE762F2", "A1F9915541020B56"),
        ("49793EBC79B3258F", "437540C8698F3CFA", "6FBF1CAFCFFD0556"),
        ("4FB05E1515AB73A7", "072D43A077075292", "2F22E49BAB7CA1AC"),
        ("49E95D6D4CA229BF", "02FE55778117F12A", "5A6B612CC26CCE4A"),
        ("018310DC409B26D6", "1D9D5C5018F728C2", "5F4C038ED12B2E41"),
        ("1C587F1C13924FEF", "305532286D6F295A", "63FAC0D034D9F793"),
    ]

for key, plaintext, expected in test_vectors:
    result = des_encrypt(plaintext, key)

    assert result == expected, (
        f"Failed for key={key}, plaintext={plaintext}: "
        f"expected {expected}, got {result}"
    )


print("DES Decryption Test Passed!")