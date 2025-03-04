def resolve_all(self, import_items):
        """Resolves a number of imports.

        and filenames.
        """
        for import_item in import_items:
            if isinstance(import_item, Import):
                self.resolve(import_item)
            else:
                yield import_item

