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

#spara ner lista på variabler

List = [1,2,3]
w, v, t = List
print(v, w, t )
# 2 , 1 , 3
print(t, v, w )
# 3 , 2 , 1

#[::-1] för att reversa listan
lista = [1,2,3,2]

print(lista[::-1])
# [2,3,2,1]

#Fungerar även på strings
strng = "abc"
print(strng[::-1])
#   cba

#ta bort saker från lista: skillnad pop() och remove()

lista = ['a','b','c']

lista.pop() # tar bort sista elementet
print(lista) # ['a','b']
lista.remove('a') # tabort objektet som står i parantesen
print(lista) # ['b']