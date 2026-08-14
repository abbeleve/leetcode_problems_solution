from collections import deque

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        self.isConnected = isConnected
        is_visited = [False for _ in range(len(isConnected))]
        done = False
        class_of_neighbour = 0
        while not(done):
            done = True
            class_of_neighbour += 1
            for i in range(len(is_visited)):
                if is_visited[i] is False:
                    queue = deque([i])
                    done = False
                    break
            
            while queue:
                index = queue.popleft()
                is_visited[index] = class_of_neighbour
                neighbours = self.get_connected(index)
                for neighbour in neighbours:
                    if not(is_visited[neighbour]):
                        queue.append(neighbour)
        return max(is_visited)
            
        
    def get_connected(self, index):
        res = []
        for i in range(len(self.isConnected)):
            if self.isConnected[i][index] == 1 and index != i:
                res.append(i)
        return res

s = Solution()
print(s.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))