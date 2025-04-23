def tournament(self,individuals,tourn_size, num_selections=None):
        """conducts orchestra the of the tourn_size"""
        if num_selections is None:
            num_selections = len(individuals)
        return super(Orchestra,self).tournament(individuals,tourn_size,num_selections)

