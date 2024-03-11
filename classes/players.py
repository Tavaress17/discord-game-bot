class players:
    def __init__(self, name):
        self.name = name
        self.life = 3

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_life(self):
        return self.life

    def set_life(self, value):
        self.life = value