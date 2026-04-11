def minimumDistance(nums):

    positions = {}
    min_distance = float("inf")

    for i in range(len(nums)):

        num = nums[i]

        if num not in positions:
            positions[num] = []

        positions[num].append(i)

        if len(positions[num]) > 3:
            positions[num].pop(0)

        if len(positions[num]) == 3:

            i1 = positions[num][0]
            i3 = positions[num][2]

            distance = 2 * (i3 - i1)

            if distance < min_distance:
                min_distance = distance

    if min_distance == float("inf"):
        return -1

    return min_distance
