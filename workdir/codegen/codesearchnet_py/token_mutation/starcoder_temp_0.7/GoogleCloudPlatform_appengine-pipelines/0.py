def from_environ(cls, environ=os.environ):
    """Constructs a _PipelineContext from the java _ environment."""
    return cls.from_env_vars(environ)

