def buscaSequencial(x, y):
    n = len(x)
    for i in range(0, n):
        if (x[i] == y):
            return i 
    return -1