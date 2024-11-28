from collections import deque

def DFS(Graph):
    track = []
    begin = 'U'

    visited = set()

    visited.add(begin)

    stack = [begin]


    while stack:
        present_node = stack.pop()
        #print(present_node)
        track.append(present_node)
        
        for present_node in Graph[present_node]:
            if present_node not in visited:
                visited.add(present_node)
                stack.append(present_node)
                if present_node == 'E':
                    return track


def BFS(Graph):
    track = []
    begin = 'U'

    visited = set()

    visited.add(begin)

    queue = deque()

    queue.append(begin)


    while queue:
        present_node = queue.popleft()
        #print(present_node)
        track.append(present_node)

        for present_node in Graph[present_node]:
            if present_node not in visited:
                visited.add(present_node)
                queue.append(present_node)
                if present_node == 'E':
                    return track
