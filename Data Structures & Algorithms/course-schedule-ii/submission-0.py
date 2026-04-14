class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        
        q = deque()
        out = []
        count = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            out.append(course)
            count += 1
            for a in adj[course]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)

        if count == numCourses:
            return out
        else:
            return []
