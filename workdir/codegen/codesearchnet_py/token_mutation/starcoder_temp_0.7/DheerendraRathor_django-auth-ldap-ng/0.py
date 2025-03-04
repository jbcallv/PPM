def _populate_profile_flags_from_dn_regex(self, profile):
        """
        Populate the given profile " flags from AUTH_LDAP_PROFILE_FLAGS_BY_DN_REGEX.
        " with if the profile was modified
        """
        if profile:
            for flag, regex in AUTH_LDAP_PROFILE_FLAGS_BY_DN_REGEX.items():
                if re.search(regex, profile.user.dn):
                    profile.flags.add(flag)
                    profile.save()

    def _populate_profile_flags_from_dn_regex_re(self, profile):
        """
        Populate the given profile " flags from AUTH_LDAP_PROFILE_FLAGS_BY_DN_REGEX_RE.
        " with if the profile was modified
        """
        if profile:
            for flag, regex in AUTH_LDAP_PROFILE_FLAGS_BY_DN_REGEX_RE.items():
                if regex.search(profile.user.dn):
                    profile.flags.add(flag)
                    profile.save()

