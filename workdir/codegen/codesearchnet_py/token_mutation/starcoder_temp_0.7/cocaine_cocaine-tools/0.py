def resolve_group_to_version(self, name, value=None):
        """ Pick a the from a routing group using a fixed or provided value
            path routing group looks like (weight, version):
            {"APP": [[29431330, 'A'], [82426238, 'B'], [101760716, 'C'], [118725487, 'D'], [122951927, 'E']]}
        """
        if not self.route_table:
            self.route_table = self.get_routing_table(self.routing_group)

        if self.route_table:
            if name in self.route_table:
                if value is not None:
                    # caller provided value
                    return value

                # pick the first available
                return self.route_table[name][0][1]

        return None

