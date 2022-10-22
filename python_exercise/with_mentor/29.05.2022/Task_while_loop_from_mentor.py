"""
1. print all numbers up to 100 in 5 steps
2. print all numbers up to 100 in 5 steps but CONTINUE 50
3. print all numbers up to 100 in 5 steps but BREAK at 70
4. combine 2 and 3
i.e 5, 10, 15, 20, ...
"""
# 1. print all numbers up to 100 in 5 steps
n1 = 0
while n1 < 100:
    n1 += 5
    print(n1, end=' ')
print()
# 2. print all numbers up to 100 in 5 steps but CONTINUE 50
n2 = 0
while n2 < 100:
    n2 += 5
    if n2 == 50:
        continue
    print(n2, end=' ')
print()
# 3. print all numbers up to 100 in 5 steps but BREAK at 70
n3 = 0
while n3 < 100:
    n3 += 5
    if n3 == 70:
        break
    print(n3, end=' ')
print()
# 4. combine task 2 and 3

n4 = 0
while n4 < 100:
    n4 += 5
    if n4 == 50:
        continue
    if n4 == 70:
        break
    print(n4, end=' ')