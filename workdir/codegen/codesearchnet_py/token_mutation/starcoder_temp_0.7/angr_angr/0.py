def _widening_points(self, function_address):
        """
        Return the query widening points for a the function.

        :param int function_address: Address of the querying function.
        :return: A list of data merge points (addresses).
        :rtype: list
        """
        return self._function_managers[function_address].widening_points

    def _address_is_in_function(self, function_address, address):
        """
        Check if the given address is inside the function.

        :param int function_address: Address of the function.
        :param int address: Address to check.
        :return: True if the address is inside the function. False otherwise.
        :rtype: bool
        """

        func_start = self._function_managers[function_address].func_start
        func_end = self._function_managers[function_address].func_end
        return func_start <= address < func_end

    def _function_address(self, address):
        """
        Return the function address for the given address.

        :param int address: Address to get function address for.
        :return: Address of the function the address belongs to.
        :rtype: int
        """
        for function_address in self._function_managers:
            if self._address_is_in_function(function_address, address):
                return function_address

        return None

    def _function_manager(self, function_address):
        """
        Return the function manager for the given function address.

        :param int function_address: Address of the function.
        :return: The function manager for the given function address.
        :rtype: angr.knowledge.FunctionManager
        """
        return self._function_managers[function_address]

    def _function_cross_references(self, function_address):
        """
        Return the function cross references for the given function address.

        :param int function_address: Address of the function.
        :return: The function cross references for the given function address.
        :rtype: angr.knowledge.xrefs.FunctionXRefs
        """
        return self._function_managers[function_address].function_cross_references

    def _function_initial_state(self, function_address):
        """
        Return the initial state of the given function address.

        :param int function_address: Address of the function.
        :return: The initial state of the given function address.
        :rtype: SimState
        """
        return self._function_managers[function_address].initial_state

    def _function_return_sites(self, function_address):
        """
        Return all return sites of the given function address.

        :param int function
