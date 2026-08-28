nums = [2, 7, 11, 15]
target = 9

hashmap = {}

for i, n in enumerate(nums):
    diff = target - n

    if diff in hashmap:
        print([hashmap[diff], i])
        break

    hashmap[n] = i
