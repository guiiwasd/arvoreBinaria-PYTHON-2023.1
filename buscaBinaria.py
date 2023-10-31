def buscaBinaria(x, y):
    li = 0
    ls = len(x) - 1
    while li <= ls:
        pa = (li + ls) // 2
        if y == x[pa]:
            return pa
        elif y < x[pa]:
            ls = pa - 1 #valor procurado abaixo da posição atual
        else:
            li = pa + 1 #valor procurado acima da posição atual
        return -1