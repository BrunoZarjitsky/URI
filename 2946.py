n = int("0b"+input(), 2)
m = int(input())
lista = []
for i in range(m):
    num = int(input())
    if n%num == 0:
        lista.append(num)
lista.sort()
lista = list(map(lambda x: str(x), lista))
if len(lista) != 0:
    print (" ".join(lista))
else:
    print ("Nenhum")