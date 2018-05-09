#creating a fibonacci sequence
def fibonacci():
    num = int(input("How many numbers that generates?:"))   # it prints the string and asks the total number to be generated
    i = 1
    if num == 0:                                            # if the given number is 0  i.e if the statement is true
        fib = []                                            # generate an empty series
    elif num == 1:                                          #  if num is 1 , if this statement is true
        fib = [1]                                           #  first number prints
    elif num == 2:                                          # if number is 2 i.e generate two numbers of the series
        fib = [1,1]                                         # this prints the first two numbers in the series in the formate [a,b]
    elif num > 2:                                           # if more than two numbers are to be generated 
        fib = [1,1]                                         # print the series in this format
        while i < (num - 1):                                # up to second last value 
            fib.append(fib[i] + fib[i-1])                   # use this function to generate the series
            i += 1                                          # continue to generate series by addying one to the last digit used
    return fib                                              
print(fibonacci())                                          # print the series
input()                                                     # this flashes the line to put the value

