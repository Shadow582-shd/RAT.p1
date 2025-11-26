def get_config(self):
    config_json = get_file_contents('config', self.config_file, self.repo)
    config = json.loads(base64.b64decode(config_json))
    for task in config:
        if task['module'] not in sys.modules:
            exec("import %s" % task['module'])
    return config
