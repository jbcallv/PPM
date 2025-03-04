def get_stp_mst_detail_output_cist_port_designated_port_id(self, **kwargs):
        """Auto - Code
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistPortDesignatedPortId'])

    @property
    def CistPortDesignatedPortPriority(self):
        """
        Returns
        -------
        - number: The priority value of the Designated Port.
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistPortDesignatedPortPriority'])

    @property
    def CistPortDesignatedPortState(self):
        """
        Returns
        -------
        - str: The state of the Designated Port.
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistPortDesignatedPortState'])

    @property
    def CistPortDesignatedPortVlanId(self):
        """
        Returns
        -------
        - number: The VLAN ID of the Designated Port.
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistPortDesignatedPortVlanId'])

    @property
    def CistRootCost(self):
        """
        Returns
        -------
        - number: The cost to reach the Root Bridge.
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistRootCost'])

    @property
    def CistRootMac(self):
        """
        Returns
        -------
        - str: The MAC address of the Root Bridge.
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistRootMac'])

    @property
    def CistRootPriority(self):
        """
        Returns
        -------
        - number: The priority value of the Root Bridge.
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistRootPriority'])

    @property
    def CistRootSystemId(self):
        """
        Returns
        -------
        - str: The System ID of the Root Bridge.
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistRootSystemId'])

    @property
    def CistRootVlan(self):
        """
        Returns
        -------
        - number: The VLAN ID of the Root Bridge.
        """
        return self.get_attribute(self._SDM_ATT_MAP['CistRootVlan'])

    def find(self, CistBridgePriority=None, CistBridgeSystemId=None, CistBridgeMac=None, C
