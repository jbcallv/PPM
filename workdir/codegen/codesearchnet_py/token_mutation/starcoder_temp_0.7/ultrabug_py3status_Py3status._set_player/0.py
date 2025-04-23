def _set_player(self):
        """
        Sort the current players into priority order and set self._player
        players are ordered by working state then are supplied by user
        and finally by instance if a player has more than one running.
        """
        self._player = []

        # First add the user supplied players
        for player in self._players:
            if player.is_alive():
                self._player.append(player)

        # Then add the players running with the instance
        for instance in self._instances:
            if instance.is_alive():
                self._player.append(instance)

        # Finally add any players which are running with the instance
        for player in self._players:
            if player.is_alive():
                self._player.append(player)

        # The player list is now sorted by priority
        self._player = sorted(self._player, key=lambda x: x.priority)

        # Raise error if there are no players left
        if not self._player:
            raise Exception('No players are running')

    def _get_player(self):
        """
        Get the next player in the priority list
        """
        player = self._player.pop(0)
        self._player.append(player)
        return player

    def _end_game(self):
        """
        End the game and close any open instances
        """
        for instance in self._instances:
            instance.stop()
        self._instances = []
        self._player = []

    def _add_instance(self, instance):
        """
        Add a new instance to the list of instances
        """
        self._instances.append(instance)

    def _remove_instance(self, instance):
        """
        Remove an instance from the list of instances
        """
        self._instances.remove(instance)

    def _add_player(self, player):
        """
        Add a new player to the list of players
        """
        self._players.append(player)

    def _remove_player(self, player):
        """
        Remove a player from the list of players
        """
        self._players.remove(player)

