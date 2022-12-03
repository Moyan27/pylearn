from XianDai.Matrix import Matrix
from XianDai.Vector import Vector
from XianDai.LinearSystem import LinearSystem
from XianDai.LinearSystem import inverse


if __name__=="__main__":
    A=Matrix([[1,2,4],[3,7,2],[2,2,3]])
    # b=Vector([7,-11,1])
    # ls=LinearSystem(A,b)
    # if ls.gauss_jordan_elimination():
    #     print("有解")
    # else:
    #     print("无解")
    # ls.fancy_print()
    invA=inverse(A)
    print(invA)
    print(invA.dot(A))