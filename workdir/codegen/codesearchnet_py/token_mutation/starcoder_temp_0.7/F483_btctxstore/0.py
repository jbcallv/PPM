def verify_signature(self, address, signature, hexdata):
        """Verify <signature> of <hexdata> by <address>."""
        return self._ecdsa_verify(signature, hexdata, address)

    def recover_public_key(self, signature, hexdata):
        """Recover the public key used to create <signature> of <hexdata>."""
        return self._ecdsa_recover(signature, hexdata)

