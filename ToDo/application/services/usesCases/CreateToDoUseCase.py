from src.ToDo.Domain.Port.PortToDo import PortToDo
from src.ToDo.Domain.entities.ToDo import ToDo

class CreateToDoUseCase:
    def __init__(self, toDo_port:PortToDo):
        self.repository = toDo_port

    def run(self, data):
        toDo = ToDo(title=data["title"], text = data["text"], check = data["check"])
        return self.repository.create(toDo)

