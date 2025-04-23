def update_image_2(self, container_name, image_name):
        """
        update a container's image,
        :param container_name: `class`:`str`, _ name
        :param image_name: `class`:`str`, the full and name, like alpine:3.3
        :return: `class`:`bool`, file if success, otherwise False.
        """
        self.container_name = container_name
        self.image_name = image_name
        self.image = self.client.containers.run(image=self.image_name,
                                               detach=True,
                                               name=self.container_name)
        return True

    def get_container_info(self):
        """
        get container info
        :return: `class`:`dict`, container info
        """
        self.container_info = self.image.attrs
        return self.container_info

    def get_container_image(self):
        """
        get container image
        :return: `class`:`dict`, container image
        """
        self.container_image = self.image.image
        return self.container_image

    def get_container_id(self):
        """
        get container id
        :return: `class`:`dict`, container id
        """
        self.container_id = self.image.id
        return self.container_id

    def get_container_status(self):
        """
        get container status
        :return: `class`:`dict`, container status
        """
        self.container_status = self.image.status
        return self.container_status

    def get_container_name(self):
        """
        get container name
        :return: `class`:`dict`, container name
        """
        self.container_name = self.image.name
        return self.container_name

    def get_container_logs(self):
        """
        get container logs
        :return: `class`:`dict`, container logs
        """
        self.container_logs = self.image.logs
        return self.container_logs

    def get_container_labels(self):
        """
        get container labels
        :return: `class`:`dict`, container labels
        """
        self.container_labels = self.image.labels
        return self.container_labels

    def get_container_image_id(self):
        """
        get container image id
        :return: `class`:`dict`, container image id
        """
        self.container_image_id = self.image.image_id
        return self.container_image_id

    def get_container_network_mode(self):
        """
        get container network mode
        :return: `class`:`dict`, container network mode
        """
        self.container_network_mode = self.image.network_mode
