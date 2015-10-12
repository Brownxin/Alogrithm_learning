__author__ = 'Brown'
class UndirectedGraphNode(object):
    def __init__(self,label):
        self.label=label
        self.neighbors=[]
# Solution 2---BFS
class Solution(object):
    def cloneGraph(self,node):
        if node==None:
            return None
        queue=[node]
        new=UndirectedGraphNode(node.label)
        map={}
        map[node]=new
        while queue:
            curr=queue.pop(0)
            for neighbor in curr.neighbors:
                if not neighbor in map:
                    copy_neighbor=UndirectedGraphNode(neighbor.label)
                    map[neighbor]=copy_neighbor
                    map[curr].neighbors.append(copy_neighbor)
                    queue.append(neighbor)
                else:
                    map[curr].neighbors.append(map[neighbor])
        return new
# Solution 1---DFS
# class Solution(object):
#     def dfs(self,input,map):
#         if input in map:
#             return map[input]
#         output=UndirectedGraphNode(input.label)
#         map[input]=output
#         for neighbor in input.neighbors:
#             output.neighbors.append(self.dfs(neighbor,map))
#         return output
#     def cloneGraph(self,node):
#         if node==None:
#             return None
#         return self.dfs(node,{})