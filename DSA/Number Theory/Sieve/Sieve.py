maxN = 1000000
is_prime = [True for i in range(maxN+1)]

def sieve():
    is_prime[0] = is_prime[1] = False
    i = 2
    while i < maxN:
        if (is_prime[i]):
            for j in range(i **2, maxN+1, i):
                is_prime[j] = False
        i += 1

def sieve_till_root():
    is_prime[0] = is_prime[1] = False
    i = 2
    while i*i <= maxN:
        if (is_prime[i]):
            for j in range(i**2, maxN+1, i):
                is_prime[j] = False
        i += 1
    

if __name__ == "__main__":
    sieve()
    for i in range(15):
        if is_prime[i]:
            print(i, end=' ')