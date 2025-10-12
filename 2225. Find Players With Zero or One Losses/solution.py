# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches):
        losses = {} 

        for w, l in matches:
            if w not in losses:
                losses[w] = 0
            losses[l] = losses.get(l, 0) + 1

        no_loss = []
        one_loss = []

        for player, lost in losses.items():
            if lost == 0:
                no_loss.append(player)
            elif lost == 1:
                one_loss.append(player)

        return [sorted(no_loss), sorted(one_loss)]