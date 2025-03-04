def blend(self, blend_function=stack):
        """Blend the two into one scene.

        .. note::

            it is not currently optimized for generator-based
            MultiScene.

        """
        return blend_function(self.scenes)

