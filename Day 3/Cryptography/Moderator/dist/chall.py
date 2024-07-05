from Crypto.Util.number import *
import random, os

random.seed(os.urandom(32))
a = getPrime(512)
b = (a - 1) * getPrime(128)
c, d = random.getrandbits(256), random.getrandbits(16)
k_n = 0x1000

# will censor the secrets with underscores
FLAG = bytes_to_long(b"SELEKDA{____________________________________________}")
known = (FLAG * k_n + d) % (a * b + c)
print(known)

# known = 57720533142139524850814247226490249306950466420274898800535525736030828621732591196013029362824092685473312318654493519281832593893