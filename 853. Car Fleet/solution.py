# 853. Car Fleet

class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]
        
        fleets = 0
        prev_time = 0
        
        for t in times:
            if t > prev_time:
                fleets += 1
                prev_time = t
        return fleets
