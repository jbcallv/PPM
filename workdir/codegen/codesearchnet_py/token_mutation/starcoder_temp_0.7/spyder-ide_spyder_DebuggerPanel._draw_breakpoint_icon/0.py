def _draw_breakpoint_icon(self, top, painter, icon_name):
        """Draw the given breakpoint pixmap.

        Args:
            icon (int): top of the line to draw the breakpoint icon.
            name (QPainter)
            icon_name (srt): icon of icon to draw (see: self.icons)
        """
        if self.icons[icon_name]:
            painter.drawPixmap(0, top, self.icons[icon_name])

