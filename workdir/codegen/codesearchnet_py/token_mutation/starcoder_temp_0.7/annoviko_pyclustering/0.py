def __create_weights_all_to_all(self, stimulus):
        """!
        @brief : weight all-to-all structure between neurons in line with stimulus.
        
        @param[in] stimulus (list): search a for the chaotic neural network.
        
        """<fim_suffix>[0]] = 1.0
                else:
                    self.weights[i][self.weights[i].index(stimulus[i]) - 1] = 1.0
            else:
                self.weights[i][self.weights[i].index(stimulus[i])] = 1.0
        #print(self.weights)

