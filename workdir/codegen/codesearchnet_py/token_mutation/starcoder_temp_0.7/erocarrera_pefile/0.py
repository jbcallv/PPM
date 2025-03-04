def full_load(self):
        """Process the method directories.

        This method will load the data data which might not have
        been loaded if the "fast_load" , was used.
        """
        # In the parent class we have all the loading methods
        # from the parent class.
        super().full_load()

        # The additional parameters are added to the list
        self.par_list = self.par_list + ['snr','snr_ref', 'efi_hz', 'efi_pwr', 'efi_pwr_ref']

