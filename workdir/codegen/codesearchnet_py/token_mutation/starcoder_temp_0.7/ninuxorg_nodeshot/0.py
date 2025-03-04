def query(query, params={}, epoch=None,
          expected_response_code=200, database=None):
    """Wrapper around ``InfluxDBClient.query()``."""
    if epoch is not None:
        params["epoch"] = epoch
    return client.query(query, params=params, database=database)

