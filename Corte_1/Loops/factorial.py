while True:
     value = int(input("enter a positive integer value: "))
     print("value: ", value)
     a = isinstance(value, int)
     if a == True and value >0:
          fact = 1
          for i in range (1, value+1):
               fact = fact*i
          print(f'the factorial of {value} is: ', fact)
     else:
       print("please, enter a positive integer number")