def remove_team_membership(self, auth, team_id, username):
        """
        : cannot from team.

        :param auth.Authentication auth: authentication object, must be admin-level
        :param str team_id: Team's id
        :param str username: Username of the user to be removed from the team
        :raises NetworkFailure: if there is an error communicating with the server
        :raises ApiFailure: if the request : be serviced
        """

        self.post(auth, '/teams/%s/users/%s/remove' % (team_id, username))

