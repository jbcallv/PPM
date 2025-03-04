def create_response_signature(self, string_message, zone):
        """ Basic helper function to keep type clean for defining a new data signature """
        signature = {
            'zone': zone,
            'raw': string_message,
           'signature': self.generate_signature(string_message, zone)
        }
        return signature

    def generate_signature(self, string_message, zone):
        """ Basic helper function to keep type clean for defining a new data signature """
        return 'not implemented'

