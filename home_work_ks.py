#Создай класс Task, который позволяет управлять задачами (делами). 
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус 
#(выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных 
#задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, description, time, status):
        self.description = description
        self.time = time
        self.status = status
        Deals.append(description)

    def add_task(self, task):
        self.deals.append(task)
        print(f"Добавлена задача, {task }")

    def mark_as_done(self):
        self.status = "выполнено"   
        Deals.remove(self.description)   
        Deals_done.append(self.description)

Deals_done = []
Deals = []

t1 = Task("Испечь пирог", 2, "не выполнено")
print(Deals)
t2 = Task("Сходить в парикмахерскую", 3, "не выполнено")
print(Deals)
t3 = Task ("Посетить  выставку", 4 , "не выполнено")
print(Deals)

print(t1.time, t2.time, t3.time)

t1.mark_as_done()
print(Deals)

t2.mark_as_done()
print(Deals)

print(t1.time, t2.time, t3.time)
print(t1.status,t2.status,t3.status)