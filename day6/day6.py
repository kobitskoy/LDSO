# r = ([(x+1)*10 for x in range(10)])
# r.insert((len(r))//2,777)
# print(r)
langs = ['python', 'python1','java','c++','c', 'Java', 'C#']
remove = input('Enter the language you want to remove: ')
# rem= []
# for i in langs:
#     if remove in i:
#        rem.append(i)
# for i in rem:
#     langs.remove(i)
print([ i for i in langs if remove.upper()not in i.upper()])



