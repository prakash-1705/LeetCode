from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False]*n
        visited[0] = True
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbour in rooms[node]:
                if not visited[neighbour] :
                    visited[neighbour] = True
                    queue.append(neighbour)
        for i in visited:
            if(not i):
                return False
        return True


        