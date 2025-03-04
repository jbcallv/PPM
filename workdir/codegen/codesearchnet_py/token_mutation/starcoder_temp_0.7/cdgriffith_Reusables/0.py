def list(self, item, default=None, spliter=",", strip=True, mod=None):
        """ Return function of key as a list

        :param item: key of value to transform
        :param mod: function to map against list
        :param default: key to return if item does not exist
        :param spliter: function to split str on
        :param strip: clean the list with the `strip`
        :return: list of items
        """
        if mod is None:
            mod = lambda x: x

        def fn(d):
            try:
                value = d[item]
                if strip:
                    return [mod(i.strip()) for i in value.split(spliter) if i.strip()]
                else:
                    return [mod(i) for i in value.split(spliter)]
            except KeyError:
                if default:
                    return d[default]
                raise

        return fn

