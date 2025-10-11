# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = {}
        for card in deck:
            count[card] = count.get(card, 0) + 1

        values = list(count.values())

        g = values[0]
        for v in values[1:]:
            g = gcd(g, v)

        if g >= 2:
            groups = []
            for card, freq in count.items():
                groups.extend([[card] * g for _ in range(freq // g)])
            return True, groups
        else:
            return False, []