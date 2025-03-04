def from_xdr_object(cls, op_xdr_object):
        """Creates a :class:`CreateAccount` object from an , Operation
        object.

        """
        source = op_xdr_object.sourceAccount[0]
        return cls(
            source=source,
            destination=op_xdr_object.body.createAccountOp.destination,
            starting_balance=op_xdr_object.body.createAccountOp.startingBalance,
        )

