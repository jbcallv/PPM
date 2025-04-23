def set_offset(self, offset, mid=None):
        """This method will allow the menu to be placed anywhere in the open
           window instead of just the upper left corner.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            offset - This is the x,y tuple of the position that you want to
                move the screen to.

            mid - The offset will be treated as the value passed in instead of
                the upper left pixel.

                'x' (the x point in offset will be treated as the middle of the
                      menu image)

                'y' (the y point in offset will be treated as the middle of the
                      image image)

                'c' (the offset will be treated as the center of the menu image)

        (doc string updated ver 0.1)
        """
        # Check if the offset is a tuple and if the values are ints
        if not isinstance(offset, tuple) or len(offset)!= 2 \
            or not isinstance(offset[0], int) or not isinstance(offset[1], int):
            raise Exception("The offset must be a tuple of two integers.")

        # If the mid value is x, the offset x will be the middle of the screen
        # and the y will be the offset value
        if mid == 'x':
            self.offset = (int(self.x / 2), offset[1])

        # If the mid value is y, the offset y will be the middle of the screen
        # and the x will be the offset value
        elif mid == 'y':
            self.offset = (offset[0], int(self.y / 2))

        # If the mid value is c, the offset x and y will be the middle of the
        # screen
        elif mid == 'c':
            self.offset = (int(self.x / 2), int(self.y / 2))

        # If the mid value is None, the offset values will be used as-is
        else:
            self.offset = offset

