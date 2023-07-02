test_list = [803, 91, 45, 3, 215]
print(test_list)
temp1 = map(str, test_list)
max_len = max(map(len, temp1))
res = sorted(test_list, key = lambda idx : (str(idx).ljust(max_len, 'a')))
print(res)
