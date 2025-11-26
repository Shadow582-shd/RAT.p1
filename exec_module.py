def exec_module(self, module):
    # Execute the module code in the context of the module's dictionary
    exec(self.current_module_code, module.__dict__)
