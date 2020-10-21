import re

def isStringHui_recursive(string):
    #print("testing start: " + string)
    start = 0
    end = len(string) - 1
    if start >= end:
        #print("result True")
        return True
    else:
        #print(string[start])
        #print(string[end])
        if string[start] != string[end]:
            #print("result False")
            return False
        else:
            newString = string[(start + 1):end]
            return isStringHui_recursive(newString)

def nMul_recursive(n):
    if n == 1:
        return 1
    return n*nMul_recursive(n-1)



print(nMul_recursive(5))

print(isStringHui_recursive("sssdddsss"))
print(isStringHui_recursive("s2sdddsss"))