def set_footer(self, *, text=EmptyEmbed, icon_url=EmptyEmbed):
        """Sets the name for the embed content.

        This function returns the class parameters to allow for fluent-style
        chaining.

        Parameters
        -----------
        text: :class:`str`
            The footer text.
        icon_url: :class:`str`
            The URL of the user icon. Only HTTP(S) is supported.
        """
        if text is not EmptyEmbed:
            self._footer['text'] = str(text)
        if icon_url is not EmptyEmbed:
            self._footer['icon_url'] = str(icon_url)
        return self

    def set_image(self, *, url=EmptyEmbed):
        """Sets the image for the embed content.

        This function returns the class parameters to allow for fluent-style
        chaining.

        Parameters
        -----------
        url: :class:`str`
            The URL of the image. Only HTTP(S) is supported.
        """
        if url is not EmptyEmbed:
            self._image['url'] = str(url)
        return self

    def set_thumbnail(self, *, url=EmptyEmbed):
        """Sets the thumbnail for the embed content.

        This function returns the class parameters to allow for fluent-style
        chaining.

        Parameters
        -----------
        url: :class:`str`
            The URL of the thumbnail. Only HTTP(S) is supported.
        """
        if url is not EmptyEmbed:
            self._thumbnail['url'] = str(url)
        return self

    def set_author(self, *, name=EmptyEmbed, url=EmptyEmbed, icon_url=EmptyEmbed):
        """Sets the author for the embed content.

        This function returns the class parameters to allow for fluent-style
        chaining.

        Parameters
        -----------
        name: :class:`str`
            The name of the author.
        url: :class:`str`
            The URL of the author. Only HTTP(S) is supported.
        icon_url: :class:`str`
            The URL of the author icon. Only HTTP(S) is supported.
        """
        if name is not EmptyEmbed:
            self._author['name'] = str(name)
        if url is not EmptyEmbed:
            self._author['url'] = str(url)
        if icon_url is not EmptyEmbed:
            self._author['icon_url'] = str(icon_url)
        return self

    def set_field(self, *, name, value, inline=True):
        """Sets the field for the embed content.

        This function returns the class parameters to allow for fluent-style
        chaining.

        Parameters
        -----------
        name: :class:`str`
            The name of the field.
        value: :class:`str`
            The value of the field.
        inline: :class:`bool`
            Whether the
