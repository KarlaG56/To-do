from src.ToDo.application.services.usesCases.DeleteToDoUseCase import DeleteToDoUseCase
from src.ToDo.Domain.Port.PortToDo import PortToDo

class DeleteController:
    def __int__(self, toDo_port:PortToDo):
        self.useCase = DeleteToDoUseCase(toDo_port)

    def run(self,id):
        self.useCase.run(id)
        return {'status': True}