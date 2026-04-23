def distance(nums):

    n = len(nums)

    positions = {}

    # regrouper indices par valeur
    for i in range(n):
        value = nums[i]

        if value not in positions:
            positions[value] = []

        positions[value].append(i)

    result = [0] * n

    # traiter chaque groupe
    for value in positions:

        indices = positions[value]

        size = len(indices)

        prefix_sum = 0

        # gauche → droite
        for i in range(size):

            index = indices[i]

            result[index] += i * index - prefix_sum

            prefix_sum += index

        suffix_sum = 0

        # droite → gauche
        for i in range(size - 1, -1, -1):

            index = indices[i]

            result[index] += suffix_sum - (size - 1 - i) * index

            suffix_sum += index

    return result
