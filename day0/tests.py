def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return print(a, b)
def tmp(a, b):
    tmp = a
    a = b
    b = tmp
    return print(a, b)
def change(a, b):
    a, b = b, a
    return print(a, b)
def ab_test(a, b):
    b,a = (str(a)+" "+str(b)).split()
    return print(a, b)
if __name__ == '__main__':
    tmp(10, 20)
    swap(10, 20)
    change(10, 20)
    ab_test(10, 20)

