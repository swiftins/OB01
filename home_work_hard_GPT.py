#Создай класс Task, который позволяет управлять задачами (делами). 
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус 
#(выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных 
#задач и вывода списка текущих (не выполненных) задач.


class Task():
    def __init__(self, action, time):
      self.action = action
      self.time = time
      self.done = False
    def mark_done(self):
      self.done = True
      
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, action, time):
       task = Task(action, time)
       self.tasks.append(task)
    
    def mark_task_done(self, action):
       for task in self.tasks:
            if task.action == action and not task.done:
               task.mark_done()
               print(f"Задача '{action}' отмечена как выполненная.")
               return
            print(f"Задача '{action}' не найдена или уже выполнена.")
    def show_pending_tasks(self):
        print("Текущие невыполненные задачи:")
        for task in self.tasks:
            if not task.done:
                print(f"- {task.action} (время выполнения: {task.action} час.)")
        print()
manager = TaskManager()
manager.add_task("Испечь пирог", 2 )
manager.add_task("Сходить в парикмахерскую", 3 )
manager.add_task("Посетить  выставку", 3 )
manager.show_pending_tasks()
manager.mark_task_done("Испечь пирог")
manager.mark_task_done("Посетить  выставку")

