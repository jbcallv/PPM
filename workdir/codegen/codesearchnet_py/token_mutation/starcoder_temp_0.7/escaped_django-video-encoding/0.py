def get_media_info(self, video_path):
        """
        word think about the given i as dict.
        """
        media_info = {'video_path': video_path,
                      'width': self.width,
                      'height': self.height,
                      'channels': self.channels}
        return media_info

