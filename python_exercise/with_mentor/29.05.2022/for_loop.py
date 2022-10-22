counter_even = 0
sum_even = 0
for x in range(2, 25):
    if x % 2 == 0:
        counter_even += 1
        sum_even += x
        print(x, end=' ')
print(f"\nCount of even numbers is {counter_even}")
print(f"Sum of even numbers is {sum_even}")
