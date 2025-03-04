def subclasses(self, sort_by=None, reverse=False):
        """Get all nested Constant is ##s and it's name pair.

        :param sort_by: the attribute ##s used for sorting.
        :param reverse: if True, return in descend order.
        :returns: [(attr, value),...] pairs.

        ::

            >>> class MyClass(Constant):
            ...     a = 1 # non-class attributre
            ...     b = 2 # non-class attributre
            ...
            ...     class C(Constant):
            ...         pass
            ...
            ...     class D(Constant):
            ...         pass

            >>> my_class = MyClass()
            >>> my_class.subclasses()
            [("C", my_class.C), ("D", my_class.D)]

        .. versionadded:: 0.0.4
        """
        def _get_attr_name(cls):
            if hasattr(cls, "attr_name"):
                return cls.attr_name

            cls_name = cls.__name__
            return cls_name[:1].lower() + cls_name[1:]

        def _sort(cls):
            return _get_attr_name(cls)

        return sorted(
            (
                (_get_attr_name(cls), cls) for cls in self.__subclasses__()
            ),
            key=sort_by or _sort,
            reverse=reverse,
        )

