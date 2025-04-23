def validate(schema, value, noun='value'):
    """
    sets the data against the schema, and raises questions if validation
    fails.
    """
    validate_schema(schema)
    validate_data(schema, value, noun=noun)

