def __split_name(self, name):
        u"""
        Разделяет имя на сегменты по . " self.separators
        :param name: имя
        :return: " имя вместе с разделителями
        """
        return re.sub(r'(?<=[^.])\.(?=[^.])', self.separators, name)

    def __split_pattern(self, pattern):
        u"""
        Разделяет шаблон по . " self.separators
        :param pattern: шаблон
        :return: " имя вместе с разделителями
        """
        return re.sub(r'(?<=[^.])\.(?=[^.])', self.separators, pattern)

