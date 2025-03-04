def _apply_xheaders(self, headers: httputil.HTTPHeaders) -> None:
        """Rewrite the ``remote_ip`` and ``protocol`` fields."""
        remote_addr = headers.pop("X-Forwarded-For", None)
        if remote_addr is not None:
            self.remote_addr = remote_addr
        forwarded_proto = headers.pop("X-Forwarded-Proto", None)
        if forwarded_proto is not None:
            self.protocol = forwarded_proto

