

import os
matrix = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]
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

#print("if_same_row= ", if_same_row(matrix))

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
#print("if_same_col= ",if_same_col(matrix))

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
#print("if_same_diagonal= ", if_same_diagonal(matrix))

#--------------------------------------------------

def reset_matrix(matrix):
    
    fresh_matrix = [['1', '2', '3'],
                    ['4', '5', '6'],
                    ['7', '8', '9']]
    for col in range(3):
         for row in range(3):
             matrix[col][row] = fresh_matrix[col][row]
             
    return matrix

#--------------------------------------------------
def replace_elemnt(matrix,str_input,replace ):
    flag_element_exist = False
    for col in range(3):
        for row in range(3):
            if matrix[col][row] == str_input: 
                matrix[col][row] = replace
                flag_element_exist = True
    if flag_element_exist == False : 
        print("Game Over or Player introduced wrong number.")
        return -1
 
                
#--------------------------------------------------

def if_win(matrix): 
    if if_same_row(matrix) or  if_same_col(matrix) or if_same_diagonal(matrix): 
        
        return True
    else:
        return False
                
#--------------------------------------------------



def start_game():
  

    os.system('cls')
    str_input = ''
    reset_matrix(matrix)
    print_matrix(matrix)
    
    while True:    
        str_input = input ("\nPlayer X Introduce a number from 1 to 9 :")
        if replace_elemnt(matrix,str_input,replace = 'x' ) == -1:
            return -1
        print_matrix(matrix)
        if if_win(matrix): 
            print('Player X Win ')
            flag_win = True
            return -1

        
       
        str_input = input ("\nPlaer 0 (zero) Introduce a number from 1 to 9 :")
        if replace_elemnt(matrix,str_input,replace = '0' ) == -1:
            return -1
        print_matrix(matrix)
        if if_win(matrix): 
            print('Player 0 Win ')
            return -1
        
  
#----------------------------------


flag = True 
while flag:
    print("\n\nNew game \n")
    
    flag_win = False
    
    msg = input ("Pres ok to start or quit for exit ")
   
    if msg =='quit':
       flag = False
       print("aplication wasa closetd.") 
    else : start_game()




