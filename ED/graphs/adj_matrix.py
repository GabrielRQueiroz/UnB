class AdjMatrixGraph:
    def __init__(self, vertices, variant):
        self.vertices = vertices
        self.variant = variant
        self.matrix = [[0 for x in range(vertices)] for y in range(vertices)]

    def add_edge(self, which_from, which_to, weight=1):
        if self.variant == "D":
            self.matrix[which_from - 1][which_to - 1] = weight
        else:
            self.matrix[which_from - 1][which_to - 1] = weight
            self.matrix[which_to - 1][which_from - 1] = weight

    def print_graph(self):
        for y in range(self.vertices):
            for x in range(self.vertices):
                weight = self.matrix[y][x]
                if weight < 10:
                    print("   ", end="")
                elif weight < 100:
                    print("  ", end="")
                else:
                    print(" ", end="")

                print(weight, end="")
            print()


vertices, edges, graph_type = input().split()
vertices = int(vertices)
edges = int(edges)
graph = AdjMatrixGraph(vertices, graph_type)

for _ in range(edges):
    where_from, where_to, weight = input().split()
    graph.add_edge(int(where_from), int(where_to), int(weight))

graph.print_graph()

### Input example
#   4 6 N
#   3 2 1
#   3 1 1
#   1 4 1
#   2 3 1
#   4 1 1
#   1 3 1
