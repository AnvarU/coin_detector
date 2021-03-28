class Coin:
    def __init__(self, name, title, value, folder_name):
        self.name = name
        self.title = title
        self.value = value
        self.folder_name = folder_name

    def __repr__(self):
        return "<class '{}'>".format(self.name)