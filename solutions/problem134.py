class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        saved_gas = []
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            saved_gas.append(diff)
        i = 0
        while i < len(saved_gas):
            if saved_gas[i] >= 0:
                possible, index = self.ride(saved_gas, i)
                if possible:
                    return i
                else:
                    i = index
                    continue
            i += 1
        return -1

    def ride(self, saved_gas, index):
        overall_sum = saved_gas[index]
        saved_index = index
        index += 1
        while index % len(saved_gas) != saved_index:
            if overall_sum < 0:
                return False, index
            overall_sum += saved_gas[index % len(saved_gas)]
            index += 1
        return True, index
        
s = Solution()
print(s.canCompleteCircuit(gas = [5,8,2,8], cost = [6,5,6,6]))