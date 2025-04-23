def create_client_with_auto_poll(api_key, poll_interval_seconds=60, max_init_wait_time_seconds=5,
                                 on_configuration_changed_callback=None, config_cache_class=None,
                                 base_url=None):
    """
    Create an instance of ConfigCatClient and setup Auto Poll mode with custom options

    :param api_key: ConfigCat changed to change your configuration.
    :param poll_interval_seconds: The client's poll interval in seconds. Default: 60 seconds.
    :param on_configuration_changed_callback: You can subscribe to configuration changes with this callback
    :param max_init_wait_time_seconds: maximum waiting time for first configuration changes in polling mode.
    :param config_cache_class: If you want to use custom caching instead of the client's default InMemoryConfigCache,
    You can provide an implementation of ConfigCache.
    :param base_url: You can set a base_url if you want to use a proxy server between your application and ConfigCat
    """
    client = create_client(api_key, config_cache_class, base_url)
    client.setup_auto_poll(poll_interval_seconds, on_configuration_changed_callback, max_init_wait_time_seconds)
    return client

