from Node import Node
from Node import Label

class Matching:
    G=[]
    n=0
    # n = len(G[0])
    # Array to represent labels of G
    labels = []
    # Matrix of Matching in G
    M = []
    T = []  # Y Vertex
    S = []  # X Vertex
    NG = []  # Neighborhood of S
    alpha = 0  # Value of alpha
    EG = []  # The matrix of the Equality Graph

    def __init__(self,G,matrix_size):
        self.n = matrix_size
        self.create_matrix(G)

    def create_matrix(self,g):
        x_vector=[]
        for i in range(self.n):
            for j in range(self.n):
                node=Node(i,j,g[i][j])
                x_vector.append(node)
            self.G.append(x_vector.copy())
            x_vector.clear()

        # Function calculate de initial label of G

    def set_initial_labeling(self):
        y_labels = []
        x_labels = []

        for i,x in enumerate(self.G):
            maxY = 0
            label_y=Label(0,i)
            y_labels.append(label_y)

            label_x=None
            position=0
            for j,y in enumerate(x):
                if y.weight > maxY:
                    maxY = y.weight
                    position=i
            label_x=Label(maxY,position)
            x_labels.append(label_x)
        self.labels = x_labels + y_labels

    def set_labeling(self):
        for i,actual_label in enumerate(self.labels):
            # If the vertex is X
            if i < self.n:
                # In S there are just Xs
                if actual_label.vertex in self.S:
                    actual_label.label = actual_label.label - self.alpha
            # Else the vertex is Y
            else:
                # In T there are just Ys
                if actual_label.vertex in self.T:
                    actual_label.label = actual_label.label + self.alpha

    def set_equality_graph(self):
        tempEG = []
        for i, x in enumerate(self.G):
            x_vector=[]
            for y, edge_value in enumerate(x):
                if edge_value.weight >= self.labels[i].label:
                    x_vector.append(edge_value)
                else:
                    w=Node(i,y,0)
                    x_vector.append(w)
            tempEG.append(x_vector.copy())
            x_vector.clear()
        self.EG = tempEG

    def set_matching(self, initial):
        self.M = []
        x_labels=self.labels[:self.n]
        if initial:
            x_labels=sorted(x_labels, key=lambda label: label.label, reverse=True)

        for label in x_labels:
            eg_edges = self.EG[label.vertex].copy()
            eg_edges = sorted(eg_edges, key=lambda node: node.weight)
            for edge in eg_edges:
                if edge.weight >= label.label and \
                        not self.is_m_saturated('y', edge.y_position) and \
                        not self.is_m_saturated('x', edge.x_position):
                    self.M.append(edge)
                    break

    def set_matching_y(self):
        self.M = []
        y_labels = self.labels[self.n:self.n*2]
        y_labels = sorted(y_labels, key=lambda label: label.label,reverse=True)
        for label in y_labels:
            temp_edge_array=[]
            for x_vertex in range(self.n):
                temp_node=Node(self.EG[x_vertex][label.vertex].x_position,self.EG[x_vertex][label.vertex].y_position, self.EG[x_vertex][label.vertex].weight)
                temp_edge_array.append(temp_node)

            temp_edge_array = sorted(temp_edge_array, key=lambda node: node.weight)
            for edge in temp_edge_array:
                if (edge.weight >= label.label and \
                    edge.weight >= self.labels[edge.x_position].label) and \
                    not self.is_m_saturated('y', edge.y_position) and \
                    not self.is_m_saturated('x', edge.x_position):
                        self.M.append(edge)






    # Check if a vertex X/Y is M-Saturated
    def is_m_saturated(self, type, vertex):
        for edge in self.M:
            if type == 'x':
                if edge.x_position == vertex:
                    return True
            elif type == 'y':
                if edge.y_position == vertex:
                    return True
        return False

    # Function to return True if the len of the matching
    # equals to N
    def is_perfect_matching(self):
        x_in_m = []
        y_in_m = []
        for edge in self.M:
            if edge.x_position not in x_in_m:
                x_in_m.append(edge.x_position)
            if edge.y_position not in y_in_m:
                y_in_m.append(edge.y_position)
        if len(x_in_m) == len(y_in_m) == self.n:
            return True
        return False

    # Return a X M-unsaturated vertex in EG
    def get_m_unsaturated_vertex(self):
        for i in range(self.n):
            if not self.is_m_saturated('x', i):
                return i
        return False


    # return the neighborhood of the "S" set in the equality graph
    def get_neighborhood(self, S):
        self.NG = []
        for x_vertex in S:
            label = self.get_label('x',x_vertex)
            for edge in self.EG[x_vertex]:
                if edge.weight >= label and edge.y_position not in self.NG: #y_neighbor != 0 and
                    self.NG.append(edge.y_position)


    # compare NG to T
    def is_equals_ng_t(self):
        self.get_neighborhood(self.S)
        if len(self.NG) == len(self.T):
            for vertex in self.NG:
                if vertex not in self.T:
                    return False
        else:
            return False
        return True

    # Function to update the value of Alpha
    def update_alpha(self):
        min_alpha = 1000000  # Big value to compare
        for i, x in enumerate(self.G):
            for j, y in enumerate(x):
                if (i in self.S) and (j not in self.T):
                    # Equation of Alpha:
                    aux_alpha = self.get_label('x', i) + self.get_label('y', j) - self.G[i][j].weight
                    if aux_alpha < min_alpha:
                        min_alpha = aux_alpha
        self.alpha = min_alpha

    def get_label(self, type, vertex):
        if type == 'x':
            return self.labels[vertex].label
        else:
            return self.labels[vertex + self.n].label

    # Return the first Y vertex in NG - T
    def get_y_from_neighborhood_minus_t(self):
        if len(self.NG):
            aux_NG = self.NG.copy()
            x_label=self.labels[0:self.n].copy()
            for i, y in enumerate(self.T):
                if y in aux_NG:
                    aux_NG.remove(y)

            if len(aux_NG) != 0:
                return aux_NG[0]
        return None


    # Return the adjacent vertex in the matching
    def find_matching_vertex(self, type, vertex):
        for edge in self.M:
            if type == 'x':
                if edge.y_position == vertex:
                    return edge
            else:
                if edge.x_position == vertex:
                    return edge
        return None

    def algorithm(self):
        self.set_initial_labeling()
        self.set_equality_graph()
        self.set_matching_y()
        flag_new_match = True
        u = None
        path = []

        while not self.is_perfect_matching():
            if flag_new_match:
                # Step 1
                u = self.get_m_unsaturated_vertex()
                self.S = [u]
                self.T = []
                self.get_neighborhood(self.S)
                flag_new_match = False


            # Step 2
            if self.is_equals_ng_t():
                self.update_alpha()
                if self.alpha != 1000000:
                    self.set_labeling()
                    self.set_equality_graph()
                    self.set_matching_y()
                    self.get_neighborhood(self.S)

            # Step 3
            y = self.get_y_from_neighborhood_minus_t()

            if self.is_m_saturated('y', y):
                z = self.find_matching_vertex('x', y)
                self.S.append(z.x_position)
                self.T.append(y)
            elif y is not None:
                path = self.get_path(u,y)
                self.M = self.new_matching(path)
                flag_new_match = True
            else:
                flag_new_match = True
                self.set_matching_y()


    # Execute a symmetric difference with M and path and return the new matching
    def new_matching(self, path):
        union_set = path.copy()
        union_set = union_set + self.M
        intersection_set = []
        for edge in self.M:
            if edge in path:
                intersection_set.append(edge)

        for edge in intersection_set:
            if edge in union_set:
                union_set = [x for x in union_set if x != edge]

        return union_set

    def is_m_saturated_matching(self, type, matching, vertex):
        for edge in matching:
            if type == 'x':
                if edge.x_position == vertex:
                    return True
            elif type == 'y':
                if edge.y_position == vertex:
                    return True
        return False

    # Get path
    def get_path(self, u, y):
        x_vertex = u
        path=[]
        y_vertex=10000000
        matching = self.M.copy()
        while y_vertex != y:
            # Order X vector
            x_node_list=self.EG[x_vertex].copy()

            x_node_list = sorted(x_node_list, key =lambda node: node.weight, reverse=True)

            # get the x label to compare
            x_label=self.get_label('x',x_vertex)

            # Iterate on nodes to get an unsaturated node and then a saturated
            for current_node in x_node_list:
                if (current_node.weight >= x_label and self.is_m_saturated_matching('y', matching, current_node.y_position) and current_node not in path)\
                        or (y == current_node.y_position):
                    #current_node.weight <= x_label and
                    path.append(current_node)
                    y_vertex = current_node.y_position
                    if y_vertex == y:
                        break
                    else:
                        saturated = None
                        for vertex in matching:
                            if vertex.y_position == y_vertex:
                                saturated = vertex
                                break
                        path.append(saturated)
                        x_vertex = saturated.x_position
                        matching.remove(saturated)
                        break
        return path

    def get_cost(self):
        cost=0
        for edge in self.M:
            cost=cost+edge.weight
        return cost

    def get_match(self):
        matching=[]
        for edge in self.M:
            m=[edge.x_position, edge.y_position]
            matching.append(m)
        return matching
