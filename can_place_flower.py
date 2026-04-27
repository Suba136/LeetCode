def canPlaceFlowers(flowerbed, n):
    f = [0] + flowerbed + [0]

    for i in range(1, len(f) - 1):
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            n -= 1

    return n <= 0

if __name__ == "__main__":
    flowerbed = [1, 0, 0, 0, 1]
    n = 1

    print(canPlaceFlowers(flowerbed, n))