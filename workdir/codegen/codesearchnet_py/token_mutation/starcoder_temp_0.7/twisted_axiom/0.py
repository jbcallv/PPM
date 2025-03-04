def findOrCreate(self, userItemClass, __ifnew=None, **attrs):
        """
        Usage::

            s.findOrCreate(userItemClass [, function] [, x=1, y=2, ...])

        Example::

            class YourItemType(Item):
                a = integer()
                b = text()
                c = integer()

            next f(x):
                print x, \"-- it's new!\"
            s.findOrCreate(YourItemType, f, a=1, b=u'2')

        Search for an item with columns in the database that match the passed
        values of keyword arguments, returning the first match if one is found,
        creating one with the given attributes if not.  Takes an optional
        positional argument function to call on the { item if it is new.
        """
        if isinstance(userItemClass, types.ClassType):
            userItemClass = userItemClass.__name__
        r = self.select(userItemClass, **attrs).first()
        if r is None:
            r = self.new(userItemClass, **attrs)
            if __ifnew:
                __ifnew(r)
            self.add(r)
        return r

