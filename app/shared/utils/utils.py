from uuid import uuid4


def generate_id():
    return uuid4().int >> 104


def to_base62(num):
    base62chars = list(str(c) for c in range(10))
    base62chars = base62chars + list(chr(c) for c in range(97, 123))
    base62chars = base62chars + list(chr(c) for c in range(65, 91))
    converted = ""
    while num // 62 != 0:
        remainder = num % 62
        converted += base62chars[remainder]
        num = num // 62
    converted += base62chars[num % 62]
    return converted[::-1]


def from_base62(hash):
    base62chars = list(str(c) for c in range(10))
    base62chars = base62chars + list(chr(c) for c in range(97, 123))
    base62chars = base62chars + list(chr(c) for c in range(65, 91))
    length = len(hash)
    key = 0
    for i in range(0, length):
        char = hash[length - 1 - i]
        if not (char.isalpha() or char.isdigit()):
            return -1
        num = base62chars.index(char)
        key += num * (62**i)
    return key
