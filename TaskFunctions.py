# TaskFunctions.py

from datetime import datetime
def addtask(assignment, deadline, priority, tasks):
    task_id = len(tasks) + 1
    tasks.append({
        'id': task_id,
        'assignment': assignment,
        'deadline': deadline,
        'priority': priority
    })


def displaytasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: (x['priority'], x['deadline']))

    print("\nAssigned Tasks:")
    for task in sorted_tasks:
        print(
            f"ID: {task['id']}, Assignment: {task['assignment']}, Deadline: {task['deadline']}, Priority: {task['priority']}")


def print_whole_list(tasks):
    print("\nComplete Task List:")
    print("ID\tAssignment\tDeadline\tPriority Level")
    for task in tasks:
        print(f"{task['id']}\t{task['assignment']}\t\t{task['deadline']}\t\t{task['priority']}")


def get_task_by_id(task_id, tasks):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        print("\nTask Details:")
        print(f"ID: {task['id']}")
        print(f"Assignment: {task['assignment']}")
        print(f"Deadline: {task['deadline']}")
        print(f"Priority: {task['priority']}")  # Fix: use 'priority' instead of 'priority_level'
    else:
        print(f"No task found with ID {task_id}")
