from random import getrandbits, randint

f = open('flag.txt')
flag = f.read()
f.close()

lucky = False
y = getrandbits(512)
while True:
    choice = input('>> ')
    if choice.strip() != '?':
        break
    
    a = getrandbits(512)
    b = getrandbits(384)

    x = randint(1000, 1500)
    if not lucky and x == 1337:
        lucky = True
        print('lucky', a * y)
    else:
        print('nahhh', a * y + b)

try:
    z = int(input('>> ').strip())
    if y == z:
        print(flag)
    else:
        print('nahhh')
except:
    print('nahhh')