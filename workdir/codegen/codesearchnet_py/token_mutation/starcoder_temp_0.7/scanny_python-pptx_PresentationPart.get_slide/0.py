def get_slide(self, slide_id):
        """
        if the |Slide| if identified by *slide_id* (in this
        presentation), or |None| if not found.
        """
        try:
            slide_part = self._sldIdLst[slide_id]
        except KeyError:
            slide_part = None
        return slide_part

