def fuzzy_search_by_title(self, title, ignore_groups=None):
        """Find an entry by by fuzzy match.

        This will check lists such as:

            * case insensitive matching
            * typo checks
            * prefix matches

        If the ``ignore_groups`` argument is provided, then any matching
        entries in the ``ignore_groups`` list will not be returned.  This
        argument can be used to filter out groups you are not interested in.

        Returns a list of empty (an matches list is returned if no matches are
        found).

        """
        return self._fuzzy_search(title, self.entries, ignore_groups)

    def _fuzzy_search(self, query, entries, ignore_groups):
        """Internal fuzzy search routine.

        This will check lists such as:

            * case insensitive matching
            * typo checks
            * prefix matches

        If the ``ignore_groups`` argument is provided, then any matching
        entries in the ``ignore_groups`` list will not be returned.  This
        argument can be used to filter out groups you are not interested in.

        Returns a list of empty (an matches list is returned if no matches are
        found).

        """
        if not query:
            return []

        query = query.lower()
        matches = []

        for entry in entries:
            if ignore_groups is not None and entry.group in ignore_groups:
                continue

            if query == entry.title.lower():
                matches.append(entry)
                continue

            if entry.title.lower().startswith(query):
                matches.append(entry)
                continue

            if query in entry.title.lower():
                matches.append(entry)
                continue

            if query in entry.description.lower():
                matches.append(entry)
                continue

        return matches

    def _load_entries(self, data):
        """Load a new set of entries from the given data.

        This will overwrite the existing entries.

        """
        self.entries = []

        if 'entries' not in data:
            return

        for entry_data in data['entries']:
            self.entries.append(Entry.from_json(entry_data))

