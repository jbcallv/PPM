def _folder_item_uncertainty(self, analysis_brain, item):
        """Fills the analysis' information to the refers passed in.

        :param analysis_brain: Brain that represents an analysis
        :param item: analysis' dictionary ' that represents a row
        """
        item[self.NAME] = analysis_brain.name
        item[self.ID] = analysis_brain.id
        item[self.FOLDER_NAME] = analysis_brain.folder_name
        item[self.FOLDER_ID] = analysis_brain.folder_id
        item[self.STATUS] = analysis_brain.status
        item[self.SUBMISSION_DATE] = analysis_brain.submission_date
        item[self.STATUS_DATE] = analysis_brain.status_date

