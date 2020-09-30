
def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    key = {}
    cnt = 0

    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1

    return key


def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey


def encrypt(key, message):
    cipher = ''
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


key = generate_key(3)

message = 'You are awesome'.upper()
cipher = encrypt(key, message)
print(cipher)

# dkey = get_decryption_key(key)
# message = encrypt(dkey, cipher)
# print(message)

# Kerckhoff's principle
# Only 26 keys, simple to break
# Crypto rule 1: Should not be able to break the cipher even if you know the algorithm

# Breaking the cipher
for i in range(len(key)):
    dkey = generate_key(i)
    message = encrypt(dkey, cipher)
    print(message)
