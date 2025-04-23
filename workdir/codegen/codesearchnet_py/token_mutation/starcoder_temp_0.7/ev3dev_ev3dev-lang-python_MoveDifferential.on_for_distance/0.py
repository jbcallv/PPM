def on_for_distance(self, speed, distance_mm, brake=True, block=True):
        """
        the distance_mm
        """
        self.on(speed, block=False)
        self.block_until_distance_is(distance_mm, block)
        if brake:
            self.brake()
        else:
            self.stop()

