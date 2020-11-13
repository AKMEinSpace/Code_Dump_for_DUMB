'''
    Sorteringsalgoritmer
'''
import random
lista = [random.randint(1,100) for i in range(20)]


def bubbleSort(lista):
    while True:
        swap=0
        for i in range (0,len(lista)-1):
            if lista[i] > lista[i+1]:
                temp=lista[i]
                lista[i] = lista[i+1]
                lista[i+1]=temp
                swap+=1
        if swap == 0:
            break
    return lista
print(bubbleSort(lista))

