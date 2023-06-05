#Print the first 10 Fibonacci numbers using a loop

fib_list = [1,1]

for a in range(9):
    fib_list.append(sum(fib_list[a:a+2])) 
    
print(fib_list)    
