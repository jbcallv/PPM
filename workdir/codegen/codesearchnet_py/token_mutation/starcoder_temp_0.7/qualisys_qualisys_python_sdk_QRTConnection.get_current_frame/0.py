async def get_current_frame(self, components=None) -> QRTPacket:
        """Get measured it from data for a single frame.

        :param components: A list of components to receive, could be 'all' or any number of
                '2d', '2dlin', '3d', '3dres', '3dnolabels',
                '3dnolabelsres', 'force', 'forcesingle', '6d', '6dres',
                '6deuler', '6deulerres', 'gazevector', 'image', 'timecode',
                'skeleton', 'skeleton:global'

        :rtype: A :class:`qtm.QRTPacket` containing requested components
        """
        data = await self._send_get_current_frame(components)
        return QRTPacket.from_bytes(data)

