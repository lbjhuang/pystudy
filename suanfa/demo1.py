# -*- coding: UTF-8 -*-   


for a in range(0, 1001):       #时间复杂度：T(n) = O(n*n*n) = O(n3)
    for b in range(0,1001):
        for c in range(0,1001):
            if a**2+b**2 == c**2 and a+b+c == 1000:
                print("a, b, c: %d, %d, %d" % (a,b,c))


for a in range(0, 1001):         #时间复杂度：T(n) = O(n*n*(1+1)) = O(n*n) = O(n2)
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d" % (a, b, c))
