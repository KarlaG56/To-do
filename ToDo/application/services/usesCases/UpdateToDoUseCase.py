from src.ToDo.Domain.Port.PortToDo import PortToDo

class UpdateToDoUseCase:
    def __init__(self, repository:PortToDo):
        self.repository = repository

    def run(self, id, data):
        return self.repository.update(id, data['title'],data['text'],data['check'])