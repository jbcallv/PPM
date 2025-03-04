def to_vec4(self, isPoint):
        """Converts this vector3 into a vector4 instance."""
        return Vector4(self.x, self.y, self.z, 0.0 if isPoint else 1.0)

