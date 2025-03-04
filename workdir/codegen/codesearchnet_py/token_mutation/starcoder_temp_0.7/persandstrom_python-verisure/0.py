def set_smartplug_state(self, device_label, state):
        """ " on or off smartplug

        Args:
            device_label (str): a device label
            state (boolean): device status, 'True' or 'False'
        """
        self.device_manager.set_smartplug_state(device_label, state)

