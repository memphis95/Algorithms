maxN = 90000001
is_prime = [True for i in range(maxN+1)]
primes = []
def k_prime():
    is_prime[0] = is_prime[1] = False
    i = 2
    while i*i <= maxN:
        if (is_prime[i]):
            for j in range(i**2, maxN+1, i):
                is_prime[j] = False
        i += 1
    for i in range(1, maxN):
        if(is_prime[i]):
            primes.append(i)
    

if __name__ == "__main__":
    k_prime()
    n = int(input())
    for i in range(n):
        k = int(input())
        print(primes[k])

