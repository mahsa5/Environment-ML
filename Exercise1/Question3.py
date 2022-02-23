#max and min
num_1 = int(input('enter num1: '))
num_2 = int(input('enter num2: '))
num_3 = int(input('enter num3: '))
if num_1 > num_2 and num_1 > num_3:
    print('max is: ', num_1)
    if num_2 > num_3:
        print('min is: ', num_3)
    else:
        print('min is: ', num_2) 
elif num_2 > num_1 and num_2 > num_3:
    print('max is: ', num_2)
    if num_1 > num_3:
        print('min is: ', num_3)
    else:
        print('min is: ', num_1)
elif num_3 > num_1 and num_3 > num_2:
    print('max is: ', num_3)
    if num_1 > num_2:
        print('min is: ', num_2)
    else:
        print('min is: ', num_1)