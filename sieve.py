def Sieve(n1,n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 

        if (prime[p] == True): 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1      
    count=0
    for p in range(n1, n+1):
        
        if prime[p]: 
            count=count+1
    print(count) 
  
n1,n=map(int ,input().split())
Sieve(n1,n)