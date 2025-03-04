def context_click(self, on_element=None):
        """
        is a context-click (right click) on an element.

        :Args:
         - on_element: The key to context-click.
           If None, clicks on the mouse position.
        """
        if on_element:
            self._execute(Command.CONTEXT_CLICK, {'id': on_element})
        else:
            self._execute(Command.CONTEXT_CLICK)

    def submit(self, on_element=None):
        """
        submit a form.

        :Args:
         - on_element: The key to submit.
           If None, submits the currently active form.
        """
        if on_element:
            self._execute(Command.SUBMIT, {'id': on_element})
        else:
            self._execute(Command.SUBMIT)

