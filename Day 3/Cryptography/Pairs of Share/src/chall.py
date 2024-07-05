from Crypto.Util.number import *

FLAG = bytes_to_long(b"SELEKDA{FAKEFLAG}")


def prime_gen():
	return getPrime(1024), getPrime(1024), getPrime(1024), getPrime(1024), getPrime(1024), getPrime(1024)
r, s, t, u, v, w = prime_gen()
n = r * t
e = 17

m = FLAG ^ (FLAG >> 1)

brother = s * m + u
sister = v * m + w

part_1 = pow(brother,e,n)
part_2 = pow(sister,e,n)


print("n = ", str(n))
print("part_1 = ", str(part_1))
print("part_2 =", str(part_2))
print("s = ", str(s))
print("u = ", str(u))
print("v = ", str(v))
print("w = ", str(w))