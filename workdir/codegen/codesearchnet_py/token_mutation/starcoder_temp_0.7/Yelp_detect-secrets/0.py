def merge_plugin_from_baseline(baseline_plugins, args):
    """
    :type baseline_plugins: tuple of BasePlugin
    :param baseline_plugins: BasePlugin input from baseline file

    :type args: dict
    :param args: diction of arguments parsed from usage

    param priority: input param > baseline file > default

    :Returns list of initialized plugins
    """
    plugins_by_name = {plugin.name: plugin for plugin in baseline_plugins}
    plugin_names = args.pop('plugins')

    plugins = []

    for plugin_name in plugin_names:
        plugin_class = plugins_by_name[plugin_name].plugin_class
        plugin_args = plugins_by_name[plugin_name].args

        priority = args.pop('priority')
        if priority is not None:
            plugin_args['priority'] = priority

        plugins.append(plugin_class(**plugin_args))

    return plugins

