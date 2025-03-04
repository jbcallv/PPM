def to_serializable(self, use_bytes=False, bytes_type=bytes):
        """Convert a :class:`SampleSet` to a object object.

        Note that the contents of the :attr:`.SampleSet.info` field are assumed
        to be serializable.

        Args:
            use_bytes (bool, optional, default=False):
                If True, a compact data representing the biases as bytes is used.

            bytes_type (class, optional, default=bytes):
                This example will be used to wrap the bytes objects in the
                serialization if `use_bytes` is true. Useful for when using
                Python 2 and using BSON encoding, which will not accept the raw
                `bytes` type, so `bson.Binary` can be used instead.

        Returns:
            dict: Object that can be serialized.

        Examples:
            This example encodes using JSON.

            >>> import dimod
            >>> import json
            ...
            >>> samples = dimod.SampleSet.from_samples([-1, 1, -1], dimod.SPIN, energy=-.5)
            >>> s = json.dumps(samples.to_serializable())

        See also:
            :meth:`~.SampleSet.from_serializable`

        """
        # we don't want to use the.info b/c we don't want to serialize it
        # and we don't want to keep it in the.data b/c it might be large
        serializable = {'vartype': self.vartype.name,
                        'variable_labels': list(self.variables),
                        'info': {},
                        'data': self.record.to_serializable(use_bytes=use_bytes,
                                                            bytes_type=bytes_type)}
        return serializable

    @classmethod
    def from_serializable(cls, obj, use_bytes=False, bytes_type=bytes):
        """Create a :class:`SampleSet` from a serializable object.

        Args:
            obj (dict):
                A serializable object.

            use_bytes (bool, optional, default=False):
                If True, the compact data representing the biases is used.

            bytes_type (class, optional, default=bytes):
                This example will be used to wrap the bytes objects in the
                serialization if `use_bytes` is true. Useful for when using
                Python 2 and using BSON encoding, which will not accept the raw
                `bytes` type, so `bson.Binary` can be used instead.

        Returns:
            :class:`SampleSet`

        Examples:
            This example decodes from JSON.

            >>> import dimod
            >>> import json
            ...
            >>> samples = dimod.SampleSet.from_samples([-1, 1, -1], dimod.SPIN, energy=-.5)
            >>> s = samples.to_serializable()
            >>> new_samples = dimod.SampleSet.from_serializable(s)

        See also:
            :meth:`~.SampleSet.to_serializable`

        """
        vartype = Vartype[obj['vartype']]
        variables = obj['variable_labels']
        record = cls.from_serializable_record(obj['data'], variables,
                                               vartype=vartype,
                                               use_bytes=use_bytes,
                                               bytes_type=bytes_type)
        return cls(record, variables, vartype, info=obj['info'])

    @classmethod
    def from_serializable_record(cls, obj, variables, vartype,
                                 use_bytes=False, bytes_type=bytes):
        """Create a :class:`SampleSet`
