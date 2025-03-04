def assign_vertexid(self):
        """1. create list of vertices which are referred by name only.
        2. list vertex according to (x, y, z)
        3. assign sequence number for each Vertex
        4. sorted list is saved as self.valid_vertices
        """
        self.valid_vertices = []
        for name in self.vertices:
            if name.startswith('V'):
                self.valid_vertices.append(name)
        self.valid_vertices.sort(key=lambda x: (self.vertices[x]['x'],
                                                self.vertices[x]['y'],
                                                self.vertices[x]['z']))
        for i, v in enumerate(self.valid_vertices):
            self.vertices[v]['vertex_id'] = i
        return

