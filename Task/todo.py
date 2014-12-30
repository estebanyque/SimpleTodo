#!/usr/bin/python

from Task import Task

my_task = Task()

print(my_task.get_task(), my_task.get_date())

print("Set Task: ")
new_task = input()
my_task.set_task(new_task)

print ("new task set up to: ", my_task.get_task())
"""
print("Date: ")
date = input()
print("Task: ")
task = input()
print("Alarm(y/N)")
alarm = input()

print(date, task, alarm)
"""