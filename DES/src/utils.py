

def permute(block, table):
    result = ""
    for i in table:
        result += block[i - 1]
    return result


def xor(a, b):
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result


def left_shift(block, n):
    return block[n:] + block[:n]


