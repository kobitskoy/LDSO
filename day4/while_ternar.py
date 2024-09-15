# s,i = 0,0
# while i < 50:
#     s += i if i % 2 == 0 else 0
#     i += 1
# print(s)
#i = 1
# for i in range(1, 11):
#     if i < 9:
#         continue
#     print(i, end=' ')

# result = ''.join(f'{c}{"_"*(i+1)}' for i, c in enumerate(s))
# print(result.capitalize()+'!')
s='праздник'
n = 0
def change_string(str):
    global n
    n += 1
    return str + '_' * n
print((''.join(list(map(change_string, s)))).capitalize(),end='!')

