import random

n = 30
k = 5

if n <= 1:
    print(False)
elif n <= 3:
    print(True)
elif n % 2 == 0:
    print(False)
else:
    d = n - 1
    while d % 2 == 0:
        d //= 2

    is_prime = True
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                is_prime = False
                break
            if x == n - 1:
                break
        if not is_prime:
            break
    print(is_prime)

n = 3
k = 5

if n <= 1:
    print(False)
elif n <= 3:
    print(True)
elif n % 2 == 0:
    print(False)
else:
    d = n - 1
    while d % 2 == 0:
        d //= 2

    is_prime = True
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                is_prime = False
                break
            if x == n - 1:
                break
        if not is_prime:
            break
    print(is_prime)
