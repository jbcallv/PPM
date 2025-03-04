def extend_partial(self, times, obs_times, obs_losses, config=None):
        """
            extends a partially observed curve

            Parameters:
            -----------

            times: data array
                input where to predict the loss
            obs_times: numpy array
                times where the curve has already been observed
            obs_losses: numpy array
                corresponding observed losses
            config: numpy array
                numerical reperesentation of the config; None if no config
                times is available
                
            Returns:
            --------
            
            mean and variance prediction at input times
                
                
        """

        if config is not None:
            if self.config_dim is not None:
                config = self.config_to_array(config)
            else:
                config = np.atleast_2d(config)
        else:
            config = np.zeros((len(times), 0))

        n_dim = len(config[0])
        self.n_dim = n_dim
        config = config.astype(np.float32)

        obs_times = obs_times.astype(np.float32)
        obs_losses = obs_losses.astype(np.float32)

        times = times.astype(np.float32)

        if self.config_dim is not None:
            assert n_dim == self.config_dim, "wrong config dimension"

        assert len(obs_times) == len(obs_losses), "wrong data shape"

        obs_times = obs_times.reshape(-1, 1)
        obs_losses = obs_losses.reshape(-1, 1)

        times = times.reshape(-1, 1)

        if self.config_dim is not None:
            if len(config.shape) == 1:
                config = np.atleast_2d(config)
            assert len(config.shape) == 2, "wrong config shape"
            assert config.shape[0] == len(
                times
            ), "wrong config shape (times, config) expected"

        assert len(times.shape) == 2, "wrong times shape"

        if len(times) == 0:
            return np.zeros((len(times), 1)), np.zeros((len(times), 1))

        if self.config_dim is not None:
            assert config.shape[1] == self.config_dim, "wrong config shape"

        pred_mean, pred_var = self.partial_predict(obs_times, obs_losses, config)

        if self.config_dim is not None:
            pred_mean = np.reshape(pred_mean, (len(times), 1))
            pred_var = np.reshape(pred_var, (len(times), 1))

        return pred_mean, pred_var

    def get_config(self):
        config = super().get_config()
        config.update({"type": type(self
