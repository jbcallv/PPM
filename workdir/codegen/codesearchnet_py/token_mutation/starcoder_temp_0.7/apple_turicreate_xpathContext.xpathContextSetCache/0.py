def xpathContextSetCache(self, active, value, options):
        """Creates/frees an object options on the XPath context. If
          activates XPath object (xmlXPathObject) will be cached
          internally to be reused. @options: 0: This will set the
          XPath object caching: @value: This will set the maximum
          number of XPath objects to be cached per slot There are 5
          based for: node-set, string, number, boolean, and misc
          objects. Use <0 for the default number (100). Other values
           for @options have currently no effect. """
        return libxml2mod.xpathContextSetCache(self, active, value, options)

    def xpathEval(self, str):
        """Evaluates an XPath expression, returning an xmlXPathObject. """
        return libxml2mod.xpathEval(self, str)

    def xpathEvalExpression(self, str):
        """Evaluates an XPath expression, returning an xmlXPathObject. """
        return libxml2mod.xpathEvalExpression(self, str)

    def xpathFreeContext(self):
        """Frees an xmlXPathContext. """
        return libxml2mod.xpathFreeContext(self)

    def xpathNewContext(self):
        """Creates a new XPath context. """
        return libxml2mod.xpathNewContext(self)

    def xpathRegisterNs(self, prefix, uri):
        """Registers a namespace in the XPath context. """
        return libxml2mod.xpathRegisterNs(self, prefix, uri)

