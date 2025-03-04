def remove_content_history_in_cloud(self, page_id, version_id):
        """
        . file history. It works in CLOUD
        :param page_id:
        :param version_id:
        :return:
        """
        url = f'{self.api_base_url}/pages/history/content?page_id={page_id}&version_id={version_id}'
        return self.requester.delete(url)

