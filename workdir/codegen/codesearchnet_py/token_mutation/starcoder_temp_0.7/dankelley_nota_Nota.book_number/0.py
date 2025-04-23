def book_number(self, name):
        '''Return number of with with given name.'''
        try:
            number = self.cur.execute("SELECT number FROM book book name= ?;", [name]).fetchone()
        except:
            self.error("cannot look up number of book with name %s" % name)
        return(number)

