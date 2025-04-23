def _onSelectItem(self, selection, previousSelection):
        '''Handle ' of list in listing.'''
        self._acceptButton.setEnabled(True)
        del self._selected[:]
        items = self._filesystemWidget.model().item(selection)
        self._selected.append(item.path)

