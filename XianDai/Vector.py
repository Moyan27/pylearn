import math
from ._global import EPSILON
class Vector():
    def __init__(self,lst):
        self._values = list(lst)
    def __iter__(self):
        """
        向量迭代器,不用写_values
        :return:
        """
        return self._values.__iter__()
    def __getitem__(self,index):
        """
        取出向量的第index个元素
        :return:
        """
        return self._values[index]
    def __len__(self):
        """
        返回向量长度（有多少个元素）
        :return:
        """
        return len(self._values)
    #系统调用-->直接输出
    def __repr__(self):
        return "Vector({})".format(self._values)
    #用户调用-->print
    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))
    def __add__(self,another):
        """
        向量相加
        :return:
        """
        if len(self)!=len(another):
            return "无法相加，元素个数不相同"
        else:
            return Vector([a+b for a,b in zip(self,another)])
    def __sub__(self,another):
        """
        向量相减
        :return:
        """
        if len(self)!=len(another):
            return "无法相减，元素个数不相同"
        else:
            return Vector([a-b for a,b in zip(self,another)])
    def __mul__(self, k):
        """
        向量相乘 self*k（默认）
        :param k:
        :return:
        """
        return Vector([k*e for e in self])
    def __rmul__(self, k):
        """
        向量相乘 k*self
        :param k:
        :return:
        """
        return Vector([e*k for e in self])
    def __truediv__(self,k):
        if self.norm()<EPSILON:
            return "错误，分母不能为零"
        else:
            return (1/k)*self
    #向量取正
    def __pos__(self):
        return 1*self
    #向量取负
    def __neg__(self):
        return -1 * self
    #定义零向量
    @classmethod
    def zero(cls,dim):
        """
        返回一个dim维度的零向量
        :param dim:
        :return:
        """
        return cls([0]*dim)
    #向量的模
    def norm(self):
        return math.sqrt(sum(e**2 for e in self))
    #单位向量
    def normalize(self):
        #return Vector([e/self.norm() for e in self])
        return Vector(self._values)/self.norm()
