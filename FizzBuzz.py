def FizzBuzz():
    lis = [None]*100
    for i in range(len(lis)):
        if i % 3 == 0:
            #print("Fizz")
            lis[i] = "Fizz"
            #print("At index",i,":",lis[i],"\n")
    return lis


#FizzBuzz()


