# prime number filter
primes = []
for num in range(2, 101):
    is_prime = True
    divisor = 2
    while divisor <= num // 2:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        primes.append(num)

print(primes)
