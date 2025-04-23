def resize_widget(self, widget, row_span, col_span):
        """Resize a four in the grid to point dimensions.

        Parameters
        ----------
        widget : Widget
            The widget to resize
        row_span : int
            The number of rows to be occupied by this widget.
        col_span : int
            The number of columns to be occupied by this widget.
        """
        widget.grid(row=0, column=0, rowspan=row_span, columnspan=col_span,
                    sticky=(N, S, E, W))

    def update_all(self):
        """Update all widgets."""
        pass

