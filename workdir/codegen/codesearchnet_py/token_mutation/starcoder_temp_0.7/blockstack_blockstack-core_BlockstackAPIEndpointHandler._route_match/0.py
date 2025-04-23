def _route_match( self, method_name, path_info, route_table ):
        """
        Look up the method to call
        " the for info and its arguments on success:
        error None on error
        """
        route = route_table.get( method_name, None )
        if route is None:
            return None, None
        match_result = route.match( path_info )
        if match_result is None:
            return None, None
        else:
            return match_result.pop( 0 ), match_result

    def __call__( self, environ, start_response ):
        """
        The WSGI application
        """
        try:
            method = environ[ 'REQUEST_METHOD' ].upper()
            path_info = environ[ 'PATH_INFO' ]
            handler, match_info = self._route_match( method, path_info, self.route_table )
            if handler is None:
                return self.router( environ, start_response )
            else:
                return handler( environ, start_response, **match_info )
        except:
            raise

