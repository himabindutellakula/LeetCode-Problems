# from collections import defaultdict

# class Solution(object):
#     def maxPathSum(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
        
#         if not root:
#             return 0  # If the root is None, return 0 (Edge case)

#         # If the tree has only the root node, return root's value
#         if not root.left and not root.right:
#             return root.val
        
#         adjList = defaultdict(list)  # To hold neighbors

#         def getNeighbours(node, parent):
#             if not node:
#                 return
            
#             if node.val in adjList:
#                 return  # Node already processed

#             # Initialize adjacency list for this node
#             adjList[node] = []

#             if parent:
#                 adjList[node].append(parent)  # Add parent connection

#             if node.left:
#                 adjList[node].append(node.left)
#                 getNeighbours(node.left, node)  # Recursively process left child

#             if node.right:
#                 adjList[node].append(node.right)
#                 getNeighbours(node.right, node)  # Recursively process right child

#         def fillAdjacencyList(node, parent):
#             if not node:
#                 return
#             getNeighbours(node, parent)
#             fillAdjacencyList(node.left, node)
#             fillAdjacencyList(node.right, node)

#         fillAdjacencyList(root, None)

#         # DFS to generate paths
#         def dfs(node, path, visited, result):
#             """Depth-First Search to generate all paths starting from 'node'."""
#             visited.add(node)
#             path.append(node)

#             # If the path has more than one node, compute the sum
#             if len(path) > 1:
#                 path_tuple = tuple(path)
#                 path_sum = sum(node.val for node in path_tuple)  # Sum of node values in the path
#                 result[node].setdefault(path_tuple, path_sum)
            
#             # Always include the current node as a path by itself
#             if len(path) == 1:
#                 result[node].setdefault(tuple(path), path[0].val)  # Only node value as path sum

#             # Explore neighbors
#             for neighbor in adjList.get(node, []):
#                 if neighbor not in visited:
#                     dfs(neighbor, path[:], visited.copy(), result)

#         def generate_paths():
#             """Generates all valid paths for each node and computes path sums."""
#             result = {node: {} for node in adjList}  # Initialize result dictionary

#             # Start DFS from each node
#             for node in adjList:
#                 dfs(node, [], set(), result)

#             return result

#         # Generate paths and print result
#         final_result = generate_paths()

#         # # Print the formatted output (optional)
#         # for node, paths in final_result.items():
#         #     print(str(node.val) + ": " + str(paths))

#         def find_max_path_sum(final_result):
#             max_sum = float('-inf')  # Initialize to negative infinity
#             max_path = None  # Store the path with the max sum

#             for node, paths in final_result.items():
#                 for path, total in paths.items():
#                     if total > max_sum:  # Update max sum if a larger one is found
#                         max_sum = total
#                         max_path = path

#             return max_sum, max_path  # Return both the max sum and the corresponding path

#         # Get the maximum sum and path
#         max_sum, max_path = find_max_path_sum(final_result)
#         # print("Maximum Path Sum:", max_sum)
#         # print("Path:", max_path)

#         return max_sum

# TLE for 5 out of 96 testcase
# time complexity is O(n)
# but for a completely unbalanced tree it can go upto O(2^n)


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0  # If the root is None, return 0 (Edge case)

        # Initialize the result variable to keep track of the maximum path sum
        self.max_sum = float('-inf')

        # Helper function to calculate the maximum path sum from the current node
        def dfs(node):
            if not node:
                return 0  # Base case: no path from a None node

            # Recursively calculate the maximum path sum for the left and right subtrees
            left_max = max(dfs(node.left), 0)  # Only take positive paths
            right_max = max(dfs(node.right), 0)  # Only take positive paths

            # Current node's maximum path sum is the node value + max path sum from left and right
            current_max = node.val + left_max + right_max

            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_max)

            # Return the maximum path sum that can be extended to the parent node
            return node.val + max(left_max, right_max)

        # Start DFS from the root node
        dfs(root)

        # Return the maximum path sum found
        return self.max_sum



