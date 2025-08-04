class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict

        graph = defaultdict(list)

        # Build graph with direction markers
        for a, b in connections:
            graph[a].append((b, 1))  # Edge a -> b needs reversal
            graph[b].append((a, 0))  # Edge b -> a is already good

        visited = set()
        result = 0

        def dfs(node):
            nonlocal result
            visited.add(node)
            for neighbor, needs_reversal in graph[node]:
                if neighbor not in visited:
                    result += needs_reversal
                    dfs(neighbor)

        dfs(0)
        return result
