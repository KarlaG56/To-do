from src.ToDo.Domain.Port.PortToDo import PortToDo

class DeleteToDoUseCase:
    def __int__(self, toDo_port:PortToDo):
        self.repository = toDo_port

    def run(self,id):
        self.repository.delete(id)