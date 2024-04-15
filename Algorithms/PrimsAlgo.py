import heapq

class Solution:
    def spanning_tree(self, V, adj):
        pq = [] # Priority queue
        heapq.heapify(pq)
        vis = [0] * V # Visited array
        sum = 0 # Initialize sum

        heapq.heappush(pq, (0, 0)) # (wt, node)

        while pq:
            wt, node = heapq.heappop(pq)
            
            if vis[node] == 1:
                continue
            
            vis[node] = 1
            sum += wt

            for adjNode, adjWt in adj[node]:
                if not vis[adjNode]:
                    heapq.heappush(pq, (adjWt, adjNode))

        return sum

def main():
    V = 5  
    adj = [[] for _ in range(V)]



    adj[0].append((1, 2))  
    adj[0].append((3, 6))  
    adj[1].append((2, 3)) 
    adj[1].append((3, 8))  
    adj[1].append((4, 5))  
    adj[2].append((4, 7))  

    sol = Solution()
    sum = sol.spanning_tree(V, adj)

    print("Sum of weights of the minimum spanning tree:", sum)

if __name__ == "__main__":
    main()
