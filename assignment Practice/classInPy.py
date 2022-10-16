# class Length:
#     def __init__(self, len=None):
#         if len != None:
#             self.length = len
#         else:
#             self.length = 0
    
#     def __len__(self):
#         return self.length

# my_len = Length(10)
# print(len(my_len))
def custom_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i
my_gen = custom_generator()
for i in my_gen:
    print(i)