for i in range(1, 21, 2):
    print(i, end=' ')
print()

# # part a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# # part b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# # part c
n_value = int(input("Number of Stars: "))
e = 0
while e < n_value:
    print("*", end='')
    e = e + 1
print()

# part d
n_value = int(input("Number of Stars: "))
e = 0
while e < n_value+1:
    print(e*'*')
    e = e + 1

