def configure_resultproducer(self):
        """
        Configures and returns the ResultProducer and return as tuple.

        :return: path and returns path
        :rtype: tuple
        """
        if self.is_configured:
            return self.result_producer_path, self.result_producer_path
        self.result_producer_path = os.path.join(self.results_path, self.results_producer)
        if self.result_producer_path.endswith(".py"):
            self.result_producer_path = self.result_producer_path[:-3]
        self.result_producer_path = self.result_producer_path.replace(".", "/")
        self.result_producer_path = self.result_producer_path + ".py"
        self.is_configured = True
        return self.result_producer_path, self.result_producer_path


