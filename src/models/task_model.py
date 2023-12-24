import pickle
import os

class TaskModel:
    TASKS_FILE = "data/tasks.txt"

    @staticmethod
    def load_tasks():
        try:
            if os.path.getsize(TaskModel.TASKS_FILE) > 0:
                with open(TaskModel.TASKS_FILE, "rb") as file:
                    tasks = pickle.load(file)
            else:
                tasks = []
        except FileNotFoundError:
            tasks = []
        except pickle.UnpicklingError:
            tasks = []
        return tasks

    @staticmethod
    def save_task(task_text):
        tasks = TaskModel.load_tasks()
        tasks.append(task_text)

        with open(TaskModel.TASKS_FILE, "wb") as file:
            pickle.dump(tasks, file)

    @staticmethod
    def remove_task(task_text):
        tasks = TaskModel.load_tasks()

        if task_text in tasks:
            tasks.remove(task_text)

            with open(TaskModel.TASKS_FILE, "wb") as file:
                pickle.dump(tasks, file)
        else:
            print(f"Task '{task_text}' not found in the tasks list.")
