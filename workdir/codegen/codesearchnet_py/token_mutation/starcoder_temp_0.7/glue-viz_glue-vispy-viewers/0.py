def on_resize(self, event):
        """Resize handler

        Parameters
        ----------
        type : - of Event
            The following event.
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

