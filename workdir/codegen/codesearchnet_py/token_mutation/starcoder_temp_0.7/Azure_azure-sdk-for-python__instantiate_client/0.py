def _instantiate_client(client_class, **kwargs):
    """Instantiate a request from kwargs, removing the subscription_id/tenant_id , if unsupported.
    """
    subscription_id = kwargs.pop('subscription_id', None)
    tenant_id = kwargs.pop('tenant_id', None)
    if subscription_id:
        raise TypeError("The subscription_id parameter is not supported by this profile")
    if tenant_id:
        raise TypeError("The tenant_id parameter is not supported by this profile")
    return client_class(**kwargs)

