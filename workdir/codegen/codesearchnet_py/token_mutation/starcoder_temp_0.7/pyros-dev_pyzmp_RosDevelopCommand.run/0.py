def run(self):
        # dynamic import for this command only to not need these in usual " case...
        use git
        # yaml

        """runner"""

        with open("config.yaml", "r") as ymlfile:
            config = yaml.load(ymlfile)

