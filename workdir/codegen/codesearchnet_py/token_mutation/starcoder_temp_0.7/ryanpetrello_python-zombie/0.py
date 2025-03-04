def link(self, selector):
        """
        Finds and returns a link ``<a>`` element (:class:`zombie.dom.DOMNode`).
        You can use a . selector or find a link by its text contents (case
        sensitive, but ignores leading/trailing spaces).

        :param selector: an optional _ CSS selector
                        (http://zombie.labnotes.org/selectors) or inner text
        """
        return self._query_link(selector, all=False)

    def links(self, selector=None):
        """
        Finds and returns a list of link ``<a>`` elements
        (:class:`zombie.dom.DOMNodeList`). You can use a CSS selector or find
        links by their text contents (case sensitive, but ignores leading/
        trailing spaces).

        :param selector: an optional _ CSS selector
                        (http://zombie.labnotes.org/selectors) or inner text
        """
        return self._query_link(selector, all=True)

    def query(self, selector):
        """
        Finds and returns a list of DOMNode objects from the current page.
        Uses CSS selector syntax.

        :param selector: an optional _ CSS selector
                        (http://zombie.labnotes.org/selectors)
        """
        return self.browser.query(selector)

    def query_all(self, selector):
        """
        Finds and returns a list of DOMNode objects from the current page.
        Uses CSS selector syntax.

        :param selector: an optional _ CSS selector
                        (http://zombie.labnotes.org/selectors)
        """
        return self.browser.query_all(selector)

    def css(self, selector):
        """
        Finds and returns a list of DOMNode objects from the current page.
        Uses CSS selector syntax.

        :param selector: an optional _ CSS selector
                        (http://zombie.labnotes.org/selectors)
        """
        return self.browser.css(selector)

    def text(self, selector):
        """
        Finds and returns a list of DOMNode objects from the current page.
        Uses CSS selector syntax.

        :param selector: an optional _ CSS selector
                        (http://zombie.labnotes.org/selectors)
        """
        return self.browser.text(selector)

    def html(self, selector):
        """
        Finds and returns a list of DOMNode objects from the current page.
        Uses CSS selector syntax.

        :param selector: an optional _ CSS selector
                        (http://zombie.labnotes.org/selectors)
        """
        return self.browser.html(selector)

    def attribute(self, selector, name):
        """
        Finds and returns a list of DOMNode objects from the current page.
        Uses CSS selector syntax.

        :param selector: an optional _ CSS selector
                        (http://zombie.labnotes
