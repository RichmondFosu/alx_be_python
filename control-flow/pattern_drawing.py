#Drawing patterns with nested loops
size = int(input('Enter the size of the pattern: '))

row = 0 #set row to 0
while row < size: # to loop for the number of times = size
    for col in range(size):
        print('*', end='') #to print * side by side for size number of times
    print()
    row += 1 # to stop loop when equal to size