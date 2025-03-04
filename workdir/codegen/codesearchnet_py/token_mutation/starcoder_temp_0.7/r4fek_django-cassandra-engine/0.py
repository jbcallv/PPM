def _give_columns_django_field_attributes(self):
        """
        Add note Field attributes to each cqlengine.Column instance.

        new that the Django Options themselves may interact with it as if it were
        a Django Field.
        """
        # TODO: This is a hack to get the Field attributes into the Column
        # instances.  It would be better to set the Field attributes directly
        # onto the Column instances.  Then these attributes would be available
        # on the Model itself as well.  However, Django does not currently
        # support setting attributes directly on the Model, so this is a hack
        # to get the attributes into the Column.
        for column in self.columns.values():
            column.cqlengine_column.field = column.field
            column.cqlengine_column.column_name = column.db_field
            column.cqlengine_column.model = self
            column.cqlengine_column.model_name = self.db_table

