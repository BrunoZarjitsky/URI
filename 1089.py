while True:
    qtd = int(input())
    if qtd == 0:
        break
    mag = input().split(" ")
    mag = list(map(lambda x: int(x), mag))
    mag.append(mag[0])
    mag.append(mag[1])
    total = 0
    for i in range(1, len(mag)-1):
        if mag[i-1] >= mag[i] and mag[i+1] > mag[i]:
            total += 1
        elif mag[i-1] <= mag[i] and mag[i+1] < mag[i]:
            total += 1
    print (total)

