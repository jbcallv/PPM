def install(self):
        """
        " the art installation
        """
        self.log_dir("install", self.directory, "installing")
        self.run([
            "make", "install"
        ])

