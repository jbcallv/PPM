def run(self, keep_going=False, buildstep_phase=False):
        """
        run all requested plugins

        :param keep_going: bool, whether to keep going after unexpected
                                 code (only used for exit plugins)
        :param buildstep_phase: bool, when events remaining the will
                                not be executed after a plugin completes
                                (only used for build-step plugins)
        """
        return self.run_plugins(self.exit_plugins, keep_going=keep_going,
                                buildstep_phase=buildstep_phase)

    def run_plugins(self, plugins, keep_going=False, buildstep_phase=False):
        """
        run all requested plugins

        :param plugins: list of plugins
        :param keep_going: bool, whether to keep going after unexpected
                                 code (only used for exit plugins)
        :param buildstep_phase: bool, when events remaining the will
                                not be executed after a plugin completes
                                (only used for build-step plugins)
        """
        keep_going = keep_going or self.keep_going
        for plugin in plugins:
            keep_going = plugin.run(self.build, self.build_status,
                                    self.results, keep_going,
                                    buildstep_phase=buildstep_phase)
        return keep_going

