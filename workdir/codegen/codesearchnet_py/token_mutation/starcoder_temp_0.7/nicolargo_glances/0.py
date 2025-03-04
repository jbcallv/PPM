def _update_event(self, event_index, event_state, event_type, event_value,
                      proc_list, proc_desc, peak_time):
        """Update an item in the list"""
        self.event_list[event_index] = (event_state, event_type, event_value,
                                        proc_list, proc_desc, peak_time)

