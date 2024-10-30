
rows = int(input("Enter the number of rows: "))  

for i in range(rows):

    print(' ' * (rows - i - 1), end='')  

    print('*' * (2 * i + 1)) 


for i in range(rows - 1):
    
    print(' ' * (i + 1), end='')  
  
    print('*' * (2 * (rows - i - 2) + 1))  
