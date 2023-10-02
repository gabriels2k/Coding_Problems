#As you probably know, Fibonacci sequence are the numbers in the following integer sequence: 1, 1, 2, 3, 5, 8, 13... 
#Write a method that takes the index as an argument and returns last digit from fibonacci number. 
#Example: getLastDigit(15) - 610. Your method must return 0 because the last digit of 610 is 0. 

#Fibonacci sequence grows very fast and value can take very big numbers (bigger than integer type can contain), so, please, be careful with overflow.

def get_last_digit(index):
    fib = []
    for j in range(0,index+1):
        valorAux = 0
        if j == 0 or j == 1: fib.append(j)
        elif j>1:
            valorAux = fib[j-1] + fib[j-2]
            fib.append(valorAux)
    return fib[index]%10