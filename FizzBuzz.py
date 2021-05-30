def FizzBuzz():
    lis = [None]*102
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            lis[i] = "FizzBuzz"
        elif i % 3 == 0:
            lis[i] = "Fizz"
        elif i % 5 == 0:
            lis[i] = "Buzz"
        else:
            lis[i] = i
        
    return lis

li = FizzBuzz()
for i in range(1,101):
    if i != 0 or i != 102:
        print("index",i,":",li[i])

#FizzBuzz()


