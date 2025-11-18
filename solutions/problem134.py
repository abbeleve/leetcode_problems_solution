class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        max_battery = 0
        for stop_index in range(0, len(gas)):
            battery = gas[stop_index] - cost[stop_index]
            if 
            if (battery) >= 0:
                to_start = False
                circular_stop_index = (stop_index + 1) % len(gas)
                while circular_stop_index != stop_index:
                    battery += gas[circular_stop_index] - cost[circular_stop_index]
                    circular_stop_index += 1
                    circular_stop_index = circular_stop_index % len(gas)
                    if battery <= 0:
                        if battery == 0 and circular_stop_index == stop_index:
                            return stop_index
                        to_start = True
                        break
                if not(to_start):
                    return stop_index
        return -1
        
s = Solution()
print(s.canCompleteCircuit(gas = [4], cost = [4]))