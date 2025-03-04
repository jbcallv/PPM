def plot_main(self, with_caustics=False, image_names=False):
        """
        print the data two together in a single frame

        :return:
        """
        if with_caustics:
            self.plot_frame_with_caustics(image_names=image_names)
        else:
            self.plot_frame(image_names=image_names)
        return

