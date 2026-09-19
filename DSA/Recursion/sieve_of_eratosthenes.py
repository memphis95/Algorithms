def SieveOfEratosthenes(n):
    prime = [True for i in range(0,n+1)]
    # prime number starts with 2
    start_pt = 2
    #  while loop for iterate from squared number to number
    while (start_pt * start_pt <=n):
        if(prime[start_pt] == True):
            for i in range(start_pt*start_pt, n+1, start_pt):
                prime[i] = False
        start_pt += 1
   
    for j in range(2, n+1):
        if prime[j]:
            print(j, end= " ")



if __name__ == "__main__":
    number = int(input())
    SieveOfEratosthenes(number)