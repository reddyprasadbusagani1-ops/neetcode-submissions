class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)

        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for prerequisite in adj[course]:
                if not dfs(prerequisite):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True