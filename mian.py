from XianDai.Vector import Vector

if __name__=="__main__":
    vec1=Vector([1,2,3])
    vec2=Vector([4,5,6])
    print(vec1.normalize())
    print(vec1.normalize().norm())