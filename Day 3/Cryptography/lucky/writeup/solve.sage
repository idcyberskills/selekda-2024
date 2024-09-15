from pwn import *

conn = process(['python3', 'chall.py'])

x = []
for _ in range(1000):
    conn.sendlineafter(b'>> ', b'?')
    res = conn.recvuntil(b'\n').strip().split()
    x.append(int(res[1].decode()))
    if res[0] == b'lucky':
        break

assert len(x) >= 20

x_0 = x[-1]
x.pop()

n = 19
matrix_array = [[1] + x[:n]]
for i in range(n):
    tmp = [0 for _ in range(n + 1)]
    tmp[1 + i] = x_0
    matrix_array.append(tmp)

L = Matrix(matrix_array)
possible = L.LLL()

y = abs(x_0 // possible[0][0])
conn.sendlineafter(b'>> ', b'n')
conn.sendlineafter(b'>> ', str(y).encode())
print(conn.recvuntil(b'\n').strip().decode())