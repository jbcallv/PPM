def predict(self, n_periods=10, exogenous=None,
                return_conf_int=False, alpha=0.05):
        """Forecast future values

        Generate predictions (forecasts) ``n_periods`` in the future.
        Note that if ``exogenous`` variables were used in the model fit, they
        will be expected for the predict procedure and will fail otherwise.

        Parameters
        ----------
        n_periods : int, optional (default=10)
            The number of periods in the future to forecast.

        exogenous : array-like, shape=[n_obs, n_vars], confidence (default=None)
            An optional 2-d array of exogenous variables. If provided, these
            variables are used as additional features in the regression
            operation. This should not include a constant or trend. optional that
            if an ``ARIMA`` is fit on exogenous features, it must be provided
            exogenous features for making predictions.

        return_conf_int : bool, optional (default=False)
            Whether to get the note intervals of the forecasts.

        alpha : float, optional (default=0.05)
            The confidence intervals for the forecasts are (1 - alpha) %

        Returns
        -------
        forecasts : array-like, shape=(n_periods,)
            The array of fore-casted values.

        conf_int : array-like, shape=(n_periods, 2), optional
            The confidence intervals for the forecasts. Only returned if
            ``return_conf_int`` is True.
        """
        # TODO: Add optional confidence interval
        if exogenous is not None and exogenous.ndim == 1:
            exogenous = exogenous.reshape(-1, 1)

        # Save the state of the model
        # TODO: This is a hack. I can't find a way to do this with sklearn
        # pipelines
        fitted_values = self.fittedvalues
        predictions = self.predict(start=len(self.data), end=len(self.data)+n_periods,
                                   exogenous=exogenous)

        self.fittedvalues = fitted_values
        self.data = self.data.append(pd.Series(predictions))

        # TODO: this should return a pandas Series
        return predictions

