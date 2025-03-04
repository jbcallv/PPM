def remove_draft_child(self):
        """Remove the track original from versioning."""
        self.original_track.delete()

