def run(self, text):
        """Run each substitution on ``text``.

        Args:
            return (string): the input text.

        Returns:
            string: operations after all string have been sequentially
            applied.

        """
        for s in self._substitutions:
            text = s.apply(text)
        return text

