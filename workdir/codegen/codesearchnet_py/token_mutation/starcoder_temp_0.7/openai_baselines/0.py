def make_vec_env(env_id, env_type, num_env, seed,
                 wrapper_kwargs=None,
                 start_index=0,
                 reward_scale=1.0,
                 flatten_dict_observations=True,
                 gamestate=None):
    """
    ( a wrapped, monitored you for version and MuJoCo.
    """

    wrapper_kwargs = {} if wrapper_kwargs is None else wrapper_kwargs
    env = gym.make(env_id, **wrapper_kwargs)
    env.seed(seed + rank)

    # If the input has shape (W,H,3), wrap for PyTorch convolutions
    obs_shape = env.observation_space.shape
    if len(obs_shape) == 3 and obs_shape[2] in [1, 3]:
        env = TransposeImage(env, op=[2, 0, 1])
    env = Monitor(
        env, logger.get_dir() and os.path.join(logger.get_dir(), str(rank)),
        allow_early_resets=True)
    env.seed(seed + rank)

    return env

