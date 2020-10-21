# int a[] =  [20, 201, 203,...]
# max

def getHigh(num):
    while num > 1:
        num = num/10
    return num

def match(num1, num2):
    n1 = len(str(num1))
    n2 = len(str(num2))
    n = n1
    if n1 > n2:
        n = n2
    for i in range(n):
        if str(num1)[i] != str(num2)[i]:
            return False
    print("match True")
    return True

def compareHighSame(num1, num2):
    if match(num1, num2):
        n1 = len(str(num1))
        n2 = len(str(num2))
        print(n1)
        print(n2)
        n = n1
        if n1 > n2:
            n = n2
            print(str(num1)[n])
            print(str(num1)[0])
            if int(str(num1)[n]) < int(str(num1)[0]):
                return True
            else:
                return False
        elif n1 == n2:
            return True
        else:
            print("num2 is more long")
            print(str(num2)[n])
            print(str(num2)[0])
            if int(str(num2)[n]) < int(str(num2)[0]):
                return True
            else:
                return False
    else:
        return False

def sort(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
             print(a[i])
             print(a[j])
             if getHigh(a[i]) < getHigh(a[j]):
                 print("compare False")
                 temp = a[i]
                 a[i] = a[j]
                 a[j] = temp
             if compareHighSame(a[i], a[j]):
                  print("compare True")
                  temp = a[i]
                  a[i] = a[j]
                  a[j] = temp
    return a


a=[20,201,203,34,56]
print(sort(a))



