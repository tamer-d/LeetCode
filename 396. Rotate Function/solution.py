def maxRotateFunction(nums):

    n = len(nums)

    total = sum(nums)

    current = 0

    for i in range(n):
        current += i * nums[i]

    maximum = current

    for i in range(n - 1, 0, -1):

        current = current + total - n * nums[i]

        if current > maximum:
            maximum = current

    return maximum
