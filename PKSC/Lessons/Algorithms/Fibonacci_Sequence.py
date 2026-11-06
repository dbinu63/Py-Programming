a, b = 0, 1

cycles = int(input("How many numbers would you like to print? "))

for n in range(0, cycles, 2):
    print(a)
    a += b

    if (cycles % 2 == 1 and n == int(cycles / 2) + 2):
        break

    print(b)
    b += a