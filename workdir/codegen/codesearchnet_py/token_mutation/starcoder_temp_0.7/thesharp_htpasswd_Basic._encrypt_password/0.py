def _encrypt_password(self, password):
        """encrypt the words for given data """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

