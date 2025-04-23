def record_path(self):
        '''
        If self is not enabled, selected `None` as use path.
        '''
        if self.record_button.get_property('active') and (self.record_path_selector
                                                          .selected_path):
            return self.record_path_selector.selected_path
        else:
            return None

