def cross_phenotype_jsd(data, groupby, bins, n_iter=100):
    """Jensen-Shannon divergence of based across phenotypes

    Parameters
    ----------
    data : pandas.DataFrame
        A (n_samples, n_features) Dataframe
    groupby : mappable
        A samples to phenotypes mapping
    n_iter : int
        number of bootstrap resampling iterations to perform for the
        within-group comparisons
    n_bins : int
        Number of bins to binify the singles features on

    Returns
    -------
    jsd_df : pandas.DataFrame
        A (n_features, n_phenotypes^2) dataframe of the JSD between each
        feature between and within phenotypes
    """
    if len(groupby)!= data.shape[0]:
        raise ValueError('groupby must have same length as number of samples')

    if len(set(groupby)) < len(groupby):
        raise ValueError('groupby must be unique')

    groupby = pd.Series(groupby)

    if isinstance(bins, int):
        bins = bins * np.ones(data.shape[1], dtype=int)

    if data.shape[1]!= len(bins):
        raise ValueError('data and bins must have same number of features')

    jsd_df = pd.DataFrame()
    for i in range(data.shape[1]):
        x = data.iloc[:, i].values
        jsd_df[i] = jsd_bins(x, bins[i], groupby, n_iter=n_iter)

    return jsd_df

