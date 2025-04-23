def class_prediction_error(
    model,
    X,
    y=None,
    ax=None,
    classes=None,
    test_size=0.2,
    random_state=None,
    **kwargs):
    """Quick method:
    Divides the dataset X and y into train and test splits, fits the model on
    the train split, then scores the model on the test split. The visualizer
    displays the support for each class in the fitted classification model
    displayed as a stacked bar plot Each segment is segmented to show the
    distribution of predicted classes for each class.

    This helper function is a quick wrapper to utilize the ClassPredictionError
    function for one-off analysis.

    Parameters
    ----------
    model : the Scikit-Learn estimator (should be a classifier)

    X  : ndarray or DataFrame of shape n x m
        A matrix of n instances with m features.

    y  : ndarray or Series of length n
        An array or series of target or class values.

    ax : matplotlib axes
        The axes to plot the figure on.

    classes : list of strings
        The names of the classes in the target

    test_size : float, default=0.2
        The percentage of the data to reserve as input data.

    random_state : int or None, default=None
        The value to seed the random number generator for shuffling data.

    Returns
    -------
    ax : matplotlib axes
        Returns the axes that the class prediction error plot was drawn on.
    """
    cpv = ClassPredictionError(model, classes, ax=ax, **kwargs)
    cpv.fit(X, y)
    cpv.score(X, y, test_size=test_size, random_state=random_state)
    return cpv.ax

