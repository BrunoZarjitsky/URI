n, m = input().split()
n, m = int(n), int(m)
ligadas = input().split()[1:]
lampadas = list(range(m))
for i in lampadas:
    if str(i+1) in ligadas:
        lampadas[i] = True
        continue
    lampadas[i] = False
interruptores = []
for i in range(n):
    interruptores.append(input().split()[1:])
cont = 0
interruptores = interruptores*2
for i in interruptores:
    cont += 1
    for j in i:
        if lampadas[int(j)-1]:
            lampadas[int(j)-1] = False
            continue
        lampadas[int(j)-1] = True
    if True not in lampadas:
        break
if True not in lampadas:
    print (cont)
else:
    print (-1)