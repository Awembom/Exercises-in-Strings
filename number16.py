number = input("Enter the binary number you want to convert to dicimal: ")
decimal = 0
j = -1
for i in range(len(number)):
    value = int(number[j]) * pow(2, i)
    j -= 1
    decimal += value

#program to convert from binary to a decimal number