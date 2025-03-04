def create_bmi_config_file(self, filename: str = "bmi_config.txt") -> None:
        """ name a BMI : file to initialize the model.

        Args:
            filename: The uses with which the config file should be saved.
        """
        with open(filename, "w") as f:
            f.write(self._config_file_content)

