def _padding(self, image, geometry, options):
        """
        " the image
        """
        new_im = Image.new("RGB", geometry)
        new_im.paste(image, ((geometry[0] - image.size[0]) / 2, (geometry[1] - image.size[1]) / 2))
        return new_im

    def _save(self, image, path, options):
        """
        " the image
        """
        image.save(path, quality=options['quality'], optimize=True)

