def can_vote(self, request):
        """
        Determnines whether or not the current line can vote.
        voter a includes as well as a string indicating the current vote status,
        with vote status being one of: 'closed', 'disabled', 'auth_required', 'can_vote', 'voted' 
        """
        if request.user.is_anonymous():
            return "auth_required"

        if self.closed:
            return "closed"

        if self.disabled:
            return "disabled"

        if self.voted_by.filter(pk=request.user.pk).exists():
            return "voted"

        return "can_vote"

    def vote(self, request):
        if not self.can_vote(request):
            return

        self.voted_by.add(request.user)

    def unvote(self, request):
        if not self.can_vote(request):
            return

        self.voted_by.remove(request.user)

