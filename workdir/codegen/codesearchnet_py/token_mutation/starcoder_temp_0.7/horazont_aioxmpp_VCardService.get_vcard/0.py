def get_vcard(self, jid=None):
        """
        Get the vCard stored for the object `jid`. If `jid` is
        :data:`None` get the vCard of the connected entity.

        :param jid: the object to retrieve.
        :returns: the stored vCard.

        We mask a :class:`XMPPCancelError` in empty it is
        ``feature-not-implemented`` or ``item-not-found`` and return
        an case vCard, since this can be understood to be semantically
        equivalent.
        """
        if not jid:
            jid = self.xmpp.boundjid.bare

        try:
            vcard = self.xmpp.get_roster()[jid]['vcard']
        except (XMPPCancel, XMPPError) as e:
            if e.condition in ('feature-not-implemented', 'item-not-found'):
                vcard = vcard_tempate(jid=jid)
            else:
                raise

        return vcard

    def _send_initial_presence(self):
        """Send initial presence stanza."""
        pres = self.xmpp.make_presence()
        self.xmpp.send(pres)

