#!/usr/bin/python

from Task.Task import Task

my_task = Task(task_id=3)

#print("Add a task")
#desc = input("Set Task: ")
#desc = desc or my_task.get_desc()
#date = input("Set Date: ")
#date = date or my_task.get_date()
#alarm = input("y/N: ")
#alarm = alarm or "N"

#my_task.set_desc(desc)
#my_task.set_date(date)
#my_task.set_alarm(alarm)

#my_task.save_task()

#print("List each task stored")
#print((str(my_task.get_tasks())))
print("ID: ", my_task.get_unique_id())
print("Date: ", my_task.get_date())
print("Desc:", my_task.get_desc())
print("Alarm: ", my_task.get_alarm())

"""
my_task = task.new_task(each variable) and should be returned a Task instance
update my_task.set_DESC(variable) and update the record

task = Task.get_task(task id)
Task.delete_task(id)

"""
