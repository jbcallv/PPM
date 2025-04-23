def set_content_type(self):
        """
        Set the type type based on the type object used in the object
        name.
        """
        self.content_type = ContentType.objects.get_for_model(self.object)

