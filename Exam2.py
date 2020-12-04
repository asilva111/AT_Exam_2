# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 00:03:58 2020

@author: andre
"""
class Solution:
    def FallingPath(self, A):
        paths = [[0] * len(A[i]) for i in range(len(A))]
        
        for i in range(len(A[0])):
            paths[0][i] = A[0][i]
        
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                paths[i][j] = A[i][j] + min(self.getLastSteps(paths,i,j))
        
        print(paths)
        return min(paths[-1])
    
    def getLastSteps(self, paths,row,col):
        lastSteps = []
        if col == 0:
            lastSteps.append(paths[row - 1][col])
            lastSteps.append(paths[row - 1][col + 1])
            
        elif col == len(paths[0]) - 1:
            lastSteps.append(paths[row - 1][col])
            lastSteps.append(paths[row - 1][col - 1])
        
        else:
            lastSteps.append(paths[row - 1][col + 1])
            lastSteps.append(paths[row - 1][col])
            lastSteps.append(paths[row - 1][col - 1])
            
        return lastSteps
    



            

        
        
    
    
    
S = Solution()       
#A = [[1,3,9],[2,1,1],[3,1,1]] 
A = [[1,2,3],[4,5,6],[7,8,9]]
print(S.FallingPath(A))



