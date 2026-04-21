def minimumHammingDistance(source, target, allowedSwaps):

    n = len(source)

    # construire le graphe
    graph = {}

    for i in range(n):
        graph[i] = []

    for a, b in allowedSwaps:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n

    def dfs(start, component):

        stack = [start]

        while stack:

            node = stack.pop()

            if visited[node]:
                continue

            visited[node] = True
            component.append(node)

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

    distance = 0

    for i in range(n):

        if visited[i]:
            continue

        component = []

        dfs(i, component)

        count = {}

        # compter occurrences dans source
        for index in component:

            value = source[index]

            if value not in count:
                count[value] = 0

            count[value] += 1

        # comparer avec target
        for index in component:

            value = target[index]

            if value in count and count[value] > 0:
                count[value] -= 1
            else:
                distance += 1

    return distance
