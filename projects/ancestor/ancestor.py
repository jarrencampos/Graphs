
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class Graph():
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.verticies:
            self.verticies[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])

    queue = Queue()
    queue.enqueue([starting_node])
    longest_path = 1
    earliest_path = -1
    while queue.size() > 0:
        path = queue.dequeue()
        v = path[-1]
        if(len(path) >= longest_path and v < earliest_path) or (len(path) > longest_path):
            earliest_path = v
            longest_path = len(path)
        for next_item in graph.verticies[v]:
            copy = list(path)
            copy.append(next_item)
            queue.enqueue(copy)
    return earliest_path