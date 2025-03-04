def _custom_init_(self, model_name, other_name=None,log_interp = True):
        """
        Custom initialization for this model
        
        :param model_name: the name of the model, corresponding to the model of the .h5 file in the main directory
        :param other_name: (optional) the name to be used as name of the name when used in astromodels. If None 
        (default), use the same name as model_name
        :return: none
        """
        
        if other_name is None:
            
            other_name = model_name
            
        self._name = other_name
        self._log_interp = log_interp
        
        if self._log_interp:
            
            self._interpolation_function = self._interpolation_function_log
            
        else:
            
            self._interpolation_function = self._interpolation_function_lin
            
        self._load_model_from_file(model_name)
        

