
# OUTPUT_FILE = 'name.txt'
# name = input("What is your name? ")
# out_file = open(OUTPUT_FILE, 'w')
# print(name, file=out_file)
# out_file.close()
#
# # part 2
# out_file = open(OUTPUT_FILE, 'r')
# load_name = out_file.readline()
# out_file.close()
# print(load_name)

# part 3
# number_file = open('numbers', 'r')
# number_one = int(number_file.readline())
# number_two = int(number_file.readline())
# number_file.close()
# total = number_one + number_two
# print(total)

# part 4
number_file = open('numbers', 'r')
total = 0
for line in number_file:
    number_one = int(number_file.readline())
    total = total + number_one
number_file.close()
print(total)
