# initalize flow matrix of size number_of_vertices x number_of_vertices
# if there is an edge between u and v then flow_matrix[u][v] equals capacity of this edge
def create_flow_matrix(edges, n_vertices):
    flow_matrix = [[0 for vertex in range(n_vertices)] for vertex in range(n_vertices)]
    for edge in edges:
        flow_matrix[edge[0]][edge[1]] = edge[2]
    return flow_matrix

def create_path(source, sink, parents):
    path=[]
    vertex = sink
    while (vertex!=source):
        path.insert(0, vertex)
        vertex = parents[vertex]
    path.insert(0, source)
    return path


def find_path(flow_matrix, source, sink, n_vertices):
    visited = []
    queue = []
    parents = [-1 for v in range(n_vertices)]
    visited.append(source)
    queue.append(source)
    
    while queue:
        node = queue.pop(0)
        for vertex, capacity in enumerate(flow_matrix[node]):
            if capacity > 0 and vertex not in visited:
                parents[vertex] = node
                if vertex == sink:
                    break
                visited.append(vertex)
                queue.append(vertex)

    if parents[sink]==-1:
        return False

    return create_path(source, sink, parents)

def find_bottleneck(path, flow_matrix):
    return min(flow_matrix[path[i]][path[i+1]] for i in range(len(path)-1))

def update_flow(flow, flow_matrix, path):
    for i in range(len(path)-1):
        # forward edge
        flow_matrix[path[i]][path[i+1]] -= flow
        # backward edge
        flow_matrix[path[i+1]][path[i]] += flow


def ford_fulkerson(network):
    source = network[0]
    sink = network[1]
    n_vertices = network[2]
    edges = network[3]
    max_flow = 0

    flow_matrix = create_flow_matrix(edges, n_vertices)
    while True:
        path = find_path(flow_matrix, source, sink, n_vertices)
        if not path:
            return max_flow
        current_flow = find_bottleneck(path, flow_matrix)
        max_flow += current_flow
        update_flow(current_flow, flow_matrix, path)

