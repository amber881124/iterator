# for i in range(3):
#     print(i)

# for loop
# for i in 'Momo':
#     print(i)
# M
# o
# m
# o

# iterator
name = 'Momo'
print(dir(name))
# 會print一堆name有的屬性,其中包含了__iter__
name_iter = iter(name)
# 等同於 name_iter = name.__iter__()
print(dir(name_iter))
# 會有__next__屬性
print(next(name_iter)) # 印出M
# 等同於 print(name_iter.__next__())
print(next(name_iter)) # 印出o
print(next(name_iter)) # 印出m
print(next(name_iter)) # 印出o
print(next(name_iter)) # 出現StopIteration這個exception

# # 把list加總
# x = [1, 3, 5]
# x_iter = iter(x)
# print(sum(x_iter)) # 9 (正確)
# print(sum(x_iter)) # 0 (因為只能iterate over一次,第二次走不了)

# # 把iterator抓出的轉成list
# x = [1, 3, 5]
# x_iter = iter(x)
# print(list(x_iter)) # [1, 3, 5] (正確)
# print(list(x_iter)) # [] (因為只能iterate over一次,第二次走不了)
