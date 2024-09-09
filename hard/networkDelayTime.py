import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        visit = set()
        for u,v,w in times:
            edges[u].append((v,w))
        print(edges)
        queue = []
        heapq.heappush(queue, (0, k))
        t = 0
        while queue:
            current_weight,current_vertex = heapq.heappop(queue)
            if current_vertex in visit:
                continue
            visit.add(current_vertex)
            t = max(t, current_weight)
            for neighbour_vertex,neighbour_vertex_weight in edges[current_vertex]:
                if neighbour_vertex not in visit:
                    # Calculates the new weight
                    new_weight = current_weight + neighbour_vertex_weight
                    heapq.heappush(queue, (new_weight, neighbour_vertex))
        
        return t if len(visit) == n else -1


        

        
