p = 1
n = int(input("NUMERO DI NUMERI DA MOLTIPLICARE: "))
for i in range(n):
    num = int(input(str(i+1)+") INSERIRE UN NUMERO: "))
    p *= num
print("PRODOTTO: "+str(p))
