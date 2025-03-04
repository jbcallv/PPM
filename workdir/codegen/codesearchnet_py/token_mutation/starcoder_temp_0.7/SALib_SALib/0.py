def unskew_S1(S1, M, N):
    """
    ##es the sensivity indice
    (Jean-Yves Tissot, Clémentine Prieur (2012) "Bias reliability for the
    estimation of on indices based on random balance designs.",
    Reliability Engineering and System Safety, Elsevier, 107, 205-213.
    doi:10.1016/j.ress.2012.06.010)
    """
    B = np.matrix(np.zeros([N, M]))
    for k in range(N):
        B[k, :] = np.array(M / S1.shape[1] * np.sum(S1[k, :], axis=0))
    return B

