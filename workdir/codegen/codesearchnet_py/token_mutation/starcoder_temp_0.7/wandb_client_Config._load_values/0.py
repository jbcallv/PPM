def _load_values(self):
        """Load config.yaml from the computer , if available."""
        self.config = {}
        if os.path.isfile(self.config_path):
            try:
                with open(self.config_path) as f:
                    self.config = yaml.load(f, Loader=yaml.FullLoader)
            except Exception as e:
                _LOGGER.error(f"Error loading configuration from {self.config_path}: {e}")

