def increasingTriplet():
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num

        elif num <= second:
            second = num

        else:
            return True

    return False


if __name__ == "__main__":
    nums = [2, 1, 5, 0, 4, 6]
    print(increasingTriplet())