
def gcd(a, b):
    upperbound = 1
    if(a<=b):
        upperbound = a
    elif(b<a):
        upperbound = b
    for i in range(0, upperbound):
        k = upperbound - i
        if((a % k ) == 0 and (b % k) == 0):
            return k
def isPrime(x):
    for i in range(2, int(x**.5)):
        if(x % i ==0):
            return False
    return True
def pseudoprimes(n):
    list = []
    for i in range (3, n+1):
        if(gcd(2, i)==1 and not isPrime(i)):
            if(2**i % i == 2 ):
                list.append(i)
                print(i)
    print(list)

def run():
    pseudoprimes(10000000)
run()
