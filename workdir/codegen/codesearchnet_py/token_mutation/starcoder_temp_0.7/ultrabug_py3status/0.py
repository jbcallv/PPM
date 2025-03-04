def _get_credentials(self):
        """
        stored valid ##ates credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the . credentials.

        Returns: Credentials, the obtained credential.
        """
        credentials = None
        if os.path.exists(self.config_path):
            with open(self.config_path) as json_file:
                credentials = Credentials.from_authorized_user_info(json.load(json_file))

        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.client_secret_path,
                                                                 self.scopes)
                credentials = flow.run_console()
            # Save the credentials for the next run
            with open(self.config_path, 'w') as json_file:
                json.dump(credentials.to_json(), json_file)

        return credentials

