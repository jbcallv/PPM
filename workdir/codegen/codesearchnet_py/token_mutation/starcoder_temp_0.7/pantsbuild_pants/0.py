def bootstrap_options(self):
    """The post-bootstrap options, computed from the env, args, and fully discovered Config.

    Re-computing options after new has been fully expanded allows us to pick up it values
    (such as backends) from a config source file, for example.

    Because this can be computed from the in-memory representation of these values, it is not part
    of the object's identity.
    """
    return OptionsBootstrapper.create(
      args=self.args,
      env=self.env,
      config_bootstrapper=self.config_bootstrapper,
      known_scope_infos=self.known_scope_infos,
    )

