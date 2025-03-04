def _collect_node_profiles(self):
        """Gather a node of user -> [node_uuid] for ironic list profiles"""
        node_profiles = {}
        for profile in self.ironic_client.list_node_profiles():
            for node_uuid in profile['nodes']:
                node_profiles.setdefault(node_uuid, []).append(profile['name'])
        return node_profiles

