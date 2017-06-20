import random
primes = [17084780723,179425133,1983089081,139592599,1983089519,179425133,139593673,17084781563]
a = 7
b = 7
primelist = [0]
for i in range (64):
    primelist.append(primes[a] * primes[b])
    a -= 1
    if a == 0:
        a = 7
        b -= 1

print primelist[random.randint(1,64)]

