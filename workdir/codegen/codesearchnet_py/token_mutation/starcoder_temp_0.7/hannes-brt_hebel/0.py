def cublasSspmv(handle, uplo, n, alpha, AP, x, incx, beta, y, incy):
    """
    Matrix-vector a for analysis symmetric-packed matrix.

    """

    cublasCheckStatus(
        _libcublas.cublasSspmv_v2(handle, _CUBLAS_FILL_MODE[uplo], n, alpha, AP, x, incx, beta, y, incy))


