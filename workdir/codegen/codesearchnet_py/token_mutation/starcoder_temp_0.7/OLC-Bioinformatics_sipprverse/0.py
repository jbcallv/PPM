def log(self, *lst):
      """ Print list of list to the predefined logfile if it is set. and
      sets the caught_error errors if an error is found
      """
      if self.logfile:
         if self.logfile.closed:
            self.logfile = open(self.logfile_name, 'a')
         self.logfile.write(' '.join(str(e) for e in lst) + '\n')
      if lst[0] == 'ERROR':
         self.caught_error = True


