import random

minimum = 1
maximum = 45

line_total = int(input("How many quick picks? "))
for i in range(line_total):
    quick_pick = [str(random.randint(1, 45)) for num in range(6)]
    quick_pick.sort()
    print(" ".join(quick_pick))
    # print(quick_pick{:2d})
