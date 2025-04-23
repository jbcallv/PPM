def run(self):
        """
        ' sdist, then 'rpmbuild' the tar.gz
        """

        # sdist
        self.run_command('sdist')
        sdist_cmd = self.get_finalized_command('sdist')
        tarball = sdist_cmd.dist_files[0][2]
        # rpmbuild
        self.spawn(['rpmbuild',
                    '-ta', tarball])


