from Crypto.Util.number import long_to_bytes, inverse
from pwn import *

conn = process(['python3', 'chall.py'])
flag_ct = conn.recvuntil(b'\n')
flag_ct = int(flag_ct[len('ct = '):].strip().decode())
print(f'{flag_ct = }')

a = -1
conn.sendlineafter(b'>> ', str(a).encode())
ct = conn.recvuntil(b'\n')
ct = int(ct[len('ct = '):].strip().decode())
n = ct + 1
print(f'{n = }')

a = 2
conn.sendlineafter(b'>> ', str(a).encode())
ct = conn.recvuntil(b'\n')
ct = int(ct[len('ct = '):].strip().decode())
print(f'{ct = }')

p, q = factor(n)
p = p[0]
q = q[0]
print(f'{p = }')
print(f'{q = }')
assert p * q == n

R = GF(min(p, q))
e = R(ct).log(R(a))
print(f'{e = }')

d = inverse(e, (p-1)*(q-1))
print(f'{d = }')

m = pow(flag_ct, d, n)
print(f'{m = }')
print(f'{long_to_bytes(m) = }')