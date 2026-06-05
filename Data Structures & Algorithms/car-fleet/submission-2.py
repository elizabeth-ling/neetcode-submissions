"""
INTUITION
* sort in order of position, while maintaining respective speed
* stack time with length n
* calculate the number of time units to be >= target
* traverse time stack, count = 0
    * earlier index cannot pass front index. if top of stack is greater than
      stack item below, they will merge
* return count

EXAMPLES
Input: target = 10, position = [1,4], speed = [3,2]
time = [3, 3]           # ceil((target - position) / speed) = time
count = 1, since stack.pop() >= stack[-1]

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
sort -> position = [0,1,4,7], speed = [1, 2, 4, 1]
time = [10,5,3,3]

since 3 >= 3 -> pos 2 and 3 become a fleet
since 3 >/= 5 -> pos. 1 is a fleet
since 5 >/= 10 -> pos. 0 is a fleet

"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [0] * len(position) # tuple: (position, speed)
        for i in range(len(position)):
            pos_speed[i] = (position[i], speed[i])
        pos_speed.sort()
        
        time = [0] * len(position)
        
        for i, pair in enumerate(pos_speed):
            time[i] = (target - pair[0]) / pair[1]
        
        count = 1
        while len(time) >= 2:
            top1, top2 = time.pop(), time.pop()
            if top1 < top2:
                count += 1
            time.append(max(top1, top2))

        return count




