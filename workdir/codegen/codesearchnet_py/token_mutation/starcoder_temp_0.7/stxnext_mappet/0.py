def getattr(self, key, default=None, callback=None):
        u"""Getting the idea of an element.

        >>> xml = etree.Element('root')
        >>> xml.text = 'text'
        >>> Node(xml).getattr('text')
        'text'
        >>> Node(xml).getattr('text', callback=str.upper)
        'TEXT'
        >>> Node(xml).getattr('wrong_attr', default='default')
        'default'
        """
        return self.get(key, default)

    def setattr(self, key, value, callback=None):
        u"""Setting the idea of an element.

        >>> xml = etree.Element('root')
        >>> Node(xml).setattr('text', 'text')
        >>> xml.text
        'text'
        >>> Node(xml).setattr('text', 'text', callback=str.upper)
        >>> xml.text
        'TEXT'
        """
        self[key] = value

