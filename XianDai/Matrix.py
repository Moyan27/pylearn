from .Vector import Vector

class Matrix:
    def __init__(self,list2d):
        self._values=[row[:] for row in list2d]
    def __repr__(self):
        return "Matrix({})".format(self._values)
    
    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))
    
    def shape(self):
        #返回矩阵的形状
        return len(self._values),len(self._values[0])
    def row_num(self):
        #返回矩阵的行数
        return len(self._values)
    def col_num(self):
        #返回矩阵的列数
        return len(self._values[0])
    def size(self):
        #返回矩阵的元素个数
        return len(self._values)*len(self._values[0])
    def __len__(self):
        #返回矩阵的长度
        return len(self._values)
    def __getitem__(self,pos):
        #返回矩阵某个元素
        r,c=pos
        return self._values[r][c]
    def __setitem__(self,pos,value):
        #设置矩阵某个元素
        r,c=pos
        self._values[r][c]=value
    def row_vector(self,index):
        #返回矩阵某一行向量
        return Vector(self._values[index])
    def col_vector(self,index):
        #返回矩阵某一列向量
        return Vector([row[index] for row in self._values])
    def __add__(self,another):
        #矩阵相加
        assert self.shape()==another.shape() ,"无法相加，矩阵不相同"
        return Matrix([[a+b for a,b in zip(row_a,row_b)] for row_a,row_b in zip(self._values,another._values)])
    def __sub__(self,another):
        #矩阵相减
        assert self.shape()==another.shape(),"无法相减，矩阵不相同"
        return Matrix([[a-b for a,b in zip(row_a,row_b)] for row_a,row_b in zip(self._values,another._values)])
    def __mul__(self,k):
        #矩阵数乘
        return Matrix([[e*k for e in row] for row in self._values])
    def __rmul__(self,k):
        #矩阵数乘
        return Matrix([[k*e for e in row] for row in self._values])
    def __truediv__(self,k):
        #返回矩阵除法结果
        return Matrix([[e/k for e in row] for row in self._values])
    def __pos__(self):
        #返回矩阵取正
        return Matrix([[+e for e in row] for row in self._values])
    def __neg__(self):
        #返回矩阵取负
        return Matrix([[-e for e in row] for row in self._values])
    @classmethod
    def zero(cls,r,c):
        #构造r行c列的零矩阵
        return cls([[0]*c for _ in range(r)])
    @classmethod
    def identity(cls,n):
        #构造n行n列的单位矩阵
        m=cls.zero(n,n)
        for i in range(n):
            m[i,i]=1
        return m
    def dot(self,another):
        #判断是矩阵还是向量
        if isinstance(another,Vector):
            assert self.col_num()==len(another),"矩阵的列数和向量的长度不相等"
            #矩阵和向量的乘法
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])
        elif isinstance(another,Matrix):
            assert self.col_num()==another.row_num(),"矩阵的列数和另一矩阵的行数不相等"
            #矩阵和矩阵的乘法
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())] for i in range(self.row_num())])
        
    #矩阵的转置
    def transpose(self):
        return Matrix([[e for e in self.col_vector(i)] for i in range(self.col_num())])
    
    #矩阵的逆矩阵
    def inverse(self):
        assert self.row_num()==self.col_num(),"矩阵的行数和列数不同"
        #计算矩阵的行列
        n=self.row_num()
         