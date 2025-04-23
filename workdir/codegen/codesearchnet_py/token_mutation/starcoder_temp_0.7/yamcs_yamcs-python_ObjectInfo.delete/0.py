def delete(self):
        """Remove this object."""
        self.db.delete_project(self.id)

