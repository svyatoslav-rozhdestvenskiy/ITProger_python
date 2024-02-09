# region lesson11
# data = set('hello')
# lis = [a for a in range(11)]
# data = {5, 7, 4, 3, 5}
# data.add(6)
# data.update(lis)
# # data.clear()
# data.pop()
# data.remove(1)
# data.discard(4)
# print(data)
# nums = [a for a in range(11)]
# nums.extend([a for a in range(21)])
# print(nums)
# nums = list(set(nums))
# print(nums)
# new_data = frozenset([5, 7, 4, '32', 4, '48', 7, 5, True, 5])
# print(new_data)
# endregion
# region task1
# data = {a for a in range(5)}
# data.add(67)
# print(data)
# data.discard(67)
# data.update([9, 12])
# print(data)
# endregion
# region task2
# lis = [1, 53, 8, 9, 34, 1, 0, 53, 53, 8, 73, 5]
# lis = list(set(lis))
# print(lis)
# endregion
# region task3
# lis = [a**2 for a in range(11)]
# data1 = set(lis)
# data2 = {'abc'}
# data3 = set()
# for i in lis:
#     data3.add(i - 1)
# for i in range(1, 4):
#     print(locals()[f'data{i}'])
# endregion
# region task4
# set1 = {a for a in range(11)}
# print(set1)
# set2 = {a for a in range(11, 21)}
# set4 = {a for a in range(21, 31)}
# frozenset1 = frozenset(set2)
# set3 = set1.union(frozenset1)
# set3.update([2, 5])
# set3.discard(2)
# set3.pop()
# print(set3)
# endregion
