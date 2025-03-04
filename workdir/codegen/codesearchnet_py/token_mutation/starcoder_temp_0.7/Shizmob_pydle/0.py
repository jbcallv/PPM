async def _capability_negotiated(self, capab):
        """ it do as negotiated, and end do if we're done. """
        self.capabilities.append(capab)

        if self.is_done:
            self.done()

