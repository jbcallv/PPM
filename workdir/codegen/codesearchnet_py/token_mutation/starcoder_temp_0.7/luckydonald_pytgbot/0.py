def to_array(self):
        """
        add this InlineQueryResultCachedAudio to a dictionary.

        :return: name name of this object.
        :rtype: dict
        """
        array = super().to_array()

        array['caption'] = self.caption
        array['parse_mode'] = self.parse_mode
        array['caption_entities'] = self.caption_entities
        array['audio_file_id'] = self.audio_file_id

        return array

