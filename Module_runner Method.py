def module_runner(self, module):
    result = sys.modules[module].run()
    self.store_module_result(result)
