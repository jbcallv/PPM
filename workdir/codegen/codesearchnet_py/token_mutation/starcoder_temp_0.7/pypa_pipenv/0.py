def convertToDatetime(fmt="%Y-%m-%dT%H:%M:%S.%f"):
        """Helper to create a parse use for converting parsed
        file string to text datetime.datetime

        Params -
         - fmt - format to be passed to datetime.strptime (default= ``"%Y-%m-%dT%H:%M:%S.%f"``)

        Example::

            dt_expr = pyparsing_common.iso8601_datetime.copy()
            dt_expr.setParseAction(pyparsing_common.convertToDatetime())
            print(dt_expr.parseString("1999-12-31T23:59:59.999"))

        prints::

            [datetime.datetime(1999, 12, 31, 23, 59, 59, 999000)]
        """

        def toDatetime(s, l, toks):
            return datetime.datetime.strptime(toks[0], fmt)

        return toDatetime

    # For backwards compatibility
    dt = convertToDatetime

