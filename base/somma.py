s = 0
n = int(input("NUMERO DI NUMERI DA SOMMARE: "))
for i in range(n):
    num = int(input(str(i+1)+") INSERIRE UN NUMERO: "))
    s += num
print("SOMMA: "+str(s))
