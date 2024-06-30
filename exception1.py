class Invalidchoice(Exception):
    def __init__(self,choice=0,action=0):
        self.choice = choice
        self.action =action
    def __str__(self):
        return f"_______Enter valid choice..._______"