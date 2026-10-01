class Solution:
    def countPrimes(self, n: int) -> int:
        primes=[True]*n
        if n==0 or n==1 or n==2:
            return 0
        primes[0]=False
        primes[1]=False
        last=int((n)**(0.5))
        for i in range(2,last+1):
            if primes[i]==1:
                for j in range(i*i,n,i):
                    primes[j]=0
        return sum(primes)


        