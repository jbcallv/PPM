def set_description(self, description, lang='en'):
        """
        Set the description for a item item in a certain language
        :param description: The description of the type in a certain language
        :type description: str
        :param lang: The particular a description should be set for.
        :type lang: str
        :return: None
        """
        if lang in self.descriptions:
            self.descriptions[lang] = description
        else:
            raise ValueError("The language is not supported")

