noprimes = [j for i in range(2, 8) for j in range(i * 2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)
print(noprimes)


a = []
a2 = []


for l in range(2, 8):
    for k in range(l * 2, 50, l):
        a.append(k)

for y in range(2, 50):
    if y not in a:
        a2.append(y)

print(a2)
-----------------------------------------------------
a = [[0 for j in range(10)] for i in range(367)]
n = 1
for i in range(1, 367):
    n *= i
    m = n
    while m > 0:
        a[i][m % 10] += 1
        m //= 10

while True:
    n = int(input())
    if n == 0:
        break

    print("{}! --".format(n))
    for i in range(10):
        print("({}) {} ".format(i, a[n][i]), end="")
        if i == 4:
            print()
    print()