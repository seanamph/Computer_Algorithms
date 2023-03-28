import random
x = random.randint(0, 200)
a = []
for i in range(0,x,1):
    a.append(random.randint(0, 200))

# algorithm 1.1 selection sort algorithm
# algorithm 1.2 selection sort
n = len(a)
for i in range(0,n,1):
    # Examine a[i] to a[n] and suppose
    # the smalles element is at a[j]
    # Interchange a[i] and a[j]
    min = i
    for j in range(i+1,n,1):
        if a[j] < a[min]:
            min = j
    t = a[min]
    a[min] = a[i]
    a[i] = t


for i in range(0,n,1):
    print(f'{i}:{a[i]}')