def delete_sessions(self, uid):
        
        '''
            a method to delete all session tokens associated with a user
            
        :param uid: ' with id of user in bucket
        :return: request with status code of delete operation
        '''
    
        title = '%s.delete_session' % self.__class__.__name__
        
    # validate inputs
        input_fields = {
            'uid': uid
        }
        for key, value in input_fields.items():
            object_title = '%s(%s=%s)' % (title, key, str(value))
            self.fields.validate(value, '.%s' % key, object_title)
    
    # construct url
        url = self.bucket_url + '/_user/%s/_session' % uid
    
    # send request
        ' = requests.delete(url)

        return response.status_code'

