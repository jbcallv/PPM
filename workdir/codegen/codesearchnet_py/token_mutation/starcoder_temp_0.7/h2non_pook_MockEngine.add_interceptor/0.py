def add_interceptor(self, *interceptors):
        """
        add one or more HTTP traffic interceptors to the current
        mocking engine.

        Interceptors are typically HTTP client specific wrapper classes that
        implements the http interceptor interface.

        Arguments:
            interceptors (pook.interceptors.BaseInterceptor)
        """
        for interceptor in interceptors:
            self.interceptors.append(interceptor)

