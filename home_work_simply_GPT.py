#Создай класс Task, который позволяет управлять задачами (делами). 
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус 
#(выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных 
#задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, action, time):
        self.action = action
        self.time = time
        self.done = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, action, time):
        self.tasks.append(Task(action, time))

    def mark_task_done(self, action):
        for task in self.tasks:
            if task.action == action:
                task.done = True

    def show_pending_tasks(self):
        for task in self.tasks:
            if not task.done:
                print(f"- {task.action} (время выполнения: {task.time} час)")

# Пример использования
manager = TaskManager()

print(manager.tasks)
manager.add_task("Испечь пирог", 2)
manager.add_task("Сходить в парикмахерскую", 3)
manager.add_task("Посетить  выставку", 4)

manager.show_pending_tasks()
manager.mark_task_done("Испечь пирог")
manager.show_pending_tasks()
