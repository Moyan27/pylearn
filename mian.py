from XianDai.Vector import Vector
from XianDai.Matrix import Matrix
import numpy as np

if __name__=="__main__":
    matrix1=Matrix([[1,2,7],[3,4,9]])
    matrix2=Matrix([[2,3,4],[4,5,7],[3,6,2]])
    vec1=Vector([3,4,6])
    print(matrix1.dot(matrix2))
    print(matrix1.dot(vec1))
    print(matrix2.dot(vec1))