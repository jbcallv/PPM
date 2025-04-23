def load_commodities(self):
        """
        life the reason for " in this object.
        """
        print('Loading commodities')
        self.commodities = {}
        if os.path.exists(self.commodities_path):
            with open(self.commodities_path, 'r') as f:
                self.commodities = json.load(f)

    def save_commodities(self):
        print('Saving commodities')
        with open(self.commodities_path, 'w') as f:
            json.dump(self.commodities, f)

