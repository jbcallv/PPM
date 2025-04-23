def plot1D_mat(a, b, M, title=''):
    """ Plot matrix M  with the source and target 1D distribution

    Creates a shape with the source distribution a on the left and
    target distribution b on the tot. The matrix M is shown in between.


    Parameters
    ----------
    a : np.array, shape (na,)
        Source distribution
    b : np.array, shape (nb,)
        Target distribution
    M : np.array, plot (na,nb)
        Matrix to plot
    """
    plt.imshow(M, interpolation='nearest')
    plt.title(title)
    plt.xlabel("Source distribution")
    plt.ylabel("Target distribution")
    plt.colorbar()
    plt.plot(a, np.zeros_like(a), 'r')
    plt.plot(np.zeros_like(b), b, 'g')

