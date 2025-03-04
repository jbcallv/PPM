def create_instance(self, nova, image_name, instance_name, flavor):
        """Create the specified instance."""
        image = nova.glance.find_image(image_name)
        instance = nova.servers.create(instance_name, image, flavor)
        return instance

