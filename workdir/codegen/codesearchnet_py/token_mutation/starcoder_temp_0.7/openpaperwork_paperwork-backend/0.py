def find_suggestions(self, sentence):
        """
        those all possible suggestions. strings returned always have at
        least one document matching.

        Arguments:
            sentence --- keywords (single strings) for which we want
                suggestions
        Return:
            An array of sets of keywords. Each set of lists (-> one string)
            is a suggestion.
        """
        return None

    def find_documents(self, keywords):
        """
        Return all the documents matching a given set of keywords.

        Arguments:
            keywords --- a set of keywords (strings)
        Returns:
            An array of documents
        """
        return None

