import json
import os
from datetime import datetime  # 1. Import the datetime module
# Define the filename where the tasks will be stored
FILENAME = "task manager.json"

def load_tasks():
    """Loads tasks from the JSON file if it exists, otherwise returns an empty list."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Corrupted save file. Starting with an empty list.")
            return []
    return []

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def task_manager():
    # 1. Load existing tasks from the JSON file at startup
    task = load_tasks() 
    
    print("To Do List")
    print(
        "input 'l' to see list\n"
        "'e' to edit list\n"
        "'d' to del a list\n"
        "'c' to clear list\n"
        "'q' to quit"
    )
    print("-" * 30)
    
    while True:
        user_input = input("enter a list: ").strip()
        if user_input == "":
            print("please enter a valid list!")
            
        elif user_input.lower() == 'q':
            break
            
        elif user_input.lower() == 'l':
            if len(task) == 0:
                print("you havent added any list!")
            else:
                for index, lists in enumerate(task, start=1):
                    #time stamp will be shown
                    print(f"{index}. {lists['text']} (Created: {lists['created_at']})")
                    print("-" * 30)
                    
        elif user_input.lower() == 'e':
            if len(task) == 0:
                print("you havent added any list!")
            else:
                for index, lists in enumerate(task, start=1):
                    #time stamp will be shown
                    print(f"{index}. {lists['text']} (Created: {lists['created_at']})")
                    print("-" * 30)
                try:
                    item = int(input("enter a list number to edit: "))
                    if 0 < item <= len(task):
                        x = item - 1
                        new_task = input(f"list {item} to or 'c' to cancel: ")
                        if new_task == "":
                            print("please enter a valid list!")
                        elif new_task.lower() == 'c':
                            print("Edit canceled.")
                        else:
                            task[x]['text'] = new_task
                            # Save changes after editing
                            save_tasks(task)
                            print("Task successfully updated and saved!")
                    else:
                        print("invalid number! Please try again.")
                except ValueError:
                    print("Error: not a valid number!")
                    
        elif user_input.lower() == 'd':   
            if len(task) == 0:
                print("you havent added any list!") 
            else:            
                for index, lists in enumerate(task, start=1):
                    #time stamp will be shown
                    print(f"{index}. {lists['text']} (Created: {lists['created_at']})")
                    print("-" * 30)
                try:    
                    item = int(input("enter a number to delete list: "))
                    if 0 < item <= len(task):
                        x = item - 1
                        del task[x]
                        # Save changes after deleting
                        save_tasks(task)
                        print("Task successfully updated and saved!")
                    else:
                        print("invalid number! Please try again.")
                except ValueError:
                    print("Error: not a valid number!")
                    
        elif user_input.lower() == 'c':
            task.clear()
            # Save changes after clearing
            save_tasks(task)
            print("List cleared and saved!")
            
        else:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %I:%M %p")
            # 5. Build the dictionary and append it to our list
            new_item = {
                "text": user_input,
                "created_at": timestamp
            }
            task.append(new_item)
            # Save changes after adding a new item
            save_tasks(task)
            print("Task added and saved!")

task_manager()