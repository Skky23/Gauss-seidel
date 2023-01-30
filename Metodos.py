m=19
n=19
matrizX=[[0 for x in range(m)] for y in range(n)]
contador = -19

with open("Ensayo.txt", "r") as archivo:
    numero = archivo.read()
    enteros= [int(x) for x in numero.split()]

for i in range(19):
    contador = contador+19
    for j in range(19):
        #print(contador)
        matrizX[i][j]=enteros[j+contador]
        if contador==361:
            break
print(matrizX)