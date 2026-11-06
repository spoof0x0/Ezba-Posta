from src.tables import IP, FP, PC1, PC2, E, P, S_BOXES, SHIFTS

assert len(IP) == 64 and all(1 <= x <= 64 for x in IP)
assert len(FP) == 64 and all(1 <= x <= 64 for x in FP)
assert len(PC1) == 56 and all(1 <= x <= 64 for x in PC1)
assert len(PC2) == 48 and all(1 <= x <= 56 for x in PC2)
assert len(E) == 48 and all(1 <= x <= 32 for x in E)
assert len(P) == 32 and all(1 <= x <= 32 for x in P)
assert len(SHIFTS) == 16

assert len(S_BOXES) == 8
for box in S_BOXES:
    assert len(box) == 4
    for row in box:
        assert len(row) == 16
        assert all(0 <= x <= 15 for x in row)

print("All DES tables passed validation!")