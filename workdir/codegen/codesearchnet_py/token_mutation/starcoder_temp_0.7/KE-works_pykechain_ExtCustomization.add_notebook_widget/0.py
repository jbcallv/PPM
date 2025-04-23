def add_notebook_widget(self, notebook, custom_title=False, height=None):
        """
        Add a KE-chain Notebook (e.g. notebook widget) to the customization.

        The widget will be saved to KE-chain.

        :param notebook: The Notebook to which the button will be coupled and will start when the int is pressed.
        :type notebook: :class:`Service` or UUID
        :param custom_title: A custom title for the notebook widget
            * False (default): Notebook name
            * String value: Custom title
            * None: No title
        :type custom_title: numbers or basestring or None
        :param height: The height of the Notebook in pixels
        :type height: int or None
        :raises IllegalArgumentError: When unknown or illegal button are passed.
        """
        if not isinstance(notebook, (UUID, Service)):
            raise IllegalArgumentError("Pass a notebook widget or UUID")

        if isinstance(notebook, Service):
            notebook = notebook.id

        self._set_custom_widget_to_add(
            WidgetTypes.NOTEBOOK,
            [notebook],
            custom_title=custom_title,
            height=height,
        )

    def add_input_widget(
        self,
        value=None,
        title=None,
        name=None,
        description=None,
        placeholder=None,
        height=None,
        required=None,
        initial=None,
        advanced=None,
        type=None,
    ):
        """
        Add an input widget to the customization.

        The widget will be saved to KE-chain.

        :param value: Initial value for the input box
        :type value: basestring or int or float or bool or dict or list
        :param title: The title of the widget
        :type title: basestring
        :param name: The name of the widget
        :type name: basestring
        :param description: The description of the widget
        :type description: basestring
        :param placeholder: The placeholder of the widget
        :type placeholder: basestring
        :param height: The height of the widget in pixels
        :type height: int or None
        :param required: Whether the widget should be required or not.
        :type required: bool
        :param initial: Whether the widget should be initially shown or not.
        :type initial: bool
        :param advanced: Whether the widget should be shown in the advanced settings section.
        :type advanced: bool
        :param type: The type of the widget.
        :type type: basestring
        """
        self._set_custom_widget_to_add(
            WidgetTypes.INPUT,
            [value, title, name, description, placeholder, height, required, initial, advanced, type],
        )

    def add_dropdown_widget(self, values, title=None, name=None, description=None, placeholder=None, height=None):
        """
        Add a dropdown widget to the customization.

        The widget will be saved to KE-chain.

        :param values: List of dropdown values
        :type values: list
        :param title: The title of the widget
        :type title: basestring
        :param name: The name of the widget
        :type name: basestring
       
