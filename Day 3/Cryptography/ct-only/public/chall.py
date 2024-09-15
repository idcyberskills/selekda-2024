from Crypto.Util.number import getPrime, bytes_to_long

p = getPrime(128)
q = getPrime(128)
n = p * q
e = getPrime(80)

m = bytes_to_long(open('flag.txt', 'rb').read())
assert m < n

ct = pow(m, e, n)
print(f'{ct = }')

while True:
    m = int(input('>> '))
    ct = pow(m, e, n)
    print(f'{ct = }')