def after_connect(self):
        """Execute after connect."""
        pass

    @abstractmethod
    def get_host_and_port(self):
        """Get host and port."""
        pass

