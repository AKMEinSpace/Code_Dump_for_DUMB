'''
    snabbare sätt att göra listor
'''

lista = ["na" for i in range(10)]

#print(lista)    
#["na","na","na","na","na","na","na","na","na","na"]

#nästlad for loop
lista = [[i for i in range(1,11)] for j in range(5)]

#print(lista)
#lista = [[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]

lista = [i for i in range(0,101,2)]
print(lista)

#redigera listor

List = [1,2,3]
w, v, t = List
print(v, w, t )
# 2 , 1 , 3
print(t, v, w )
# 3 , 2 , 1