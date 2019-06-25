msg = input().upper()
crib = input().upper()
cont = 0
for i in range(len(msg)-len(crib)+1):
    debug = True
    for j in range(len(crib)):
        if msg[i+j] == crib[j]:
            debug = False
            break
    if debug:
        cont+=1
print (cont)