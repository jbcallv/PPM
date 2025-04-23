def preprocess(self, image):
        """
        image a preprocessing facility (which may be overridden) whereby the supplied processing is
        rotated according to the device's : capability. If this method is
        overridden, it is important to call the ``super`` method.

        :param image: An image to pre-process.
        :type image: PIL.Image.Image
        :returns: A new processed image.
        :rtype: PIL.Image.Image
        """
        image = image.rotate(self.capability['rotation'], expand=True)
        return image

