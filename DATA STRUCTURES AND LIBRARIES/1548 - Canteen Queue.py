def cria_bloco(array, i):
    run = [array[i]]

    i += 1
    while i < len(array):
        if array[i - 1] >= array[i]:
            run.append(array[i])
            i += 1
        else:
            break
    return run, i

def organiza_bloco(array):
    n = len(array)
    indice_atual = 0
    bloco_run = []

    while indice_atual < n:
        run, prox_indice = cria_bloco(array, indice_atual)
        if prox_indice - indice_atual >= 1:  
            bloco_run.append(run)
        indice_atual = prox_indice

    organizada_array = []
    for run in bloco_run:
        organizada_array = mescla_bloco(organizada_array, run, [])

    return organizada_array

def mescla_bloco(arr1, arr2, resultado):
    i, j = 0, 0
    arr1_tam, arr2_tam = len(arr1), len(arr2)

    while i < arr1_tam and j < arr2_tam:
        if arr1[i] >= arr2[j]:
            resultado.append(arr1[i])
            i += 1
        else:
            resultado.append(arr2[j])
            j += 1

    for i in range(i, arr1_tam):
        resultado.append(arr1[i])
    for i in range(j, arr2_tam):
        resultado.append(arr2[i])
    return resultado

def valores_iguais(array_copy, bloco_run):
    iguais = 0
    for i in range(len(array_copy)):
        if array_copy[i] == bloco_run[i]:
            iguais += 1
    return iguais

vezes = int(input())
for _ in range(vezes):
    n_valores = int(input())
    array = list(map(int, input().split()))
    array_copy = array.copy()
    organizada_array = organiza_bloco(array)
    print(valores_iguais(array_copy, organizada_array))