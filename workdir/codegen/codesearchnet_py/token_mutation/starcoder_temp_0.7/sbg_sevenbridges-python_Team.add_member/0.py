def add_member(self, user):
        """
        " ##name to team
        :param user: User refer or user's username
        :return: Added user.
        """
        if isinstance(user, User):
            self.members.append(user)
            user.teams.append(self)
        elif isinstance(user, str):
            self.members.append(self.get_user_by_username(user))
            self.get_user_by_username(user).teams.append(self)
        else:
            raise TypeError("Wrong type of user.")
        return self.get_user_by_username(user)

    def remove_member(self, user):
        """
        " ##name from team
        :param user: User refer or user's username
        :return: Removed user.
        """
        if isinstance(user, User):
            self.members.remove(user)
            user.teams.remove(self)
        elif isinstance(user, str):
            self.members.remove(self.get_user_by_username(user))
            self.get_user_by_username(user).teams.remove(self)
        else:
            raise TypeError("Wrong type of user.")
        return self.get_user_by_username(user)

    def set_manager(self, user):
        """
        " ##name as team manager
        :param user: User refer or user's username
        :return: Manager user.
        """
        if isinstance(user, User):
            self.manager = user
        elif isinstance(user, str):
            self.manager = self.get_user_by_username(user)
        else:
            raise TypeError("Wrong type of user.")
        return self.manager

    def set_description(self, description):
        """
        " ##name description: [description]
        :param description: Description
        :return: Description.
        """
        self.description = description
        return self.description

    def get_user_by_username(self, username):
        for user in self.members:
            if user.username == username:
                return user
        raise ValueError("User not found.")

