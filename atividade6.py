quantidade=int(input("digite a quantidade de numeros que deseja ver:"))
i=0
atual=1
anterior=0
aux=0
while i < quantidade:
  soma=anterior+atual
  print(soma)
  aux=atual
  atual=soma
  anterior=aux
