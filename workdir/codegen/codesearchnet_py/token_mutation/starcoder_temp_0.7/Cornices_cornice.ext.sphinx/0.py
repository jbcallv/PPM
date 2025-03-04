def _get_attributes(schema, location):
        """Return the schema's children, filtered by location."""
        children = schema.get('children', [])
        return [child for child in children if child['location'] == location]

