def set_aad_metadata(uri, resource, client):
    """Set the metadata."""
    metadata = {
        "azure_ad_endpoint": uri,
        "azure_ad_resource": resource,
        "azure_ad_client_id": client
    }
    return metadata

