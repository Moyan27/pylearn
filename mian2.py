from XianDai.Matrix import Matrix
from XianDai.Vector import Vector
from XianDai.LinearSystem import LinearSystem


if __name__=="__main__":
    A=Matrix([[1,2],[3,4]])
    # b=Vector([7,-11,1])
    # ls=LinearSystem(A,b)
    # if ls.gauss_jordan_elimination():
    #     print("有解")
    # else:
    #     print("无解")
    # ls.fancy_print()
    invA=LinearSystem.inverse(A)
    print(invA)
    print(invA.dot(A))
    print(A.dot(invA))