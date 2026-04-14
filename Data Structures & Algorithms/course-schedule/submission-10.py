class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)


        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        count = 0
        while q:
            course = q.popleft()
            count += 1
            for a in adj[course]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)
        
        return count == numCourses
