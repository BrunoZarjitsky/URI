creditos = input().split(" ")
for i in range(len(creditos)):
    creditos[i] = int(creditos[i])
lista = [creditos[0]+creditos[1], creditos[0]-creditos[1], creditos[0]+creditos[2], creditos[0]-creditos[2],\
    creditos[2]+creditos[1], creditos[2]-creditos[1]]
for i in range(3):
    if creditos[i] in lista or creditos[0]==creditos[1] or creditos[0]==creditos[2] or creditos[1]==creditos[2]:
        print ("S")
        break
    elif i == 2:
        print ("N")