# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:23:59 2020

@author: Chandini Ganesan
This is a 9X9 Sudoku solver 
"""
from random import seed
from random import randint
puzzle=[[0,0,0,0,0,0,2,0,0],
        [0,8,0,0,0,7,0,9,0],
        [6,0,2,0,0,0,5,0,0],
        [0,7,0,0,6,0,0,0,0],
        [0,0,0,9,0,1,0,0,0],
        [0,0,0,0,2,0,0,4,0],
        [0,0,5,0,0,0,6,0,3],
        [0,9,0,4,0,0,0,7,0],
        [0,0,6,0,0,0,0,0,0]]
def work():
    status=check_all(puzzle)
    if status==None:
        return True
    else:
        i,j=status
    for val in range(1,10):
        #print(i,j,val,check_column,check_row,check_box)
        if check_column(j,val) and check_row(i,val) and check_box(i,j,val):
            puzzle[i][j]=val
            if work():
                return True
            puzzle[i][j]=0
    return False
        
    
                
            
def check_all(puzz):
    for i in range(0,len(puzz)):
        for j in range(0,len(puzz[i])):
            if puzz[i][j]==0:
                return i,j
    return None

def check_column(col_index,rand_val):
    for i in range(0,9):
        if(puzzle[i][col_index]==rand_val):
            return False
    return True
def check_row(row_index,rand_val):
    for i in range(0,9):
        if(puzzle[row_index][i]==rand_val):
            return False
    return True
def check_box(i,j,rand_val):    
    row=(i//3)*3
    column=(j//3)*3
    #print(row,column)
    for x in range(row,row+3):
        for y in range(column,column+3):
            if puzzle[x][y]==rand_val :
                return False
    return True

work()
print(puzzle)
