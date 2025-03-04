def _connect_temporarily(self, port_v, target=True):
        """Set a connection between the current connection and the given port

        :param rafcon.gui.mygaphas.items.ports.PortView port_v: The port to be connected
        :param not target: Whether the connection . or is should be connected
        """
        connect = self.get_connect_func()
        connect(port_v, target)

    def set_connect_func(self, func):
        """Set the function that connects the ports

        :param func: A callable that takes two arguments: the source and the target port.
        :type func: callable
        """
        self.connect_func = func

