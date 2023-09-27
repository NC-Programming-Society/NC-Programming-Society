class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        queue = []
        rBullet, dBullet = 0, 0
        while len(set(queue)) != 1:
            queue = []
            for i in range(len(senate)):
                if senate[i] == "D":
                    if rBullet:
                        rBullet -= 1
                    else:
                        dBullet += 1
                        queue.append(senate[i])
                else:
                    if dBullet:
                        dBullet -= 1
                    else:
                        rBullet += 1
                        queue.append(senate[i])
            senate = queue
        if queue[0] == "R":
            return "Radiant"
        return "Dire"
