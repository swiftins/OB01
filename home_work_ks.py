#Создай класс Task, который позволяет управлять задачами (делами). 
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус 
#(выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных 
#задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, time, status):
        self.description = description
        self.time = time
        self.status = status
        self.deals = []

    def add_task(self, task):
        self.deals.append(task)
        print(f"Добавлена задача, {task }")

    def mark_as_done(self):
        self.status = "выполнено"



t1 = Task("Испечь пирог", 2, "не выполнено")
t2 = Task("Сходить в парикмахерскую", 3, "не выполнено")
t3 = Task ("Посетить  выставку", 4 , "не выполнено")

    

