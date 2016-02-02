
numbers = []
count = 0
total = 0

while True:
    line = input("enter a number or Enter to finish: ")
    if line:
        try:
            number = int(line)
            if len(numbers) == 0:
                min_num = number
                max_num = number
            else:
                if min_num > number:
                    min_num = number
                if max_num < number:
                    max_num = number
            numbers.append(number)
            total += number
            count += 1
        except ValueError as err:
            print(err)
            continue
    else:
        break;
if len(numbers):
    print("numbers:", numbers)
    print("count = ", count, "sum = ", total, "lowest = ", min_num,
          "highest = ", max_num, "mean = ", total/count)
