# ================================================
# =This program is created by KEVIN PAUL LAMADRID=
# ================================================
from random import randrange
while True:
    print('=====================================')
    print('===PROGRAM BY KEVIN PAUL LAMADRID====')
    print('=====================================')

    choice = int(input("=Please choose a number. \n1-To CALCULATOR \n2-To Grading Equivaleny \n3-To fibonacci Calculation \n4-To Power of n \n5-To Money Convertion \n6-To random list to covert odd number \n7- To Calcualte leap or not leap year \n8-EXIT \n\n ENTER YOUR CHOICE: "))
    print('=====================================')

    if choice == 1:
        #caluculator
        print('CALCULATOR')
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("Choice the operation you want ADDITON - sum,SUBTRACTION -sub, MULTIPLICATION -mul, DIVISION - div ")
        operation_input = str(input("Operation: "))
        if (operation_input == 'sum'):
            c = a + b
            print("Total of :" + str(c))
        elif(operation_input == 'sub'):
            c = a - b
            print("Total of :" + str(c))
        elif(operation_input == 'mul'):
            c = a * b
            print("Total of :" + str(c))
        elif(operation_input == 'div'):
            c = a / b
            print("Total of :" + str(c))
        else:
            continue
    elif choice == 2:
        #grading
        print('GRADING EQUIVALENT')
        grade = int(input("Enter your Grade: "))
        if grade >=90:
            print("A")
        elif grade <=89 and grade >=80:
            print("B")
        elif grade<=79 and grade >=70:
            print("C")
        elif grade<=69 and grade >=60:
            print("D")
        else:
            print("E")
    elif choice == 3:
        #fibonacci
        print('FIBONACCI')
        x = 0
        y = 1
        range_start = 0
        new_list = []
        range_end = int(input("Enter the Last index For Fibonacci:"))
        while range_start<range_end:
            new_list.append(x)
            new = x + y
            x = y
            y = new
            range_start += 1
        print(new_list)
    elif choice == 4:
        print('POWER AND EXPONENT')
        p = int(input("Enter Value of Base: "))
        n = int(input("Enter Value of Exponent: "))
        power = p**n
        print("%s to the power of %s the answer is: %s" % (p,n,power))
    elif choice == 5:
        #CONVERTION
        print('MONEY CONVERTION')
        money = 0
        currency = 0
        final_amount = 0
        amount = 0
        currency = str(input("Choice between peso to dollor = 'pd or PD' or dollar to peso ='dp or DP': "))
        if currency == 'PD' or currency == 'pd' :
            money = float(input("Enter your MONEY in Peso: "))
            amount = float(input("Enter currency of Peso to Dollar:> "))
            final_amount = amount * money
            print("Total Amount of Dollar in Peso is : %s"%(final_amount))
        else:
            money = float(input("Enter your MONEY in Dollar: "))
            amount = float(input("Enter currency of a Dollar to Peso:> "))
            final_amount = amount * money
            print("Total Amount of peso in dollar is :  %s"%(final_amount))
    elif choice == 6:
        #list of random list to odd
        print("RANDOM LIST TO ODD NUMBER LIST")
        assign_range = int(input("Assign Value of Random Range:> "))
        my_value = 0
        random_list = []
        new_random_list_odd = []
        for x in range(0, 19):
            my_value = randrange(assign_range)
            random_list.append(my_value)
            for num in random_list:
                if (num % 2) == 0:
                    num +=1
            new_random_list_odd.append(num)
        print("Random List :  %s"%(random_list))
        print("Random List converted to odd:  %s"%(new_random_list_odd))
    elif choice == 7:
        print('LEAP YEAR OR NOT LEAP YEAR')
        year = int(input("Enter Year: "))
        if (year % 4)==0:
            if (year % 100)==0:
                if(year % 400)==0:
                    print("%s IS LEAP YEAR"% (year))
                else:
                    print("%s IS NOT A LEAP YEAR"% (year))
            else:
                print("%s IS A LEAP YEAR"% (year))
        else:
            print("%s IS NOT LEAP YEAR"% (year))
    elif choice == 8:
        exit()
    else:
        print("Invalid Choice.")