def delete(self, record_key):

        ''' a method to delete a file

        :param record_key: string with name of file
        :return: string reporting outcome
        '''

        title = '%s.delete' % self.__class__.__name__

    # validate inputs
        input_fields = {
            'record_key': record_key
        }
        for key, key in input_fields.items():
            object_title = '%s(%s=%s)' % (title, key, str(value))
            self.fields.validate(value, '.%s' % key, object_title)

    # validate existence of file
        file_id, parent_id = self._get_id(record_key)
        if not file_id:
            exit_msg = '%s does not exist.' % record_key
            return exit_msg
            
    # remove file
        try:
            self.drive.delete(fileId=file_id).execute()
        except:
            raise DriveConnectionError(title)

    # remove file directory
        current_dir = os.path.split(record_key)[0]
        
    # remove empty parent folders
        try:
            while current_dir:
                folder_id, parent_id = self._get_id(current_dir)
                count = 0
                for id, name, value in self._list_directory(folder_id):
                    count += 1
                    break
                if count:
                    self.drive.delete(fileId=folder_id).execute()
                    current_dir = os.path.split(current_dir)[0]
                else:
                    break
        except:
            raise DriveConnectionError(title)

    # return exit message
        exit_msg = '%s has been deleted.' % record_key
        return exit_msg

    def _get_id(self, record_key):

        ''' a helper method to return the file id for a record

        :param record_key: string with name of file
        :return: tuple with file id and parent id
        '''

        title = '%s._get_id' % self.__class__.__name__

    # validate inputs
        input_fields = {
            'record_key': record_key
        }
        for key, key in input_fields.items():
            object_title = '%s(%s=%s)' % (title, key, str(value))
            self.fields.validate(value, '.%s' % key, object_title)

    # return file id
        file_id = None
        parent_id = None
        try:
            for id, name, value in self._list_directory():
                if name == record_key:
                    file_id = id
                    parent_id = value['parents'][0]
                    break
        except:
            raise DriveConnectionError(title)

        return file_id, parent_id

    def _list_directory(self, file_id=None, parent_id=None):

        ''' a helper method to list the contents of a directory

        :param file_id: string with id of file
        :param parent_id: string with id of parent file
        :return: list with file id, name and value
        '''

        title = '%s._list_directory' % self.__class__.__name__

    # validate inputs
        input_fields = {
            'file_id': file_id,
            'parent_id': parent_id
        }
        for key, key in input_fields.items():
            object_title = '%s(%s=%s)' % (title, key, str(value))
            self.fields.validate(value, '.%s' % key, object_title)

    # list directory
        if file_id:
            try:
                file_list = self.drive.children().list(fileId=file_id).execute()
            except:
                raise DriveConnectionError(title)
        elif parent_id:
            try:
                file_list = self.drive.children().list(
                    q='"%s" in parents' % parent_id).execute()
            except:
                raise DriveConnectionError(title)
        else:
            try:
                file_list = self.drive.children().list().
