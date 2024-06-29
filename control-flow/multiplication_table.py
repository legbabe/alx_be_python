number = int(input("Enter a number to see its multiplication table: "))

for value in range(1,11):
    final = value * number
    print(number, '*', value, '= ', final)
    print('yes')