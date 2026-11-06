"""
اختبار DES باستخدام NBS SP 500-20 test vectors.

الاستخدام (من فولدر المشروع DES):
    1) حط الملفين test_nbs_vectors.py و nbs_vectors.txt جوه فولدر tests/
    2) python tests/test_nbs_vectors.py
       أو لو الـ vectors في مكان تاني:
       python tests/test_nbs_vectors.py path/to/vectors.txt

صيغة كل سطر في الملف:  KEY  INPUT  EXPECTED_OUTPUT
والسطر "encrypt" / "decrypt" بيحدد العملية للأسطر اللي بعده.
دوالك ترتيبها (النص، المفتاح) وبتاخد hex strings.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
for p in (ROOT, HERE):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from src.des import des_encrypt, des_decrypt
except ImportError:
    from src.des import des_encrypt, des_decrypt

DEFAULT_VECTORS = os.path.join(HERE, "nbs_vectors.txt")

HINTS = {
    "Initial Permutation": "جدول IP أو جدول E (expansion) أو ترتيب البتات في أول/آخر الجولات",
    "Inverse Permutation": "جدول FP (IP^-1) أو الـ swap بين left/right بعد الجولة 16",
    "Key Permutation": "جدول PC-1 / PC-2 أو عدد الـ left shifts في الـ key schedule",
    "right-shifts": "ترتيب الـ subkeys في الـ decrypt (لازم K16..K1) أو الـ key schedule",
    "Data permutation": "جدول P أو جدول E",
    "S-Box": "واحد من الـ S-boxes فيه رقم غلط أو ترتيب الصفوف/الأعمدة غلط",
}

SKIP_PREFIXES = (
    "Test vectors", "implementation", '"Validating', "Implementations", "NBS", "Errors",
)


def norm(out) -> str:
    """يحوّل ناتج دالتك لـ 16 hex حروف كبيرة."""
    if isinstance(out, (bytes, bytearray)):
        return bytes(out).hex().upper()
    if isinstance(out, int):
        return f"{out:016X}"
    s = str(out).strip().replace(" ", "")
    if s.lower().startswith("0x"):
        s = s[2:]
    if len(s) == 64 and set(s) <= {"0", "1"}:
        return f"{int(s, 2):016X}"
    return s.upper().zfill(16)


def load(path):
    """يرجّع قايمة: (section, mode, key, input, expected)"""
    mode, section, rows = None, "?", []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith("#"):
                t = line.lstrip("# ").strip()
                if t and not t.startswith(SKIP_PREFIXES):
                    section = t
                continue
            if line in ("encrypt", "decrypt"):
                mode = line
                continue
            parts = line.split()
            if len(parts) == 3 and mode:
                k, i, o = (x.upper() for x in parts)
                rows.append((section, mode, k, i, o))
    return rows


def hint_for(section):
    for key, text in HINTS.items():
        if key.lower() in section.lower():
            return text
    return ""


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_VECTORS
    if not os.path.exists(path):
        sys.exit(f"ملف الـ vectors مش موجود: {path}")

    rows = load(path)
    sections = {}
    for section, mode, k, i, o in rows:
        sections.setdefault((section, mode), []).append((k, i, o))

    total = failed_total = 0
    for (section, mode), items in sections.items():
        fails = []
        for k, i, o in items:
            try:
                fn = des_encrypt if mode == "encrypt" else des_decrypt
                got = norm(fn(i, k))  # (النص/الشفرة، المفتاح)
            except Exception as e:  # noqa: BLE001
                got = f"EXCEPTION: {type(e).__name__}: {e}"
            if got != o:
                fails.append((k, i, o, got))
        total += len(items)
        failed_total += len(fails)

        status = "PASS" if not fails else "FAIL"
        print(f"[{status}] {mode:7s} {section}: {len(items) - len(fails)}/{len(items)}")
        for k, i, o, got in fails[:3]:
            print(f"        key={k} in={i}")
            print(f"        expected={o}")
            print(f"        got     ={got}")
        if len(fails) > 3:
            print(f"        ... و {len(fails) - 3} حالات تانية فاشلة")
        if fails and hint_for(section):
            print(f"        احتمال المشكلة: {hint_for(section)}")

    print()
    print(f"TOTAL: {total - failed_total}/{total} PASSED!")
    sys.exit(1 if failed_total else 0)


if __name__ == "__main__":
    main()
