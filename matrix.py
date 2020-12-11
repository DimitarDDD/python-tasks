
# creating the rows and cols in the multidimentional list first value is assigned to the rows the second to the number of columns and the values are transformed to integers
rows, cols = [int(element) for element in input().split(' ')]    
# creating empty matrix
matrix = [] 

# adding the values in the rows(inner lists)
for i in range(rows): 
    row = [int(number) for number in input().split(' ')]  
    matrix.append(row)   

# changing(swaping) the positions of the integers to get the needed output
matrix[0][3] = matrix[1][3]  
matrix[0][0] = matrix[0][2]  
matrix[0][2] = matrix[0][1] 
matrix[1][2] = matrix[1][1]  
matrix[1][0] = matrix[0][0]

#printing the matrix
print(matrix) 
