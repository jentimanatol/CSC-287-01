
from ntpath import join


matrix = [['0', '2', '3'],
          ['4', '0', '6'],
          ['7', '8', '0']]



#----------------------------------------------------------------

def test_matrix_operation(matrix):
    print("print element matrix [1][2]= ", matrix[1][2])
    print ("print a row matrix [2]= ", matrix [2] )

    print ("concatinate 3 number = " + 'a'+ 'b'+ 'c')

    #print ("Summ of element in a row 2 = ", sum(matrix[2]))# not working for str
    
    print ("lenght of matrix ", len(matrix))
    
    print ("lenght of matrix[0] ", len(matrix[0]))
    
#test_matrix_operation(matrix)
#------------------------------------------------------------------

def concatinate_matrix(matrix):
    concatinate_element = ' '
    for row in matrix:
      for element in row:
        concatinate_element += element       
    print("concatinate_element = " , concatinate_element)
# concatinate_matrix(matrix)
    
#-------------------------------------------------------------------

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
#print_matrix(matrix)
#--------------------------------------------------

def chek_same_row(matrix):
    for row in matrix:
        print(''.join(row))
        if ''.join(row) == 'xxx': 
           print('win')
        else: print('los')
#chek_same_row(matrix)


#--------------------------------------------------

def if_same_row(matrix):
    for row in matrix:
        if ''.join(row) == 'xxx' or ''.join(row) == '000' : 
           return True
    return False

print("if_same_row= ", if_same_row(matrix))

#--------------------------------------------------

def if_same_col(matrix):
    
    for col in range(3):
        colon =''
        for row in range(3):
            colon += matrix[row][col]
            #print(colon)
            if colon == 'xxx' or colon == '000' :
                 return True       
    return False
print("if_same_col= ",if_same_col(matrix))

#--------------------------------------------------

def if_same_diagonal(matrix):
    
    diagonal = ''
    for d in range(3):
            diagonal += matrix[d][d]
            #print(colon)
            if diagonal == 'xxx' or diagonal == '000' :
                 return True       
             
             
    diagonal = ''         
    for d in range(3):
            diagonal += matrix[d][2-d]
            #print(diagonal)
            if diagonal == 'xxx' or diagonal == '000' :
                 return True       
                     
    return False
print("if_same_diagonal= ", if_same_diagonal(matrix))

#--------------------------------------------------







print_matrix(matrix)

