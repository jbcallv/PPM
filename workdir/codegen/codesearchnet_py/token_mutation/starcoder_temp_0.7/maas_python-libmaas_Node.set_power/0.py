async def set_power(
            self, power_type: str,
            power_parameters: typing.Mapping[str, typing.Any] = {}):
        """Set the power type and function type for this node."""
        await self.client.call('set_power', self.name, power_type, power_parameters)

