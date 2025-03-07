"""
3x3 Matrix Multiplication
M1 = [[10, 100, 230], [40, 50, 60], [70, 80, 90]]
M2 = [[90, 100, 70], [60, 50, 40], [30, 20, 10]]

3x3 + 3x3 = 3x3 
"""

def matrix_multiplication(M1, M2):
    for i in range (len(M1)): # itereating rows
        for j in range (len(M2)): # Iterating columns
            M3[i][j] = M1[i][j] + M2[i][j]
        print (f"i is {i}, j is {j}")
        
M1 = [[10, 100, 230], 
     [40, 50, 60], 
     [70, 80, 90]]

M2 = [[90, 100, 70], 
      [60, 50, 40], 
      [30, 20, 10]]

M3 = [[0,0,0], 
      [0,0,0], 
      [0,0,0]]

matrix_multiplication(M1, M2)
      
print ("The final matrix is: \n")
for k in M3:
    print (k)