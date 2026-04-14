class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for edge in prerequisites:
            adjlist[edge[1]].append(edge[0])

        visited = set()

        def dfs(course):
            if course in visited:
                print('fail')
                return False
            if adjlist[course] == []:
                return True
            visited.add(course)
            print(course)
            for prereq in adjlist[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            return True

        for c in range(numCourses):
            print('yuh')
            if not dfs(c):
                return False
        
        return True