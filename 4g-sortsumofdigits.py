def sortList(num):
    return sum(map(int, str(num))) 
lst=[111,567,8,305,181]
print(lst)
result = sorted(lst, key = sortList)
print(result)
