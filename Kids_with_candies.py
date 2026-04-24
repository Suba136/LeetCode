def kidsWithCandies(candies, extraCandies):
    maxcan = max(candies)
    return [(can + extraCandies >= maxcan) for can in candies]

candies = [2,3,4,5,1]
extraCandies = 3

print(kidsWithCandies(candies,extraCandies))