def mousePressEvent(self, event):
        """
        Reimplements the :meth:`QLabel.mousePressEvent` method.

        :param event: QEvent.
        :type event: QEvent
        """

        if self.mouse_event_callback is not None:
            self.mouse_event_callback(event, self.mouse_event_data)

