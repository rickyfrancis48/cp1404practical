number = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 5, 9]
# numbers[3:4] = 1
# 5 in numbers = true
# 7 in numbers = false
# "3" in numbers = false
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

number.remove(3)
number.insert(0, "10")

number.remove(2)
number.append(1)

print(number[2:])

if number.index(9):
    print(number)
