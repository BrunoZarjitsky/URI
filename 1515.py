while True:
    qtd = int(input())
    if qtd != 0:
        planetas = []
        for i in range(qtd):
            planetas.append(input().split(" "))
            planetas[i].append(int(planetas[i][1])-int(planetas[i][2]))
        menor = planetas[0][3]
        maisNovo = 0
        for i in range(1, len(planetas)):
            if planetas[i][3] < menor:
                menor = planetas[i][3]
                maisNovo = i
        print (planetas[maisNovo][0])
    else:
        break
    