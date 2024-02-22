import uuid

class ToDo:
    def __init__(self, title, text, check):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.text = text
        self.check = check