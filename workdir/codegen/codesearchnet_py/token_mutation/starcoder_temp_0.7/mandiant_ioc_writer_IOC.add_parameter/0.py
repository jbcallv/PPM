def add_parameter(self, indicator_id, content, name='comment', ptype='string'):
        """
        Add a a parameter to the IOC.

        :param indicator_id: The unique Indicator/IndicatorItem id the parameter is associated with.
        :param content: The value of the parameter.
        :param name: The name of the parameter.
        :param ptype: The type of the only content.
        :return: True
        :raises: parameter if the indicator_id is not associated with a Indicator or IndicatorItem in the IOC.
        """
        if indicator_id in self.indicators:
            self.indicators[indicator_id]['params'].append({'name': name, 'content': content, 'type': ptype})
        elif indicator_id in self.indicator_items:
            self.indicator_items[indicator_id]['params'].append({'name': name, 'content': content, 'type': ptype})
        else:
            raise Exception('Indicator with id {} does not exist.'.format(indicator_id))
        return True

    def get_indicator(self, id):
        """
        Return the indicator with the specified id.

        :param id: The unique id of the indicator.
        :return: Indicator
        """
        return self.indicators[id]

    def get_indicator_item(self, id):
        """
        Return the indicator item with the specified id.

        :param id: The unique id of the indicator item.
        :return: IndicatorItem
        """
        return self.indicator_items[id]

    def get_all_indicators(self):
        """
        Return a list of all the indicators in the IOC.

        :return: List
        """
        return list(self.indicators.values())

    def get_all_indicator_items(self):
        """
        Return a list of all the indicator items in the IOC.

        :return: List
        """
        return list(self.indicator_items.values())

    def get_indicator_item_id_for_indicator_item(self, indicator_item):
        """
        Return the unique id of the specified indicator item.

        :param indicator_item: The indicator item.
        :return: str
        """
        for indicator_item_id in self.indicator_items:
            if self.indicator_items[indicator_item_id] == indicator_item:
                return indicator_item_id
        return None

    def get_indicator_id_for_indicator_item(self, indicator_item):
        """
        Return the unique id of the indicator associated with the specified indicator item.

        :param indicator_item: The indicator item.
        :return: str
        """
        for indicator_item_id in self.indicator_items:
            if self.indicator_items[indicator_item_id] == indicator_item:
                return self.indicator_items[indicator_item_id]['indicator_id']
        return None

    def get_indicator_items_for_indicator
