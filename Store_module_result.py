def store_module_result(self, data):
        message = datetime.now().isoformat()  # Get the current time as a string
        remote_path = f'data/{self.id}/{message}.data'  # Define the remote path in the repository
        # Encode the data to base64
        bindata = base64.b64encode(bytes('%r' % data, 'utf-8'))
        # Create a new file in the repository with the encoded data
        self.repo.create_file(remote_path, message, bindata)
