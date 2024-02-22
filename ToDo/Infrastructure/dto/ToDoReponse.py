def response(todo):
    return {'id': todo.uuid, 'title': todo.title, 'check': todo.check, 'text': todo.text}