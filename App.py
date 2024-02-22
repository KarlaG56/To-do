from flask import Flask
from src.ToDo.Infrastructure.routes.ToDoRoute import todo_blueprint

app = Flask(__name__)

app.register_blueprint(todo_blueprint, url_prefix="/toDo")

if __name__ == "__main__":
    app.run(debug=True)
