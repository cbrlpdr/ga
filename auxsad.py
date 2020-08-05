import itertools

vec = [25,27,37,40,42]

clA = [25,27,37]
clB = [40,42]

sm = 0
for a in itertools.combinations(clA,2):
    print (a)

for a in itertools.combinations(clB,2):
    for i in range(len(a)-1):
        sm+=abs(a[i]-a[i+1])

print(sm)

