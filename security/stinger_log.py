class Stinger:
    def __init__(self):
        self.blacklist = set()

    def check_immunity(self, sig):
        return sig in self.blacklist

    def mark_bot(self, sig):
        self.blacklist.add(sig)