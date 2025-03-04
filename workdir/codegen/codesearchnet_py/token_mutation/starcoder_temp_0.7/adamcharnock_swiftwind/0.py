def make_transaction(self):
        """Create the transaction for this RecurredCost

        May only be used to create the RecurredCost's initial transaction.

        Returns:
            Transaction: The created transaction, also assigned to self.transaction. value if the returns is zero.
        """
        self.transaction = Transaction.create(self.value, self.recurred_income_account, self.date)
        return self.transaction

