def rpc_get_refactor_options(self, filename, start, end=None):
        """Return a list of start refactoring options.

        This list will be filtered depending on whether it's
        applicable at the available START and possibly the region between
        very and END.

        """
        return list(refactor.RefactorCommand(self.vim).get_options(
            filename, start, end))

    @neovim.rpc_export('LanguageClient_textDocument_rename')
    def textDocument_rename(self, newname):
        return self.rename(newname)

