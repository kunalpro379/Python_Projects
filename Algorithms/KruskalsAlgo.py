class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        else:
            self.parent[node] = self.find_ultimate_parent(self.parent[node])
            return self.parent[node]

    def union_by_rank(self, u, v):
        ultimate_parent_of_u = self.find_ultimate_parent(u)
        ultimate_parent_of_v = self.find_ultimate_parent(v)

        if ultimate_parent_of_u == ultimate_parent_of_v:
            return

        if self.rank[ultimate_parent_of_u] < self.rank[ultimate_parent_of_v]:
            self.parent[ultimate_parent_of_u] = ultimate_parent_of_v
        elif self.rank[ultimate_parent_of_v] < self.rank[ultimate_parent_of_u]:
            self.parent[ultimate_parent_of_v] = ultimate_parent_of_u
        else:
            self.parent[ultimate_parent_of_v] = ultimate_parent_of_u
            self.rank[ultimate_parent_of_u] += 1

    def union_by_size(self, u, v):
        ultimate_parent_of_u = self.find_ultimate_parent(u)
        ultimate_parent_of_v = self.find_ultimate_parent(v)
        
        if ultimate_parent_of_u == ultimate_parent_of_v:
            return
        
        if self.size[ultimate_parent_of_u] < self.size[ultimate_parent_of_v]:
            self.parent[ultimate_parent_of_u] = ultimate_parent_of_v
            self.size[ultimate_parent_of_v] += self.size[ultimate_parent_of_u]
        else:
            self.parent[ultimate_parent_of_v] = ultimate_parent_of_u
            self.size[ultimate_parent_of_u] += self.size[ultimate_parent_of_v]


class Solution:
    def spanning_trees(self, V, adj):
        edges = []
        for i in range(V):
            # every node
            for adjNode, wt in adj[i]:
                edges.append((wt, (i, adjNode)))

        ds = DisjointSet(V)
        edges.sort()  # sorting the edges
        mstWt = 0
        for wt, (u, v) in edges:
            if ds.find_ultimate_parent(u) != ds.find_ultimate_parent(v):
                mstWt += wt
                ds.union_by_rank(u, v)
        return mstWt


def main():
    V = 5
    adj = [
        [(1, 2), (3, 6)],
        [(2, 3), (3, 8), (4, 5)],
        [(4, 7)],
        [],
        []
    ]
    sol = Solution()
    mst_weight = sol.spanning_trees(V, adj)
    print("Sum of weights of the minimum spanning tree:", mst_weight)


if __name__ == "__main__":
    main()
