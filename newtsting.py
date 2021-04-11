# import numpy as np

# # # # a=np.array([[1,2],[5,8],[6,7]])
# # # # c1=a[:,0]
# # # # c2=a[:,1]
# # # # print(c1)
# # # # print(c2)


# # # # c=np.column_stack((c1,c2))
# # # # d=np.transpose(c)
# # # # print(d)
# # # arr1=np.array([1,2,3,4,5])
# # # arr2=np.array([5,67,8,9,10])
# # # newarray=np.column_stack((arr1,arr2))
# # # print(newarray)


# # # class Test:
# # #     def __init__(self,a):
# # #         self.hifi=a
    
# # #     def hello(self,b):
# # #         self.hifi=b
    
# # #     def final(self):
# # #         print(self.hifi)

# # # s=Test(3)
# # # s.hello(5)
# # # s.final()

# # # a=np.array([1,2,3])
# # # b=np.array([6,7,9])
# # # c=np.row_stack((a,b))
# # # print(c)
# # def hello(g):
# #     a=1
# #     b=2
# #     return(a,b)
# # print(hello(6))

# # inputstring=input("enter the string\n")
# # for i in inputstring:
# #     if i=="a" or id(i)==id("e"):
# #         print("true")
# #         break
# # if i==inputstring[-1]:
# #     print("false")


# # class one:
# #     def __init__(self,a=1,b=2):
# #         print(a+b)
# # o=one(2)

# d={}
# d[0]=1
# d[0]=2
# print(d)
import itertools
["".join(perm) for perm in itertools.permutations("abc")]
