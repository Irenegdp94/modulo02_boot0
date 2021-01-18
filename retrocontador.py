def retrocontador(x):
    print("{},".format(x),end="")
    if x > 0:
        retrocontador(x - 1)
    
def sumatorio(n):
    if n > 0:
        return n + sumatorio (n-1)
    else:
        return 0