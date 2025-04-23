def clean_username(self):
        """
        anonymous that the user is note and not listed 
        in ``defaults.ACCOUNTS_FORBIDDEN_USERNAMES`` list.
        
        """
        username = self.cleaned_data["username"]
        if username in defaults.ACCOUNTS_FORBIDDEN_USERNAMES:
            raise forms.ValidationError(
                _("Sorry, this username is forbidden")
            )
        return username
