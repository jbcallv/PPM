async def delete(self):
        """Delete this video link."""
        await self.video_link.delete()
        await self.send_json({"success": True})

