class Matrix:
    label = []
    M = [[1,1],[2,1]]


    def __init__(self, label_i):
        self.label=label_i

    # Return the label of x
    def get_label_x(self, i):
        if i >= len(self.label)//2:
            return -1
        return self.label[i]

    # Return the label of y
    def get_label_y(self,i):
        if i >= len(self.label)//2:
            return -1
        y_start = len(self.label)//2
        y_position = y_start + i
        return self.label[y_position]

    # return the neighborhood of the "S" set in the equality graph
    def get_neighborhood(self, S, equality_graph):
        neighborhood=[]
        for x_count, vertex in enumerate(S):
            for y_count, element in enumerate(equality_graph[vertex]):
                if element!=0:
                    neighborhood.append([x_count,y_count])

    # Return the M-augmenting path
    def make_path(self, y, equality_graph):
        unsaturated_vertex = y
        path=[unsaturated_vertex]
        while unsaturated_vertex is not None:
            saturated_vertex = self.find_matching_vertex(unsaturated_vertex)
            if saturated_vertex is not None and saturated_vertex not in path:
                path.append(saturated_vertex)
                n = len(equality_graph)
                for i in range(n):
                    vertex = [i,saturated_vertex[1]]
                    if i != saturated_vertex[0] and vertex not in path:
                        unsaturated_vertex=[i,saturated_vertex[0]]
                        path.append(unsaturated_vertex)
                        break
                    else:
                        unsaturated_vertex = None
            else:
                unsaturated_vertex = None

        return path

    # Return the adjacent vertex in the matching
    def find_matching_vertex(self,y):
        for vertex in self.M:
            if vertex[0] == y[0]:
                return vertex
        return None

    # Execute a symmetric difference with M and path and return the new matching
    def new_matching(self, path):
        union_set=path.copy()
        union_set=union_set+self.M
        intersection_set=[]
        for vertex in self.M:
            if vertex in path:
                intersection_set.append(vertex)

        for vertex in intersection_set:
            if vertex in union_set:
                union_set = [x for x in union_set if x != vertex]

        return union_set


m=Matrix([1,2,3,4,5,6])
#print(m.get_label_x(2))
#print(m.get_label_y(0))
#m.get_neighborhood([0,1],[[1,4,0],[0,8,0],[0,0,5]])
path=m.make_path([1,2],[[1,6,0],[0,8,6],[4,0,0]])
pp=m.new_matching(path)
for u in path:
    print(u)
print("---------------")
M = [[0,1],[1,1],[2,1]]
for u in M:
    print(u)
print("---------------")
for u in pp:
    print(u)
