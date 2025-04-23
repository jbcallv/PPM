def get_repositories_by_composition(self, *args, **kwargs):
        """Pass through to provider CompositionRepositorySession.get_repositories_by_composition"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._provider_session.get_repositories_by_composition(*args, **kwargs)

    def get_compositions_by_repository(self, *args, **kwargs):
        """Pass through to provider CompositionRepositorySession.get_compositions_by_repository"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._provider_session.get_compositions_by_repository(*args, **kwargs)

    def get_composition_query_from_inspector(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    composition_query_inspector_session = property(fget=get_composition_query_inspector_session)

    def get_composition_query_inspector_session_for_repository(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_composition_query_inspector_session_for_repository(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_repository_query_inspector_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    repository_query_inspector_session = property(fget=get_repository_query_inspector_session)

    def get_repository_query_inspector_session_for_repository(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_repository_query_inspector_session_for_composition(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')
