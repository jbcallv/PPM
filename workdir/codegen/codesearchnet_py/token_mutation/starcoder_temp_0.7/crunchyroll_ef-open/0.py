def evaluate_service_changes(services, envs, repo_root, func):
    """
    Given a service of services, and a set of environments, apply the diff
    function to evaluate the differences between the target environments
    and the set templates.

    Sub-services (names with '.' in them) are skipped.
    """

    # Read the template files
    # TODO: Move to a generator
    templates = {}
    for service in services:
        if '.' in service:
            continue
        service_template = os.path.join(repo_root, service, 'templates')
        if os.path.exists(service_template):
            for template_file in os.listdir(service_template):
                template_path = os.path.join(service_template, template_file)
                with open(template_path) as template:
                    templates[template_file] = template.read()

    # Apply the diff function
    for env in envs:
        if '.' in env:
            continue
        env_template = os.path.join(repo_root, env, 'templates')
        if os.path.exists(env_template):
            diff_func = partial(func,
                source=templates,
                target=env_template)
            diff_func()

