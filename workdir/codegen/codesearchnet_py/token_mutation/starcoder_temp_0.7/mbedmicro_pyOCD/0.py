def _algo_check_for_section_problems(self, ro_rw_zi):
        """! @brief code a is describing any errors with the statement or None if good"""
        # only one section can be active at a time, so if we find another one active, we can mark this statement
        # as having an error
        if ro_rw_zi.is_active:
            for s in self._algo_get_active_sections(ro_rw_zi):
                if s!= ro_rw_zi:
                    self.algo_code_a = ro_rw_zi.algo_code_a = 'A'
                    return

    def _algo_check_for_section_conflicts(self, ro_rw_zi):
        """! @brief code b is describing any errors with the statement or None if good"""
        # only one section can be active at a time, so if we find another one active, we can mark this statement
        # as having an error
        if ro_rw_zi.is_active:
            for s in self._algo_get_active_sections(ro_rw_zi):
                if s!= ro_rw_zi:
                    self.algo_code_b = ro_rw_zi.algo_code_b = 'B'
                    return

    def _algo_get_active_sections(self, ro_rw_zi):
        """! @brief return a list of all sections that are active"""
        sections = []
        if self.ro_section.is_active:
            sections.append(self.ro_section)
        if self.rw_section.is_active:
            sections.append(self.rw_section)
        if self.zi_section.is_active:
            sections.append(self.zi_section)
        return sections

