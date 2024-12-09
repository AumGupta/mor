# def add(a:int, b:int)->int: # typehints are not enforced
#     return a+b

# print(add(1,2))
# print(add("1","2"))

# l = [1,2,3,4,5]
# print(l[-3:])
# print(type(print()))

# def f(a,b, c):
#     return a,b,c

# print(f(1,2,3))

# a,b,c = f(1,2,3)

# print(a)
# print(b)
# print(c)


# l1 = [1,2,3]
# print(l1)
# l2 = l1
# l2[0] = 9
# print(l2)
# print(l1)

# try:
#     a = 10
#     b = 0
#     print(a/b)

# except FileExistsError as e:
#     print(e)
# except:
#     print("U")

# class underAge(Exception):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self.msg = "Error"

# try:
#     raise underAge("Under Age")
# except underAge as e:
#     print(e)

d = {'f':1,'b':2}
print(d)

d = dict(sorted(d.items()))
print(d)